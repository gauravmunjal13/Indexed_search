import sys
import os
import src.indexingEngine.indexing_module as indexing_module
import src.utils.utils as utils
import datetime

'''
This is the main file for the Indexed Search project.
'''

if __name__ == '__main__':

    print("Welcome to indexed search.\n")

    # Take input from user
    query = input('Enter a string to search : ')
    directory = input('Enter a folder to search this string : ')

    # Check whether the given director is present or not
    if not os.path.isdir(directory):
        # utils.Log.log("The directory you gave does not exist. Exiting...")
        sys.exit("The directory you gave does not exist. Exiting...")

    # Create indexing module object
    indexer = indexing_module.IndexModule()

    # Record start time
    start_time = datetime.datetime.now()

    # Index the directory
    indexer.index(directory)

    # Record end time
    end_time = datetime.datetime.now()

    # Print indexing time to the user
    print("Indexing time := " + str(end_time - start_time))

    # split query into words
    words = query.split()

    # TODO Merge the results
    # for word in words:
    result = indexer.search(words[0])
    utils.Log.log("Result := " + str(result))

    # Save the indexing
    indexer.save()
