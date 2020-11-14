#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
import re
import sys
import pickle
import subprocess
import copy
import shutil
from functools import reduce
from doc_utils import tabularize

def info(fmt, *args):
    print(fmt % args)

def warn(fmt, *args):
    sys.stderr.write(('WARNING: ' + fmt + '\n') % args)

def error(fmt, *args):
    sys.stderr.write(('ERROR: ' + fmt + '\n') % args)

def describe(items):
    text = ''
    for item in sorted(items):
        text += ''.join(['* ', '**', item[0], '**: ', item[1], '\n'])
    return text

def is_in_soc_family(soc, soc_family):
    return soc in soc_family.split(':')

def is_compatible_machine(soc_family, compatible_machine_re):
    if compatible_machine_re:
        socs = soc_family.split(':')
        compatible_machine_pattern = re.compile(compatible_machine_re)
        for soc in socs:
            if compatible_machine_pattern.match(soc):
                return True
        return False
    else:
        return True

def format_version(version):
    version = str(version)
    if 'gitAUTOINC' in version:
        version_pattern = re.compile('(.*)gitAUTOINC.*')
        version_number = version_pattern.match(version).groups()[0]
        return version_number + 'git'
    else:
        ## remove <x> in case versions are in the <x>:<y> format
        comma_prefix = re.compile('\\d+:(.*)')
        match = comma_prefix.match(version)
        if match:
            return match.groups()[0]
        else:
            return version

def write_inc_file(out_dir, file, text):
    out_file = os.path.join(out_dir, file)
    info('Writing %s' % out_file)
    out_fd = open(out_file, 'w')
    out_fd.write(text)
    out_fd.close()

def write_tabular(out_dir, file, header, body):
    table = [header] + body
    write_inc_file(out_dir, file, tabularize([header] + body))

def write_table_by_recipe(out_dir, file, recipe, header, data):
    body = []
    for board in data.keys():
        recipe_data = data[board]['recipes'][recipe]
        version = format_version(recipe_data['version'])
        body += [[board, recipe_data['recipe'], version]]
    write_tabular(out_dir, file, header, body)

def write_linux_default(data, out_dir):
    write_table_by_recipe(out_dir,
                          'linux-default.inc',
                          'virtual/kernel',
                          ['Board', 'Kernel Provider', 'Kernel Version'],
                          data)


def write_bootloader_default(data, out_dir):
    boards_bloaders = {}
    for  board, board_data in data.items():
        if 'u-boot' in board_data['recipes']:
            bootloader = board_data['recipes']['u-boot']
            boards_bloaders[board] = (bootloader['recipe'], bootloader['version'])
        elif 'virtual/bootloader' in board_data['recipes']:
            bootloader = board_data['recipes']['virtual/bootloader']
            boards_bloaders[board] = (bootloader['recipe'], bootloader['version'])
        else:
            error('No bootloader for %s' % (board,))
            sys.exit(1)

    body = []
    for board, bootloader in boards_bloaders.items():
        body.append([board, bootloader[0], format_version(bootloader[1])])
    write_tabular(out_dir,
                  'bootloader-default.inc',
                  ['Board', 'Bootloader', 'Bootloader version'],
                  body)

def write_fsl_community_bsp_supported_kernels(data, out_dir):
    kernels = []
    kernel_recipes = [] # just to keep track of recipes already collected
    for board, board_data in data.items():
        kernel = board_data['recipes']['virtual/kernel']
        recipe = kernel['recipe']
        recipe_file = kernel['file']
        if (('/sources/meta-freescale/' in recipe_file) or \
                ('/sources/meta-freescale-3rdparty/' in recipe_file)) and \
                recipe not in kernel_recipes:
            kernels += [[recipe, kernel['description']]]
            kernel_recipes.append(recipe)
    write_inc_file(out_dir, 'fsl-community-bsp-supported-kernels.inc', describe(kernels))

