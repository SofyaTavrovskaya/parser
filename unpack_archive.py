#!/usr/bin/python3

import gzip
import os
import bz2


def unpack_gz(path_to_file):
    """
    Unpack .gz archives

    :param path_to_file:
    :return: .log file
    """
    gz_file = gzip.open(path_to_file).read()
    log_file_path = os.path.splitext(path_to_file)[0]
    with open(log_file_path, 'wb') as output:
        output.write(gz_file)


def unpack_bz2(path_to_file):
    """
    Unpack .bz2 archives

    :param path_to_file:
    :return: .gz archive
    """
    bz2_file = bz2.BZ2File(path_to_file).read()
    gz_file_path = os.path.splitext(path_to_file)[0]
    with open(gz_file_path, 'wb') as output:
        output.write(bz2_file)

