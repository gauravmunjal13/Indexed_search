import unittest
import src.storage.fileManager

__author__ = 'Arjun H'


class StorageTests(unittest.TestCase):

    def test_saveToFile(self):
        data = "abcdef"
        src.storage.fileManager.FileManager.save(self, "", data)
        pass

    def test_retrieveFromFile(self):
        self.assertTrue(False)
        pass


if __name__ == '__main__':
    unittest.main()