import os
import src.utils.utils as utils
from src.storage.fileManager import FileManager as Storage


class IndexModule:
    """
    This class will contain the inverted index data structure and methods to manipulate it
    """
    def __init__(self, option=0):
        """
        initialize the inverted data structure and update it for the files in the folder name.
        """
        utils.Log.log("instantiate IndexModule class")
        # option: will decide whether index is used for folder/files or urls
        self.inverted_index = {}  # to contain the inverted index data structure
        self.file_mapping = {}    # to contain the mapping of document id of file with its path and metadata

        # Check is data is already present
        self.inverted_index, self.file_mapping = Storage.retrieve()

    def __del__(self):
        """
        this function is automatically called by python when the object of this class goes out of scope
        we save the files we need in this function.
        """
        utils.Log.log("delete the IndexModule class object")
        Storage.save(self.inverted_index, self.file_mapping)

    def index(self, location, option=0):
        """
        this function does the indexing of the directory
        :param location: the location to index / de-index
        :param option: 0 -> for index; 1 -> for de-index
        """
        utils.Log.enter()

        # find all the files in a directory and update the inverted index data structure
        # for any file if it has been updated in the directory.
        files = utils.find_files(location)  # files is a list of all the files in the directory
        for file in files:
            inode_number = os.stat(file).st_ino
            # index the file
            if option == 0:
                mod_time = os.stat(file).st_mtime
                if inode_number not in self.file_mapping:
                    self.file_mapping[inode_number] = [file, mod_time]
                    self.index_file(file, inode_number)
                else:
                    if self.file_mapping[inode_number][1] != mod_time:
                        self.file_mapping[inode_number][1] = mod_time
                        self.index_file(file, inode_number)
            # de-index the file
            elif option == 1:
                # check for the file in file_mapping
                if inode_number in self.file_mapping:
                    del self.file_mapping[inode_number]
                    self.de_index_file(file, inode_number)

        utils.Log.exit()

    def index_file(self, filename, ind_number):
        """
        :param filename: filename with absolute path
        :param ind_number: inode number of the file
        :return:
        """
        utils.Log.enter("Indexing file : " + filename)
        if not isinstance(filename, str):
            str(filename)

        # Opening file
        with open(filename, mode='r', encoding='utf-8') as file_descriptor:
            file_contents = file_descriptor.read()

            # local dictionary to be merge with global dictionary
            l_inverted_index = {}

            # positional reference for saving the relative positions in the inverted index
            pos = 0

            # file_id which is to be mapped with the filename along with its path and many other things
            file_id = ind_number

            # make the inverted index data structure
            for word in file_contents.split():
                if word not in l_inverted_index:
                    l_inverted_index[word] = [pos]
                else:
                    l_inverted_index[word].append(pos)
                pos += 1
            for key in l_inverted_index.keys():
                temp_dict = {}
                value = l_inverted_index[key]
                temp_dict[file_id] = value
                l_inverted_index[key] = temp_dict
            print(l_inverted_index)
            # update the local inverted index to the global inverted index
            self.update_index(l_inverted_index)
            utils.Log.exit("Updated index : " + str(self.inverted_index))

    def de_index_file(self, file, inumber):
        """
        de-index the file from the inverted index data structure
        :param file: file to de-index
        :param inumber: inode number of the file to be de-indexed
        :return: None
        """
        utils.Log.enter("De-indexing file : " + file)
        if not isinstance(file, str):
            str(file)

        with open(file, mode='r', encoding='utf-8') as file_descriptor:
            file_contents = file_descriptor.read()
            for word in file_contents.split():
                # this if statement will avoid if the word repeats in the file
                if inumber in self.inverted_index[word]:
                    del self.inverted_index[word][inumber]

        utils.Log.exit()

    def update_index(self, index):
        # key is the word here
        for key in index:
            # If word is present than update its dict otherwise add the new word
            if key in self.inverted_index:
                """ here, key is the word, index[key] is the dict
                (with file inode number as the key and posting list as the value)"""
                self.inverted_index[key].update(index[key])
            else:
                self.inverted_index[key] = index[key]

    def search(self, query):
        # query is treated as a single entity
        utils.Log.log("Query := " + str(query))
        ret_var = {}
        """ query is the word here, self.inverted_index[query] is the dict"""
        if query in self.inverted_index:
            for file_inode_number in self.inverted_index[query]:
                file_name = self.file_mapping[file_inode_number][0]
                # value of ret_var[file_name] is list
                ret_var[file_name] = self.inverted_index[query][file_inode_number]
        return ret_var