def write_fsl_community_bsp_supported_bootloaders_descr(data, out_dir):
    bootloaders = []
    bootloader_recipes = [] # just to keep track of recipes already collected
    for board, board_data in data.items():
        for bootloader_software in ['u-boot', 'barebox']:
            if bootloader_software in board_data['recipes']:
                bootloader = board_data['recipes'][bootloader_software]
                recipe = bootloader['recipe']
                recipe_file = bootloader['file']
                if (('/sources/meta-freescale/' in recipe_file) or \
                        ('/sources/meta-freescale-3rdparty/' in recipe_file)) and \
                        recipe not in bootloader_recipes:
                    bootloaders += [[recipe, bootloader['description']]]
                    bootloader_recipes.append(recipe)
    write_inc_file(out_dir, 'fsl-community-bsp-supported-bootloaders-descr.inc', describe(bootloaders))

def write_userspace_pkg(data, out_dir):
    pkgs = {'gstreamer1.0': [],
            'udev': []}
    for board, board_data in data.items():
        for pkg in pkgs.keys():
            versions = pkgs[pkg]
            version = board_data['recipes'][pkg]['version']
            if version not in versions:
                pkgs[pkg].append(version)

    ## Check if all the versions are the same for each package
    multiple_versions = []
    for pkg, versions in pkgs.items():
        if len(versions) > 1:
            multiple_versions.append((pkg, versions))
    for pkg, vs in multiple_versions:
        error('multiple versions have been found for %s: %s' % (pkg, ', '.join(map(str, vs))))
    if multiple_versions:
        sys.exit(1)

    ## Check if packages are available for all SoCs:
    pkg_board_restriction = False
    for pkg in pkgs:
        for board_data in data.values():
            compatible_machine = board_data['recipes'][pkg]['compatible-machine']
            if compatible_machine:
                pkg_board_restriction = True
                error('Package %s has restrictions with regard to boards: COMPATIBLE_MACHINE=%s' % (pkg, compatible_machine))
    if pkg_board_restriction:
        sys.exit(1)

    ## Finaly write the table
    write_tabular(out_dir,
                  'userspace-pkg.inc',
                  ['Package', 'Board/SoC Family', 'Version'],
                  [ [pkg, 'All', format_version(version[0])] for pkg, version in pkgs.items() ])


