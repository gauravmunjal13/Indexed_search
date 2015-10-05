import os
import src.indexingEngine.indexing_module as indexing_module
import src.utils.utils as utils

'''
This is the main file for the Indexed Search project.
'''


def is_input_valid(query, location):
    # Checking if user entered a valid directory
    if not os.path.isdir(location):
        utils.Log.log("The directory you gave does not exist. Exiting...")
        return False
    return True


if __name__ == '__main__':

    print("Welcome to indexed search.\n")

    # Take input from user
    query = input('Enter a string to search : ')
    location = input('Enter a folder to search this string : ')

    if not is_input_valid(query, location):
        exit(0)

    # Passing the inputs to the indexing engine
    indexer = indexing_module.IndexModule()
    indexer.index(location)

    result = indexer.search(query)
    utils.Log.log("Result := " + str(result))
    indexer.save()
