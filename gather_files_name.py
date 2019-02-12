#!/usr/bin/python3

import os
import fnmatch


def get_path(path):
    '''

    :param path:
    :return:
    '''
    os.chdir(path)
    list = []
    for root, dirs, files in os.walk(path, topdown=True):
        for name in files:
            list.append(os.path.join(root, name))
        for name in dirs:
            list.append(os.path.join(root, name))
    return list


def get_nova_logs_path(path):
    '''

    :param path:
    :return:
    '''

    list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if fnmatch.fnmatch(file, '*.log.[0-9]'):
                list.append(os.path.join(root, file))
    return list

