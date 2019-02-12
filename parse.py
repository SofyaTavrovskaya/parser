#!/usr/bin/python3


import re
from log_entry import LogEntry


def parse_file(path_to_file):
    '''

    :param path_to_file:
    :return:
    '''
    result = []
    lines = []
    with open(path_to_file, "rt") as fo:
        error_block_flag = False

        for line in fo.readlines():
            split_line = line.split()
            level_name = split_line[3]

            if level_name in ['ERROR', 'CRITICAL']:
                if not error_block_flag:
                    error_block_flag = True
                    lines = []
                lines.append(line.replace('\n', ''))
            else:
                if error_block_flag:
                    error_block_flag = False
                    result.append(lines)
                line = line.replace('\n', '')
                line = [line]
                result.append(line)
        return result


def parse_line(line):
    '''

    :param line:
    :return:
    '''
    if len(line) == 1:
        first_line = line[0]
        split_line = first_line.split()
        # get msecs from logs line
        split_time = split_line[1].split('.')
        try:
            msecs = split_time[1]
        except IndexError:
            msecs = 0

        # get asctime from logs line
        asctime = ' '.join([split_line[0], split_time[0]])
        # get process id from logs line
        process = split_line[2]
        # get levelname from logs line
        levelname = split_line[3]
        # get name from logs file
        name = split_line[4]
        # cut line to easy parse
        user_identitys = re.findall(r'\[(.*?)\]', first_line)
        # get request id
        request_id = user_identitys[0].split()[0]
        # get ip address
        instance = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", first_line)
        if user_identitys == ['-']:
            message = ' '.join(split_line[6:])
        else:
            message = ' '.join(split_line[10:])
        return LogEntry(msecs=msecs, asctime=asctime, process=process, name=name, levelname=levelname,
                        user_identitys=user_identitys, request_id=request_id, instance=instance, message=message)
    else:
        first_line = line[0]
        split_line = first_line.split()
        split_time = split_line[1].split('.')
        msecs = split_time[1]
        asctime = ' '.join([split_line[0], split_time[0]])
        process = split_line[2]
        name = split_line[4]
        levelname = split_line[3]
        user_identitys = re.findall(r'\[(.*?)\]', first_line)
        request_id = user_identitys[0].split()[0]
        instance = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", first_line)
        message = '\n'.join(line[1:])
        return LogEntry(msecs=msecs, asctime=asctime, process=process, name=name, levelname=levelname,
                        user_identitys=user_identitys, request_id=request_id, instance=instance, message=message)