def write_soc_pkg(data, out_dir):
    boards = [
        'imx23evk',
        'imx25pdk',
        'imx28evk',
        'imx51evk',
        'imx53ard',
        'imx53qsb',
        'imx6qdlsabreauto',
        'imx6qdlsabresd',
        'imx6slevk',
        'imx6sllevk',
        'imx6sxsabreauto',
        'imx6sxsabresd',
        'imx6ulevk',
        'imx6ullevk',
        'imx7dsabresd',
        'imx7ulpevk',
        'imx8mmevk',
        'imx8mnevk',
        'imx8mpevk',
        'imx8mqevk',
        'imx8qmmek',
        'imx8qxpmek'
    ]

    socs = {
        'mxs': [],
        'mx5': [],
        'mx6sl': [],
        'mx6dl': [],
        'vf60': [],
        'mx8qm': [],
        'mx8mm': [],
        'mx8mn': [],
        'mx8mp': [],
        'mx8mq': [],
        'mx8qxp': []
    }

    pkgs = [
        'firmware-imx-8',
        'firmware-imx-8m',
        'firmware-imx',
        'firmware-sof-imx',
        'firmware-qca6174',
        'firmware-qca9377',
        'qca-tools',
        'imx-atf',
        'imx-kobs',
        'imx-lib',
        'imx-boot',
        'imx-mkimage',
        'imx-sc-firmware',
        'imx-seco-libs',
        'imx-seco',
        'imx-test',
        'imx-uuc',
        'imx-vpu-hantro-vc',
        'imx-vpu-hantro',
        'imx-vpu',
        'libimxdmabuffer',
        'mxsldr',
        'u-boot-fslc',
        'u-boot-imx',
        'u-boot-imx-tools',
        'udev',
        'devregs',
        'imx-usb-loader',
        'libdrm-armada',
        'libdrm',
        'imx-dpu-g2d',
        'imx-gpu-apitrace',
        'imx-gpu-g2d',
        'imx-gpu-viv',
        'imx-gpu-viv',
        'wayland-protocols',
        'weston',
        'xf86-video-armada',
        'xf86-video-imx-vivante',
        'kernel-module-imx-gpu-viv',
        'kernel-module-qca6174',
        'kernel-module-qca9377',
        'linux-fslc-imx',
        'linux-fslc-lts-4.19',
        'linux-imx',
        'imx-alsa-plugins',
        'gstreamer1.0-libav',
        'gstreamer1.0-plugins-bad',
        'gstreamer1.0-plugins-base',
        'gstreamer1.0-plugins-good',
        'gstreamer1.0-plugins-imx',
        'gstreamer1.0-plugins-ugly',
        'gstreamer1.0-rtsp-server',
        'gstreamer1.0',
        'imx-gst1.0-plugin',
        'imx-codec',
        'imx-dspc-asrc',
        'imx-parser',
        'imx-vpuwrap',
        'libimxvpuapi2',
        'libimxvpuapi',
        'optee-client',
        'optee-os',
        'optee-test',
        'systemd'
    ]

    ## Fill the socs dictionary
    for board, board_data in data.items():
        if board not in boards:
            continue

        soc_family = board_data['soc-family']
        for soc in socs.keys():
            if is_in_soc_family(soc, soc_family):
                socs[soc].append(board)
    ## Check if the same board is not in multiple SoCs
    boards_socs = {}
    board_in_multiple_socs = False
    for soc, boards in socs.items():
        for board in boards:
            if board in boards_socs:
                board_in_multiple_socs = True
                error('Board %s has been found in both %s and %s SoCs' % (board, boards_socs[board], soc))
            else:
                boards_socs[board] = soc
    if board_in_multiple_socs:
        sys.exit(1)

    ## Use the most frequent package versions among boards of the same
    ## SoC, in case of different versions for the same package
    pkgs_socs_versions = {}
    for pkg in pkgs:
        for soc, boards in socs.items():
            if boards:
                pkg_versions = {}
                for board in boards:
                    if pkg in data[board]['recipes']:
                        recipe = data[board]['recipes'][pkg]
                        compatible_machine = recipe['compatible-machine']
                        if compatible_machine is None:
                            pkg_versions[board] = recipe['version']
                        elif (compatible_machine and \
                              is_compatible_machine(data[board]['soc-family'], compatible_machine)):
                            pkg_versions[board] = recipe['version']
                        else:
                            ## The package is not for that board
                            pkg_versions[board] = -1
                    else:
                        pkg_versions[board] = -1

                versions_histogram = {}
                for version in pkg_versions.values():
                    if version in versions_histogram:
                        versions_histogram[version] += 1
                    else:
                        versions_histogram[version] = 1
                versions_freq = list(versions_histogram.values())
                most_freq = max(versions_freq)
                num_most_freq = versions_freq.count(most_freq)

                ## imx-test is a special case: it has a "fake" version
                ## number (00.00.00) that must be specially handled.
                if (pkg == 'imx-test' and
                    num_most_freq == 2 and
                    '00.00.00' in versions_histogram.keys()):
                    del versions_histogram['00.00.00']
                    num_most_freq -= 1

                ## More than one "most frequent" version?
                if num_most_freq > 1:
                    error('The most frequent versions (%s) for %s are equally distributed among boards of SoC %s.  Cannot determine which one to use.' % \
                              ([ ver for ver, count in versions_histogram.items() if count == most_freq ],
                               pkg,
                               soc))
                    sys.exit(1)
                else:
                    pkg_version = None
                    for version, count in versions_histogram.items():
                        if count == most_freq:
                            pkg_version = version
                            break
                    pkgs_socs_versions[(pkg, soc)] = pkg_version

    ## Build up the table body
    body = []
    soc_names = list(filter(lambda soc: socs[soc], sorted(socs.keys())))
    for pkg in pkgs:
        versions = [ pkgs_socs_versions[(pkg, soc)] for soc in soc_names ]
        def replace_noversions(versions):
            new_versions = []
            for v in versions:
                if v == -1:
                    new_versions.append('--')
                else:
                    new_versions.append(format_version(v))
            return new_versions
        body.append([pkg] + replace_noversions(versions))

    ## Finally write the table
    write_tabular(out_dir,
                  'soc-pkg.inc',
                  ['Package name'] + list(map(lambda soc: 'mx6q / mx6dl' if soc == 'mx6dl' else soc,  soc_names)),
                  body)


