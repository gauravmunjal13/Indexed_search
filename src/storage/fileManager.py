import os
import pickle

__author__ = 'Arjun H'

'''
This is the File Manager file, which takes care of storage in files.
'''

class FileManager():

    def save(self, location, indexData):

        # TODO Check if an index is already associated with this location

        # open the file
        print("Saving the file to := " + os.getcwd() + '\\.testing')
        pickle._dump(indexData, open("save.p", "wb"))
        pass

    def retrieve(self, location):
        pass

    pass