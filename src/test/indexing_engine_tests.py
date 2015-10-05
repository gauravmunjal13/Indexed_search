import unittest
from src.indexingEngine import indexing_module

_path_prefix = "C:/Users/Arjun H/Documents/Origins/Indexed_search/src/storage/data/test/"


class IndexingEngineTests(unittest.TestCase):

    def test_empty_directory(self):
        """
        indexing engine should return empty result when there are no files in the folder
        """

        # create indexer object
        indexer = indexing_module.IndexModule()

        # index the location (storage/data/test/empty_directory)
        indexer.index(_path_prefix + 'empty_directory')

        # search for few words and check that the result is empty
        result = indexer.search("")
        print(result)
        self.assertTrue(result == {})

        result = indexer.search("hello")
        self.assertTrue(result == {})

        result = indexer.search("world")
        self.assertTrue(result == {})

    def test_word_not_found_in_file(self):
        """
        indexing engine should return empty result when the word is not found in a single file
        """

        # create indexer object
        indexer = indexing_module.IndexModule()

        # index the location (storage/data/test/word_not_found)
        indexer.index(_path_prefix + 'word_not_found')

        # search for few words and check that the result is empty
        result = indexer.search("hello")
        print(result)
        self.assertTrue(result == {})

        result = indexer.search("world")
        self.assertTrue(result == {})

    def test_word_found_in_file(self):
        """
        indexing engine should return correct result when the word is found in a file
        """

        # create indexer object
        indexer = indexing_module.IndexModule()

        # index the location (storage/data/test/empty_directory)
        indexer.index(_path_prefix + 'word_not_found')

        # search for few words and check that the result is empty
        result = indexer.search("unit")
        self.assertTrue(result != [])

        result = indexer.search("index")
        self.assertTrue(result != [])
        print(result)

    def test_word_positions_in_file(self):
        """
        indexing engine should return correct position listing of a word in a file
        """
        pass

    def test_add_word_in_file(self):
        """
        indexing engine should update the index when a word is deleted from a file
        """
        pass

    def test_delete_word_in_file(self):
        pass

    def test_modify_word_in_file(self):
        pass

    def test_add_file_in_directory(self):
        pass

    def test_delete_file_in_directory(self):
        pass

    def test_rename_file_in_directory(self):
        pass

if __name__ == '__main__':
    unittest.main()
