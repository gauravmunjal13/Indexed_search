import sys
import os
import src.indexingEngine.indexing_module as indexing_module
import src.utils.utils as utils
import datetime
import argparse
'''
This is the main file for the Indexed Search project.
'''


def parse_command_line_args():

    # argparse is the recommended command-line parsing module in the Python standard library.
    parser = argparse.ArgumentParser()

    # Creating a mutually exclusive group for searching and indexing
    group = parser.add_mutually_exclusive_group()

    # '-' is for short option, '--' for long option
    # the value is stored in a variable with the name same as the long option
    group.add_argument("-i", "--index", help="location to index")
    group.add_argument("-s", "--search", help="query to search")

    # add input optional command line arguments for clean and de-indexing
    """ clean is a flag. This means that, if the option is specified,
    assign the value True to clean. Not specifying it implies False."""
    group.add_argument("--clean", help="clean indexing", action="store_true")
    group.add_argument("-d", "--deindex", help="location to de-index")

    # parse the arguments
    args = parser.parse_args()

    return args


def main():

    # call function to parse command line arguments
    args = parse_command_line_args()

    # take action depending upon user input
    if args.index or args.deindex:

        # user want to index (currently support for adding index only)
        print("Index : " + args.index)

        # check whether the given directory is present or not
        if not os.path.isdir(args.index):
            # utils.Log.log("The directory you gave does not exist. Exiting...")
            sys.exit("The directory you gave does not exist. Exiting...")

        # get indexing module object
        indexer = indexing_module.IndexModule()

        # record start time
        start_time = datetime.datetime.now()

        if args.index:
            # index the directory
            indexer.index(args.index)
        else:
            # de-index the directory
            indexer.index(args.deindex,1)

        # record end time
        end_time = datetime.datetime.now()

        # print indexing time to the user
        print("Indexing time := " + str(end_time - start_time))

    elif args.clean:
        # get indexing module object
        utils.Log.log("cleaning the indexed data")
        # indexer = indexing_module.IndexModule()
        indexing_module.IndexModule.clean()

    elif args.search:

        # user wants to search a query
        print("Search : " + args.search)

        # get indexing module object
        indexer = indexing_module.IndexModule()

        # record start time
        start_time = datetime.datetime.now()

        # split query into words
        words = args.search.split()

        # TODO Merge the results
        # for word in words:
        result = indexer.search(words[0])

        # record end time
        end_time = datetime.datetime.now()

        # print indexing time to the user
        print("Searching time := " + str(end_time - start_time))

        utils.Log.log("Result := " + str(result))

    else:

        # TODO show usage here
        print("No option specified")

if __name__ == '__main__':
    main()
