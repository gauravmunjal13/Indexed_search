import os
import pickle
import src.utils.utils as utils
'''
This is the File Manager file, which takes care of storage in files.
'''


class FileManager:

    @staticmethod
    def save(inverted_index, file_mapping):
        utils.Log.enter()
        try:
            with open('iids.pickle', 'wb') as f:
                utils.Log.log("Opening iids.pickle file to save data")
                pickle.dump(inverted_index, f)
        except IOError:
            utils.Log.log("Data not saved yet")
        try:
            with open('fmap.pickle', 'wb') as f:
                utils.Log.log("Opening fmap.pickle file to save data")
                pickle.dump(file_mapping, f)
        except IOError:
            utils.Log.log("Data not saved yet")
        utils.Log.exit()
        return True

    @staticmethod
    def retrieve():
        utils.Log.enter()
        inverted_index = {}
        file_mapping = {}
        """ if file not found, no issues as empty dictionaries would be passed.
        for the first time they would be created while using save method """
        try:
            with open('iids.pickle','rb') as f:
                inverted_index = pickle.load(f)
        except FileNotFoundError:
            utils.Log.log("iids.pickle file not created yet")
        try:
            with open('fmap.pickle','rb') as f:
                file_mapping = pickle.load(f)
        except FileNotFoundError:
            utils.Log.log("fmap.pickle file not created yet")
        return inverted_index, file_mapping
    utils.Log.exit()