import sys
import os
import fnmatch
import inspect

'''
This modules implements various utility like
 - Logging
 - Various string functions
'''


class Log:

    @staticmethod
    def get_hdr():
        hdr = ""
        hdr += os.path.basename(inspect.stack()[2][1])
        hdr += ":" + str(inspect.stack()[2][2])
        hdr += "::" + str(inspect.stack()[2][3]) + "():"
        return hdr

    @staticmethod
    def enter(arg=""):
        print(Log.get_hdr() + " Enter " + arg)

    @staticmethod
    def exit(arg=""):
        print(Log.get_hdr() + "Exit " + arg)

    @staticmethod
    def log(arg):
        print(Log.get_hdr() + " " + arg)


class StringHelperFunctions:

    @staticmethod
    def stem():
        # TODO Implement porter stemmer or any other algorithm for stemming
        pass
    pass


def find_files(directory, pattern='*'):
    """ to find files recursively in a directory """

    if not os.path.exists(directory):
        raise ValueError("Directory not found {}".format(directory))

    matches = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            full_path = os.path.join(root, filename)
            if fnmatch.filter([full_path], pattern):
                matches.append(os.path.join(root, filename))
    return matches



