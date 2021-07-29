import os
from pathlib import Path
from unittest import TestCase
from fast_image_exploration import DirectoryDataSource

class TestDirectoryDataSource(TestCase):

    def test_directory_construction(self):
        test_path = Path(__file__).parent
        directory = 'mnist/mnist_png/'
        source = DirectoryDataSource(os.path.join(test_path, directory))
        self.assertEqual(len(source.list_images()), 20)

    def test_file_construction(self):
        test_path = Path(__file__).parent
        file = 'mnist/data.txt'
        source = DirectoryDataSource(os.path.join(test_path, file))
        self.assertEqual(len(source.list_images()), 20)