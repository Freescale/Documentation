#!/usr/bin/env python3

import argparse
import contextlib
import logging
import os
import sys
import warnings

PATH = os.getenv('PATH').split(':')
bitbake_paths = [os.path.join(path, '..', 'lib')
                 for path in PATH if os.path.exists(os.path.join(path, 'bitbake'))]
if not bitbake_paths:
    raise ImportError("Unable to locate bitbake, please ensure PATH is set correctly.")

sys.path[0:0] = bitbake_paths

def find_yocto_root():
    def inner_find(dir):
        repo_dir = os.path.join(dir, '.repo')
        if os.path.exists(repo_dir) and os.path.isdir(repo_dir):
            return dir
        elif dir == '/':
            return False
        else:
            return inner_find(os.path.dirname(dir))
    BUILDDIR = os.environ.get('BUILDDIR')
    if BUILDDIR:
        yocto_root = inner_find(BUILDDIR)
    else:
        yocto_root = inner_find(os.getcwd())
    return yocto_root or die("ERROR: won't search from /.")

def get_yocto_path():
    types = ['poky', 'openembedded-core', 'oe']
    base = find_yocto_root()
    paths = [os.path.join(base, 'sources', t, 'scripts/lib') for t in types]
    path = list(filter(os.path.exists, paths))
    if len(path) != 1:
        print("ERROR: Can't find scripts path")
        sys.exit(1)
    sys.path.append(path[0])

basepath = ''

get_yocto_path()
from devtool import setup_tinfoil


class Terminate(BaseException):
    pass


class CompleteParser(argparse.ArgumentParser):
    """Argument parser which handles '--complete' for completions"""
    def __init__(self, *args, **kwargs):
        self.complete_parser = argparse.ArgumentParser(add_help=False)
        self.complete_parser.add_argument('--complete', action='store_true')
        super(CompleteParser, self).__init__(*args, **kwargs)

    def parse_args(self, args=None, namespace=None):
        parsed, remaining = self.complete_parser.parse_known_args(args)
        if parsed.complete:
            for action in self._actions:
                for string in action.option_strings:
                    print(string)
        else:
            return super(CompleteParser, self).parse_args(remaining, namespace)


def iter_uniq(iterable):
    """Yield unique elements of an iterable"""
    seen = set()
    for i in iterable:
        if i not in seen:
            seen.add(i)
            yield i


@contextlib.contextmanager
def status(message, outfile=sys.stderr):
    """Show the user what we're doing, and whether we succeed"""
    outfile.write('{0}..'.format(message))
    outfile.flush()
    try:
        yield
    except KeyboardInterrupt:
        outfile.write('.interrupted\n')
        raise
    except Terminate:
        outfile.write('.terminated\n')
        raise
    except BaseException:
        outfile.write('.failed\n')
        raise
    outfile.write('.done\n')


def setup_log_handler(logger, output=sys.stderr):
    log_format = bb.msg.BBLogFormatter("%(levelname)s: %(message)s")
    if output.isatty() and hasattr(log_format, 'enable_color'):
        log_format.enable_color()
    handler = logging.StreamHandler(output)
    handler.setFormatter(log_format)

    bb.msg.addDefaultlogFilter(handler)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


def sigterm_exception(signum, stackframe):
    raise Terminate()

###### end of bbcmd

import pickle

def load_data(data_file):
    try:
        fd = open(data_file, 'rb')
        data = pickle.load(fd)
        fd.close()
        return data
    except:
        return {}

def dump_data(data, data_file):
    fd = open(data_file, 'wb')
    pickle.dump(data, fd, protocol=2)
    fd.close()

def extract_bitbake_metadata(recipes):
    try:
        tinfoil = setup_tinfoil(config_only=True, basepath=basepath)
        tinfoil.parseRecipes()

        data = {}

        try:
            metadata = tinfoil.parse_recipe("virtual/kernel")
        except:
            sys.exit(1)

        machine = metadata.getVar('MACHINE', True)
        data['image-bootloader'] = metadata.getVar('IMAGE_BOOTLOADER', True)
        data['soc-family'] = metadata.getVar('SOC_FAMILY', True)
        if data['soc-family'] is None:
            data['soc-family'] = metadata.getVar('MACHINEOVERRIDES', True)
        data['recipes'] = {}

        metadata = None
        for recipe in recipes:
            try:
                metadata = tinfoil.parse_recipe(recipe)
            except:
                continue

            pv = metadata.getVar('PV', True)
            localversion = metadata.getVar('LOCALVERSION', True)
            version = pv + (localversion or '')

            data['recipes'][recipe] = {}
            data['recipes'][recipe]['recipe'] = metadata.getVar('PN', True)
            data['recipes'][recipe]['version'] = version
            data['recipes'][recipe]['file'] = tinfoil.get_recipe_file(recipe)
            data['recipes'][recipe]['srcbranch'] = metadata.getVar('SRCBRANCH', True)
            data['recipes'][recipe]['compatible-machine'] = metadata.getVar('COMPATIBLE_MACHINE', True)

            description = metadata.getVar('DESCRIPTION', True)
            if not description:
                description = metadata.getVar('SUMMARY', True)
            data['recipes'][recipe]['description'] = description

        return {machine: data}

    finally:
        tinfoil.shutdown()


data_file = sys.argv[1]
user_recipes = sys.argv[2:]

data = load_data(data_file)
data.update(extract_bitbake_metadata(user_recipes))

dump_data(data, data_file)
