#!/usr/bin/python3

import os
import re


def get_path(path):
    """
    Collect absolute path of all files in directory with logs

    :param path: path to directory with files
    :return: absolute path name
    """
    os.chdir(path)

    for root, dirs, files in os.walk(path, topdown=True):
        for name in files:
            yield name
        for name in dirs:
            yield name


def get_nova_logs_path(path):
    """
    Collect absolute path of all logs files in directory with logs

    :param path: path to directory with  files
    :return: absolute path name file with logs
    """

    regexp = re.compile(r'(^(?:(?!\bgz\b).)*$)')
    for root, dirs, files in os.walk(path):
        for file in files:
            if regexp.search(file):
                yield file
