from unittest import TestCase
from fast_image_exploration import DirectoryDataSource

class TestDirectoryDataSource(TestCase):

    def test_directory_construction(self):
        directory = 'mnist/mnist_png/'
        source = DirectoryDataSource(directory)
        self.assertEqual(len(source.list_images()), 20)

    def test_file_construction(self):
        file = 'mnist/data.txt'
        source = DirectoryDataSource(file)
        self.assertEqual(len(source.list_images()), 20)