def write_maintainers_tables(data, out_dir, bsp_dir):
    meta_freescale_machines_dir = os.path.join(bsp_dir, 'sources', 'meta-freescale', 'conf', 'machine')
    meta_freescale_3rdparty_machines_dir = os.path.join(bsp_dir, 'sources', 'meta-freescale-3rdparty', 'conf', 'machine')
    get_maintainer_script = os.path.join(bsp_dir, 'sources', 'meta-freescale', 'scripts', 'get-maintainer')
    try:
        get_maintainer_pipe = subprocess.Popen([get_maintainer_script,
                                                '--dump',
                                                meta_freescale_machines_dir,
                                                meta_freescale_3rdparty_machines_dir],
                                               stdout=subprocess.PIPE)
    except OSError:
        error('Could not run the get-maintainer script (attempted %s)' % (get_maintainer_script,))
        sys.exit(1)

    get_maintainer_output = get_maintainer_pipe.communicate()[0].decode()
    maintained = []
    not_maintained = []
    for line in get_maintainer_output.splitlines():
        if line == '':
            continue
        columns = line.split('\t')
        len_cols = len(columns)
        if len_cols == 2:
            not_maintained.append(columns)
        elif len_cols == 3:
            maintained.append(columns[0:2])
        else:
            error('write_maintainers_tables: unexpected get-maintainers output format.')

    ## Write the maintained boards file
    write_tabular(out_dir,
                  'machines-with-maintainers.inc',
                  ['Machine', 'Name'],
                  maintained)

    ## Write the unmaintained boards file
    write_tabular(out_dir,
                  'machines-without-maintainers.inc',
                  ['Machine', 'Name'],
                  not_maintained)


def write_machines_list(data, out_dir, bsp_dir):
    output_machine_list_script = './output-machine-list'
    try:
        output_machine_list_pipe = subprocess.Popen([output_machine_list_script,
                                                     bsp_dir,
                                                     'tabularize'],
                                                    stdout=subprocess.PIPE)
    except OSError:
        error('Could not run the output-machine-list script (attempted %s)' % (output_machine_list_script,))
        sys.exit(1)

    out, err = output_machine_list_pipe.communicate()
    out_file = os.path.join(out_dir, 'machine-list.inc')
    info('Writing %s' % out_file)
    fd = open(out_file, 'w')
    fd.write(str(out))
    fd.close()


def write_soc_tree(data, out_dir):
    SOCS_FAMILIES = {
        re.compile("mx(\d|s)"): 'i.MX',
        re.compile("vf(\d+)?"): 'Vybrid',
        re.compile("ls102xa"): 'Layerscape'
    }

    VALID_SOCS = re.compile(r'mxs|mx2[0-9]|mx5[0-9]?|mx6(?:dl|q|sl+|sx|ul+)?|mx7(?:d?|ulp)|mx8(?:mm|mn|mp|pq|qm|qxp)|ls104[3-6]a]|vf(?:[5-6]0)?|ls102xa')

    PADDING="   "

    def print_tree(tree, fd, padding=PADDING):
        for key in sorted(tree.keys(), key=lambda s: s.lower()):
            value = tree[key]
            if any(value):
                print_tree(value, fd, padding + key + " -> ")
            else:
                fd.write(padding + key + ";\n")

    def dict_merge(a, b):
        if not isinstance(b, dict):
            return b
        result = copy.deepcopy(a)
        for k, v in b.items():
            if k in result and isinstance(result[k], dict):
                    result[k] = dict_merge(result[k], v)
            else:
                result[k] = copy.deepcopy(v)
        return result

    def socs2dict(socs):
        tree = {}
        for branch in socs:
            tmp = {}
            reduce(lambda d, key: d.setdefault(key, {}), branch, tmp)
            tree = dict_merge(tree, tmp)
        return tree

    def include_preample(preample_file, fd):
        with open(preample_file, 'r') as preamble:
            for line in preamble:
                fd.write(PADDING + line)
        fd.write("\n")

    soc_families = []
    for board, board_data in data.items():
        sf = board_data['soc-family']
        result = VALID_SOCS.findall(sf)
        soc_family = ":".join(result)
        if soc_family not in soc_families:
            soc_families.append(soc_family)

    max_depth = 2
    socs = map(lambda i: i[0][0:max_depth],
               zip(map(lambda soc_family: soc_family.split(':'),
                       soc_families)))

    socs_dict = {}
    for key, value in socs2dict(socs).items():
        for pattern, family in SOCS_FAMILIES.items():
            if pattern.match(key):
                if not family in socs_dict.keys():
                    socs_dict[family] = {}
                socs_dict[family][key] = value

    out_file = os.path.join(out_dir, 'soc-tree.diag')
    info('Writing %s' % out_file)
    fd = open(out_file, 'w')
    fd.write("blockdiag SoCs {\n")
    include_preample('./blockdiag.preample', fd)
    print_tree(socs_dict, fd)
    fd.write("}\n")
    fd.close()

