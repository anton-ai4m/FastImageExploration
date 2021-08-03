import os
from pathlib import Path
from unittest import TestCase
from fast_image_exploration import DirectoryDataSource

class TestDirectoryDataSource(TestCase):

    def test_file_construction(self):
        test_path = Path(__file__).parent
        file = 'mnist/data.txt'
        source = DirectoryDataSource(os.path.join(test_path, file))
        self.assertEqual(len(source.list_images()), 20)

    def test_image_load(self):
        test_path = Path(__file__).parent
        file = 'mnist/data.txt'
        source = DirectoryDataSource(os.path.join(test_path, file))
        shape = source.get_image(source.list_images()[0]).shape
        self.assertEqual(shape, (28, 28))

    def test_label_load(self):
        test_path = Path(__file__).parent
        file = 'mnist/data.txt'
        source = DirectoryDataSource(os.path.join(test_path, file))
        label = source.get_label(source.list_images()[8])
        self.assertEqual(label, '4')