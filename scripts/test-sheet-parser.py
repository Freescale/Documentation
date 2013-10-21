#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import csv

def usage(exit_code=None):
    msg = '''Usage: %s <csv file> <fsl repos dir>

<csv file> is the CSV file with the for responses.

<fsl repos dir> is the directory under which the Freescale
repositories (meta-fsl-arm and meta-fsl-arm-extra) can be found.
''' % os.path.basename(sys.argv[0])
    if exit_code is not None and exit_code != 0:
        sys.stderr.write(msg)
        sys.exit(exit_code)
    sys.stdout.write(msg)


###
### rst utils
###
def rst_header(level, text):
    if level == 1:
        h = '=' * len(text)
        return h + '\n' + text + '\n' + h + '\n'
    elif level == 2:
        h = '-' * len(text)
        return h + '\n' + text + '\n' + h + '\n'
    elif level == 3:
        h = '=' * len(text)
        return text + '\n' + h + '\n'
    elif level == 4:
        h = '-' * len(text)
        return text + '\n' + h + '\n'
    else:
        raise

def rst_item(text, level=0, bullet='*'):
    return '%s%s %s\n' % (' ' * (level * 2), bullet, text)

### end rst utils

def read_test_sheet(csv_file):
    try:
        with open(csv_file, 'rb') as csv_fd:
            reader = csv.reader(csv_fd, delimiter=',')
            return list(reader)
    except IOError:
        print('Could not read %s.  Aborting.') % csv_file
        sys.exit(1)

def parse_board_file(board_file):
    def get_descr(line):
        return ' '.join(line.split(':')[1:]).strip()
    try:
        with open(board_file, 'r') as bf:
            board_spec = {}
            for line in bf.readlines():
                if line.startswith('#@NAME'):
                    board_spec['name'] = get_descr(line)
                elif line.startswith('#@SOC'):
                    board_spec['soc'] = get_descr(line)
            return board_spec
    except IOError:
        print('Could not read %s.') % board_file


def get_supported_boards(repos_dir):
    boards = {}
    for current, dirs, files in os.walk(repos_dir):
        if os.path.basename(current) == 'machine':
            if current.find('sources/meta-fsl') == -1:
                continue

            for file in files:
                if file.endswith('.conf'):
                    boards[file.replace('.conf', '')] = parse_board_file(os.path.join(current, file))
    return boards


fields = ['timestamp',
          'tester',
          'tester_email',
          'board',
          'image',
          'boot?',
          'kernel_works?',
          'kernel_log',
          'x11_works?',
          'x11_log',
          'plays_movie?',
          'plays_mp3?',
          'additional_comments',
          'preferred_provider_kernel',
          'uname',
          'memtester?',
          'dummy1',
          'plays_wav?'
          'usb',
          'sdcard',
          'evtest',
          'video_playback_plugins',
          'video_capture',
          'dummy2',
          'video_encoding_plugins',
          'directfb_works?',
          'tune',
          'mentester']


def column(key, row):
    i = fields.index(key)
    return row[i]

def get_testers_by_board_image(board, image, test_sheet):
    return [ (column('tester', row), board, image) \
                 for row in test_sheet if column('board', row) == board and column('image', row) == image ]

def get_testers_by_board(board, test_sheet):
    return [ (column('tester', row), board, column('image', row)) \
                 for row in test_sheet if column('board', row) == board ]


def process_test_sheet(test_sheet, repos_dir):
    header = test_sheet[0]
    responses = test_sheet[1:]
    responses_by_board = {}
    board_index = fields.index('board')
    supported_boards = get_supported_boards(repos_dir)


    # for row in test_sheet:
    #     print row

    for response in responses:
        board = response[board_index]
        if board not in responses_by_board.keys():
            responses_by_board[board] = []
        responses_by_board[board].append(response)

    for board, responses in responses_by_board.items():
        print(rst_header(2, '%s (%s)' % (supported_boards[board]['name'],
                                         supported_boards[board]['soc'],)))

        testers_data = get_testers_by_board(board, responses)
        testers = list(set([ t[0] for t in testers_data ]))
        tester_str = None
        if len(testers) > 1:
            tester_str = 'persons'
        else:
            tester_str = 'person'

        images = list(set([ t[2] for t in testers_data ]))
        image_str = None
        was = None
        if len(images) > 1:
            image_str = 'images'
            was = 'were'
        else:
            image_str = 'image'
            was = 'was'



        print('This board was tested by %d %s.\n' % (len(testers), tester_str))
        print('%d %s %s used:\n' % (len(images), image_str, was))
        for image in images:
            print '  * ' + image

        # Omit the first 4 questions (personal + board) and empty questions
        # for qno, question in enumerate(header):
        #     if qno > 3 and question != '':
        #         print(rst_item(question))
        #         for responses in responses_by_board[board]:
        #             resp = responses[qno]
        #             if resp:
        #                 print(rst_item(resp, level=1))
        #         print('')

        print('\n')

    not_tested = set(supported_boards.keys()) - set(responses_by_board.keys())

    print(rst_header(1, "Not tested boards"))

    if len(not_tested) > 0:
        print('The following boards have not been tested:\n')
        for board in not_tested:
            print(rst_item('%s (%s)' % (supported_boards[board]['name'],
                                        supported_boards[board]['soc'] + ')')))


def main():
    if '-h' in sys.argv or '-help' in sys.argv or '--help' in sys.argv:
        usage(0)

    if len(sys.argv) < 3:
        usage(1)

    csv_file = sys.argv[1]
    repos_dir = sys.argv[2]
    process_test_sheet(read_test_sheet(csv_file), repos_dir)


if __name__ == '__main__':
    main()
