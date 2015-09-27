import os
import pickle
import src.utils.utils as utils
'''
This is the File Manager file, which takes care of storage in files.
'''


class FileManager:

    @staticmethod
    def save(location, file_name, permission, indexed_data):

        # TODO Check if an index is already associated with this location
        pickle.dump(indexed_data, open(file_name, permission))
        return True

    @staticmethod
    def retrieve(location, file_name, permission):
        try:
            f = open(file_name, permission)
            return pickle.load(f)
        except FileNotFoundError:
            utils.Log.log("File not found : " + file_name)
            pass
        return {}

    pass