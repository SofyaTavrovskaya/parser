#!/usr/bin/python3

import logging
import sys
from gather_files_name import get_path, get_nova_logs_path
from unpack_archive import unpack_gz
from unpack_archive import unpack_bz2
from parse import parse_file, parse_line


logging.basicConfig(filename='parser.log', level=logging.DEBUG)
LOG = logging.getLogger("Logs parser")


def main():
    """

    Gets from console absolute path to directory with logs and
    return dictionary with parsed logs as objects

    :return:dictionary

    """
    if len(sys.argv) < 2:
        print("Enter absolute path to directory with logs")
    else:
        log_files = get_path(sys.argv[1])
        for file in log_files:
            if file.endswith('.bz2'):
                unpack_bz2(file)
                log_files = get_path(sys.argv[1])
                LOG.info("Unpack .bz2 file %s" % file)

        for path in log_files:
            if path.endswith('.gz'):
                unpack_gz(path)
                LOG.info("Unpack .gz file %s" % path)

        log_files = get_nova_logs_path(sys.argv[1])

        dict = {}
        log_message = []

        for log_file in log_files:
            lines_list = parse_file(log_file)
            LOG.info("Parse file %s" % log_file)
            for item in lines_list:
                log = parse_line(item)
                log_message.append(log)
        dict[log_file] = log_message
        print(dict)


if __name__ == '__main__':
    main()
