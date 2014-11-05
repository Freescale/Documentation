#! /usr/bin/env python
# Call this file on the command line with "-h" as argument to get all the
# available options.

import argparse
import csv
import os
import re
import sys
import time
import urllib2
from doc_utils import tabularize

BASE_DIRECTORY = os.path.dirname(os.path.realpath(__file__ + "/../"))

CLOSED_BUGS_URL = "https://bugzilla.yoctoproject.org/buglist.cgi?v4=meta-fsl-arm&o5=substring&f1=OP&o3=substring&v6=meta-fsl-arm&o7=matches&f0=OP&f8=CP&v3=meta-fsl-arm&o2=substring&o6=substring&v7=%22meta-fsl-arm%22&f9=CP&f4=alias&chfieldto=Now&v5=meta-fsl-arm&chfield=bug_status&query_format=advanced&j1=OR&f3=component&chfieldfrom=<<START_DATE>>&f2=product&o4=substring&bug_status=RESOLVED&bug_status=VERIFIED&bug_status=CLOSED&f5=short_desc&f6=status_whiteboard&v2=meta-fsl-arm&f7=content&ctype=csv"
CLOSED_BUGS_OUTPUT_FILE_PATH = BASE_DIRECTORY + "/release-notes/source/closed_bugs.inc"

OPEN_BUGS_URL = "https://bugzilla.yoctoproject.org/buglist.cgi?quicksearch=meta-fsl-arm&chfieldfrom=<<START_DATE>>&ctype=csv"
OPEN_BUGS_OUTPUT_FILE_PATH = BASE_DIRECTORY + "/release-notes/source/open_bugs.inc"

def request_bug_list(url):
    buffer = urllib2.urlopen(url)
    csv_bug_list = buffer.read()
    buffer.close()
    return csv_bug_list

def parse_data(csv_bug_list, columns_to_keep):
    data = []
    column_names_ids = columns_to_keep.keys()
    column_names = columns_to_keep.values()
    csv_bug_rows = csv.reader(csv_bug_list.splitlines(), delimiter=',', quotechar='"')

    for row in csv_bug_rows:
        selected_row = []
        for column_name_id in column_names_ids:
            selected_row.append(row[column_name_id])
        data.append(selected_row)

    for idx, column_name in enumerate(column_names):
        data[0][idx] = column_name

    return data

def write_to_file(file_path, data):
    if(file_path == "-"):
        print "\n" + data
    else:
        print 'Writing to file "' + file_path + '"...'
        f = open(file_path, 'w')
        f.write(data)
        f.close()
        print "Done!"

def generate_bugs_file(url, output_file_path, columns_to_keep):
    print "Requesting bugs list in CSV format from https://bugzilla.yoctoproject.org/..."
    csv_bug_list = request_bug_list(url)
    print "Parsing data..."
    data = parse_data(csv_bug_list, columns_to_keep)
    print "Building table..."
    table = tabularize(data)
    write_to_file(output_file_path, table)

def process_arguments():
    desc = ('Generates a ReST table of the meta-fsl-arm bugs present on the ' +
            'Bugzilla bug list of the Yocto Project.')
    parser = argparse.ArgumentParser(description=desc)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-o', '--open-bugs', dest='bug_type', action='store_const',
                       const='open-bugs', default='open-bugs',
                       help='Create a ReST table of open bugs (default)')
    group.add_argument('-c', '--closed-bugs', dest='bug_type', action='store_const',
                       const='closed-bugs',
                       help='Create a ReST table of closed bugs')
    parser.add_argument('-D', '--start-date', metavar='date',
                        dest='start_date',
                        help='Minimmal bug creation date in the format: ' +
                        'YYYY-MM-DD. All bugs created before that will be ' +
                        'ignored. Defaults to "2014-01-01" for closed bugs.')
    parser.add_argument('-O', '--output', metavar='output', default=None,
                        help='Where the generated table is written. Use "-" ' +
                        'for STDOUT. By default it is based on the type of ' +
                        'bugs selected: "' + OPEN_BUGS_OUTPUT_FILE_PATH +
                        '" for open bugs; "' + CLOSED_BUGS_OUTPUT_FILE_PATH +
                        '" for closed bugs.')
    args = parser.parse_args()

    if(args.bug_type == 'closed-bugs'):
        start_processing_message = "Generating table for closed bugs..."
        url = CLOSED_BUGS_URL
        if(args.output):
            output = args.output
        else:
            output = CLOSED_BUGS_OUTPUT_FILE_PATH
        if(args.start_date):
            start_date = args.start_date
        else:
            start_date = "2014-01-01"
        columns_to_keep = {0: "Bug ID", 5: "Resolution", 6: "Summary"}
    else:
        start_processing_message = "Generating table for open bugs..."
        url = OPEN_BUGS_URL
        if(args.output):
            output = args.output
        else:
            output = OPEN_BUGS_OUTPUT_FILE_PATH
        if(args.start_date):
            start_date = args.start_date
        else:
            start_date = ""
        columns_to_keep = {0: "Bug ID", 4: "Status", 6: "Summary"}

    if(start_date):
        # check if the suplied start_date is valid:
        try:
            time.strptime(start_date, "%Y-%m-%d")
        except ValueError:
            print(os.path.basename(sys.argv[0]) +
                  ": error: start_date must be in the following format: " +
                  "YYYY-MM-DD")
            exit(1)

    print start_processing_message
    url = re.sub('<<START_DATE>>', start_date, url)
    return [url, output, columns_to_keep]

url, file_path, columns_to_keep = process_arguments()
generate_bugs_file(url, file_path, columns_to_keep)
