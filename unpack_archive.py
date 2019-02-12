#!/usr/bin/python3

import gzip
import os
import bz2
import pdb


def unpack_gz(path_to_file):
    """
    Unpack .gz archives

    :param path_to_file:
    :return: .log archive
    """
    gz_file = gzip.open(path_to_file).read()
    log_file_path = os.path.splitext(path_to_file)[0]
    print(log_file_path)
    with open(log_file_path, 'wb') as output:
        output.write(gz_file)


def unpack_bz2(path_to_file):
    """
    Unpack .bz2 archives

    :param path_to_file:
    :return: .gz file
    """
    bz2_file = bz2.BZ2File(path_to_file).read()
    gz_file_path = os.path.splitext(path_to_file)[0]
    print(gz_file_path)
    with open(gz_file_path, 'wb') as output:
        output.write(bz2_file)


# def unpack_archives(path_to_files):
#     for file in path_to_files:
#         if file.endswith('.bz2'):
#             LOG.info("Found .bz2 file %s" % file)
#             file = unpack_bz2(file)
#             yield os.path(file)
#
#     for file in path_to_files:
#         if file.endswith('.gz'):
#             LOG.info("Found .gz file %s" % file)
#             file = unpack_gz(file)
#             yield os.path(file)

