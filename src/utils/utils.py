import sys
import os
import fnmatch

'''
This modules implements various utility like
 - Logging
 - Various string functions
'''

    #(sys._getframe().f_back.f_code.co_name)
class Log:
    pass


class StringHelperFunctions:
    def stem(self):
        # TODO Implement porter stemmer or any other algorithm for stemming
        pass
    pass

def test_log():
    Log()

if __name__ == "__main__":
    test_log()

def find_files( directory, pattern='*'):
    ''' to find files recursively in a directory '''
    if not os.path.exists(directory):
        raise ValueError("Directory not found {}".format(directory))

    matches = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            full_path = os.path.join(root, filename)
            if fnmatch.filter([full_path], pattern):
                matches.append(os.path.join(root, filename))
    return matches


def get_function_name():
    return sys._getframe().f_back.f_code.co_name


def test_utils_module():
    print(get_function_name())

if __name__ == "__main__":
    test_utils_module()