def write_recipe_descriptions(recipe_pattern, data, out_file):
    wanted = {}
    for board, board_data in data.items():
        recipes = board_data['recipes']
        for recipe, recipe_data in recipes.items():
            if recipe_pattern in recipe:
                # nevermind clobbering previous findings
                wanted[recipe] = recipe_data['description']
    fd = open(out_file, 'w')
    info('Writing %s' % out_file)
    for recipe in sorted(wanted.keys()):
        fd.write('* **%s**: %s\n' % (recipe, wanted[recipe]))
    fd.close()

def write_image_descriptions(data, out_dir):
    write_recipe_descriptions('image', data, os.path.join(out_dir, 'images.inc'))

def write_packagegroup_descriptions(data, out_dir):
    write_recipe_descriptions('packagegroup', data, os.path.join(out_dir, 'packagegroups.inc'))

def write_acknowledgements(out_dir, bsp_dir, gitdm_dir, start_commit, end_commit):
    meta_freescale_dir = os.path.join(gitdm_dir, 'meta-freescale')
    gen_statistics_script = os.path.join(meta_freescale_dir, 'gen-statistics')
    anchor = os.getcwd()
    try:
        os.chdir(meta_freescale_dir)
        subprocess.call([gen_statistics_script,
                         bsp_dir,
                         start_commit,
                         end_commit],
                        stdout=subprocess.PIPE)
        os.chdir(anchor)
    except OSError:
        error('Could not run the gen-statistics script (attempted %s)' % (gen_statistics_script,))
        sys.exit(1)

    out_file = os.path.join(out_dir, 'ack-sourcers.inc')
    info('Writing %s' % out_file)
    shutil.copyfile(os.path.join(meta_freescale_dir, 'results.all.txt'),
                    out_file)


def usage(exit_code=None):
    print('Usage: %s <data file> <output dir> <bsp dir> <gitdb dir> <start commit> <end commit>' % (os.path.basename(sys.argv[0]),))
    if exit_code:
        sys.exit(exit_code)


if '-h' in sys.argv or '-help' in sys.argv or '--help' in sys.argv:
    usage(0)

if len(sys.argv) < 6:
    usage(1)

data_file = sys.argv[1]
out_dir = sys.argv[2]
bsp_dir = sys.argv[3]
gitdm_dir = sys.argv[4]
start_commit = sys.argv[5]
end_commit = sys.argv[6]

data_fd = open(data_file, 'rb')
data = pickle.load(data_fd)
data_fd.close()

try:
    os.mkdir(out_dir)
except:
    if not os.path.isdir(out_dir):
        sys.stderr.write('A file named %s already exists. Aborting.' % out_dir)
        sys.exit(1)
    else:
        pass # if a directory already exists, it's ok

write_linux_default(data, out_dir)
write_fsl_community_bsp_supported_kernels(data, out_dir)
write_fsl_community_bsp_supported_bootloaders_descr(data, out_dir)
write_bootloader_default(data, out_dir)
write_userspace_pkg(data, out_dir)
write_soc_pkg(data, out_dir)
write_maintainers_tables(data, out_dir, bsp_dir)
write_machines_list(data, out_dir, bsp_dir)
write_soc_tree(data, out_dir)
write_image_descriptions(data, out_dir)
write_packagegroup_descriptions(data, out_dir)
write_acknowledgements(out_dir, bsp_dir, gitdm_dir, start_commit, end_commit)
