import sys
import os
import fnmatch
import inspect

'''
This modules implements various utility like
 - Logging
 - Various string functions
'''


def log_header(func):
    """
    decorator to add the log header to the function called
    :param func: func to be decorated
    :return: decorated function (header_to_log)
    """
    def header_to_log(*args, **kwargs):
        print("" + os.path.basename(inspect.stack()[1][1]) +
                              ":" + str(inspect.stack()[1][2]) +
                              "::" + str(inspect.stack()[1][3]) + "():", end=' ')
        func(*args, **kwargs)
    return header_to_log


class Log:

    @staticmethod
    @log_header
    def enter(arg=""):
        print(" [Enter] " + arg)

    @staticmethod
    @log_header
    def exit(arg=""):
        print(" [Exit] " + arg)

    @staticmethod
    @log_header
    def log(arg):
        print(" " + arg)


def find_files(directory, pattern='*'):
    """ to find files recursively in a directory """

    if not os.path.exists(directory):
        raise ValueError("Directory not found {}".format(directory))

    matches = []
    for root, dir_names, file_names in os.walk(directory):
        for filename in file_names:
            full_path = os.path.join(root, filename)
            if fnmatch.filter([full_path], pattern):
                matches.append(os.path.join(root, filename))
    return matches
