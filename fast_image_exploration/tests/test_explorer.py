from unittest import TestCase
from fast_image_exploration import DatasetExplorer

class TestExplorer(TestCase):

    def test_directory_construction(self):
        cfg = {
            "image_directory": "/mnist/mnist_png/"
        }
        explorer = DatasetExplorer(cfg)
        self.assertEquals(explorer._count_images(), 20)

    def test_file_construction(self):
        cfg = {
            "input_file": "/mnist/data.txt"
        }
        explorer = DatasetExplorer(cfg)
        self.assertEquals(explorer._count_images(), 20)