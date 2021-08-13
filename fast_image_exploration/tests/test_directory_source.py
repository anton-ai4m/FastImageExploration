import os
import numpy as np
from pathlib import Path
from unittest import TestCase
from fast_image_exploration import DirectoryDataSource


class TestDirectoryDataSource(TestCase):

    def test_mnist_construction(self):
        test_path = Path(__file__).parent
        file = 'classification/data.txt'
        source = DirectoryDataSource(os.path.join(test_path, file), "classification")
        self.assertEqual(len(source.list_images()), 20)

    def test_mnist_image_load(self):
        test_path = Path(__file__).parent
        file = 'classification/data.txt'
        source = DirectoryDataSource(os.path.join(test_path, file), "classification")
        shape = source.get_image(source.list_images()[0]).shape
        self.assertEqual(shape, (28, 28))

    def test_mnist_label_load(self):
        test_path = Path(__file__).parent
        file = 'classification/data.txt'
        source = DirectoryDataSource(os.path.join(test_path, file), "classification")
        label = source.get_label(source.list_images()[8])
        self.assertEqual(label, '4')

    def test_segmentation_construction(self):
        test_path = Path(__file__).parent
        file = 'segmentation/data.txt'
        source = DirectoryDataSource(os.path.join(test_path, file), "segmentation")
        self.assertEqual(len(source.list_images()), 10)

    def test_segmentation_image_load(self):
        test_path = Path(__file__).parent
        file = 'segmentation/data.txt'
        source = DirectoryDataSource(os.path.join(test_path, file), "segmentation")
        shape = source.get_image(source.list_images()[0]).shape
        self.assertEqual(shape, (256, 256, 4))

    def test_segmentation_label_load(self):
        test_path = Path(__file__).parent
        file = 'segmentation/data.txt'
        source = DirectoryDataSource(os.path.join(test_path, file), "segmentation")
        label = source.get_label(source.list_images()[8])
        self.assertIsInstance(label, np.ndarray)
        self.assertEqual(label.shape, (256, 256))

    def test_detection_construction(self):
        test_path = Path(__file__).parent
        file = 'detection/data.txt'
        source = DirectoryDataSource(os.path.join(test_path, file), "detection")
        self.assertEqual(len(source.list_images()), 112)

    def test_detection_image_load(self):
        test_path = Path(__file__).parent
        file = 'detection/data.txt'
        source = DirectoryDataSource(os.path.join(test_path, file), "detection")
        image = source.get_image(source.list_images()[86])
        self.assertEqual(image.shape, (224, 224, 3))

    def test_detection_label_load(self):
        test_path = Path(__file__).parent
        file = 'detection/data.txt'
        source = DirectoryDataSource(os.path.join(test_path, file), "detection")
        label = source.get_label(source.list_images()[86])
        self.assertIsInstance(label, np.ndarray)
        self.assertEqual(label.shape, (1, 4))
