#! /usr/bin/env python
from doc_utils import tabularize
import csv
import os
import sys


def process_machines_table(csv_table):
    return tabularize(csv_table)

def read_csv_file(csv_file):
    try:
        with open(csv_file, 'rb') as csv_fd:
            reader = csv.reader(csv_fd, delimiter=',')
            return list(reader)
    except IOError:
        sys.stderr.write('Could not read %s.  Aborting.\n') % csv_file
        sys.exit(1)


def usage(exit_code=None):
    msg = '''Usage: %s <csv file>

<csv file> is the CSV file with the machines.
''' % os.path.basename(sys.argv[0])
    if exit_code is not None and exit_code != 0:
        sys.stderr.write(msg)
        sys.exit(exit_code)
    sys.stdout.write(msg)


def main():
    if '-h' in sys.argv or '-help' in sys.argv or '--help' in sys.argv:
        usage(0)

    if len(sys.argv) < 2:
        usage(1)

    csv_file = sys.argv[1]
    table = process_machines_table(read_csv_file(csv_file))
    print(table.strip())


if __name__ == '__main__':
    main()
