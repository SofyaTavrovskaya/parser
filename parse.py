#!/usr/bin/python3


import re
from log_entry import LogEntry
from loger import LOG


def parse_file(path_to_file):
    """
    Read all lines in open file of logs and create list of all logs

    :param path_to_file: absolute path to logs file
    :return:list of logs lines
    """
    result = []
    lines = []
    with open(path_to_file, "rt") as fo:
        error_block_flag = False

        for line in fo.readlines():
            split_line = line.split()
            try:
                level_name = split_line[3]
            except IndexError:
                LOG.error("Error: list of index out of range. Line: %s" % line)
                level_name = ''

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
    """
    Parse line of log

    :param line: item from list with logs
    :return: object with parsed log
    """
    if len(line) == 1:
        first_line = line[0]
        split_line = first_line.split()
        # get msecs from logs line
        try:
            split_time = split_line[1].split('.')
        except IndexError:
            LOG.error("Error: list of index out of range. Line: %s" % line)
            split_time = 0
        try:
            msecs = split_time[1]
        except IndexError:
            LOG.error("Error: list of index out of range. Line: %s" % line)
            msecs = 0
        # get asctime from logs line
        asctime = ' '.join([split_line[0], split_time[0]])
        # get process id from logs line
        try:
            process = split_line[2]
        except IndexError:
            LOG.error("Error: list of index out of range. Line: %s" % line)
            process = 0
        # get levelname from logs line
        try:
            levelname = split_line[3]
        except IndexError:
            LOG.error("Error: list of index out of range. Line: %s" % line)
            levelname = ''
        # get name from logs file
        try:
            name = split_line[4]
        except IndexError:
            LOG.error("Error: list of index out of range. Line: %s" % line)
            name = ''
        # cut line to easy parse
        user_identitys = re.findall(r'\[(.*?)\]', first_line)
        # get request id
        try:
            request_id = user_identitys[0].split()[0]
        except IndexError:
            LOG.error("Error: list of index out of range. Line: %s" % line)
            request_id = '-'
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
        try:
            process = split_line[2]
        except IndexError:
            LOG.error("Error: list of index out of range. Line: %s" % line)
            process = 0
        try:
            name = split_line[4]
        except IndexError:
            LOG.error("Error: list of index out of range. Line: %s" % line)
            name = ''
        try:
            levelname = split_line[3]
        except IndexError:
            LOG.error("Error: list of index out of range. Line: %s" % line)
            levelname = ''
        user_identitys = re.findall(r'\[(.*?)\]', first_line)
        try:
            request_id = user_identitys[0].split()[0]
        except IndexError:
            LOG.error("Error: list of index out of range. Line: %s" % line)
            request_id = '-'
        instance = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", first_line)
        message = '\n'.join(line[1:])
        return LogEntry(msecs=msecs, asctime=asctime, process=process, name=name, levelname=levelname,
                        user_identitys=user_identitys, request_id=request_id, instance=instance, message=message)
