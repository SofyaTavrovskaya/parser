#!/usr/bin/python3

from loger import LOG
import sys
from gather_files_name import get_path, get_nova_logs_path
from unpack_archive import unpack_gz
from unpack_archive import unpack_bz2
from parse import parse_file, parse_line


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
                LOG.info("Found .bz2 file %s" % file)
                unpack_bz2(file)

        log_files = get_path(sys.argv[1])

        for path in log_files:
            if path.endswith('.gz'):
                LOG.info("Found .gz file %s" % path)
                unpack_gz(path)

        log_files = get_nova_logs_path(sys.argv[1])

        log_message = []

        for log_file in log_files:
            lines_list = parse_file(log_file)
            LOG.info("Parse file %s" % log_file)
            for item in lines_list:
                log = parse_line(item)
                log_message.append(log)
            print(log_message)


if __name__ == '__main__':
    main()
