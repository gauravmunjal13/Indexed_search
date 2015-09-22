__author__ = 'Arjun H'

'''
This is the main file for the Indexed Search project.
'''

# Imports
import os

if __name__ == '__main__':

    print("Welcome to indexed search.\n")

    # Take input from user
    str = input('Enter a string to search : ')
    location = input('Enter a folder to search this string : ')

    # TODO Validate input

    # Checking if user entered a valid directory
    if os.path.isdir(location):
        # Passing the inputs to the indexing engine
        pass
    else:
        print("The directory you gave does not exist. Exiting...")