import os
import weakref
import src.utils.utils as utils
from src.storage.fileManager import FileManager as storage


class IndexModule:
    """
    This class will contain the inverted index data structure and methods to manipulate it
    """
    def __init__(self, option=0):
        """
        initialize the inverted data structure and update it for the files in the folder name.
        """
        # option: will decide whether index is used for folder/files or urls
        self.inverted_index = {}  # to contain the inverted index data structure
        self.file_mapping = {}    # to contain the mapping of document id of file with its path and metadata

        def on_die():
            """
            will call on as __del__() alternative
            """
            utils.Log.enter()
            storage.save('', 'iids.pickle', 'wb', self.inverted_index)
            storage.save('', 'fmap.pickle', 'wb', self.file_mapping)
            #with open('iids.pickle', 'wb') as f:
            #    pickle.dump(self.inverted_index, f)
            #with open('fmap.pickle', 'rb') as f:
            #    pickle.dump(self.file_mapping, f)

        self._del_ref = weakref.ref(self, on_die)

    def index(self, location):
        """
        this function does the indexing of the directory
        """
        utils.Log.enter()

        # Check is data is already present
        self.inverted_index = storage.retrieve(location, 'iids.pickle', 'rb')
        self.file_mapping = storage.retrieve(location, 'fmap.pickle', 'rb')

        if self.inverted_index != {} and self.file_mapping != {}:
            utils.Log.log("Index data present")

        #with open('iids.pickle', 'rb') as f:
        #    self.inverted_index = pickle.load(f)
        #with open('fmap.pickle', 'rb') as f:
        #    self.file_mapping = pickle.load(f)
        #print(self.inverted_index)
        #print(self.file_mapping)

        # find all the files in a directory and update the inverted index data structure
        # for any file if it has been updated in the directory.
        files = utils.find_files(location)  # files is a list of all the files in the directory
        for file in files:
            inode_number = os.stat(file).st_ino
            mod_time = os.stat(file).st_mtime
            if file not in self.file_mapping:
                self.file_mapping[file] = [inode_number, mod_time, file]
                self.index_file(file, inode_number)
            else:
                if self.file_mapping[file][1] != mod_time:
                    self.file_mapping[file][1] = mod_time  # not sure whether change of file contents will change the inode number
                    self.index_file(file, inode_number)

        storage.save('', 'iids.pickle', 'wb', self.inverted_index)
        storage.save('', 'fmap.pickle', 'wb', self.file_mapping)
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
            # currently using 101 just for now
            file_id = os.path.basename(filename) #ind_number

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

            # update the local inverted index to the global inverted index
            self.update_index(l_inverted_index)
            #self.inverted_index.update(l_inverted_index)
        utils.Log.exit("Updated index : " + str(self.inverted_index))

    def index_stream(self, stream_object):
        """
        If a library function takes a filename, open it, read it and close it.
        Then one should use stream object instead of restricting to the file stream object.
        :param stream_object: stream object can be of file, ioString, ioByte, standard IO file,
        object of class with __enter__() & __exit__() functions.
        :return:
        """
        pass

    def update_index(self, index):
        for key in index:
            if key in self.inverted_index:
                file_listing = self.inverted_index[key]
                file_listing.update(index[key])
            else:
                self.inverted_index[key] = index[key]


    def search(self, query):
        utils.Log.enter("Query := " + str(query))
        return_list = []
        if query in self.inverted_index:
            return_list.append(self.inverted_index[query])
        return return_list
