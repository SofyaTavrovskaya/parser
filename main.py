#!/usr/bin/python3

from loger import LOG
import sys
from gather_files_name import get_path, get_nova_logs_path
from unpack_archive import unpack_gz
from unpack_archive import unpack_bz2
from parse import parse_file, parse_line
import pdb


def main():
    """

    Gets from console absolute path to directory with logs and
    return dictionary with parsed logs as objects

    :return:dictionary

    """
    if len(sys.argv) < 2:
        print("Enter absolute path to directory with logs")
    else:
        for file in get_path(sys.argv[1]):
            if file.endswith('.bz2'):
                unpack_bz2(file)
                LOG.info("Unpack .bz2 file %s" % file)

        for path in get_path(sys.argv[1]):
            if path.endswith('.gz'):
                unpack_gz(path)
                LOG.info("Unpack .gz file %s" % path)

        dict = {}
        log_message = []

        for log_file in get_nova_logs_path(sys.argv[1]):
            lines_list = parse_file(log_file)
            LOG.info("Parse file %s" % log_file)
            for item in lines_list:
                log = parse_line(item)
                log_message.append(log)
        dict[log_file] = log_message
        print(dict)


if __name__ == '__main__':
    main()
