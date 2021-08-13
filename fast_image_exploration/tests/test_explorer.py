from unittest import TestCase
import os
from pathlib import Path
from fast_image_exploration import DatasetExplorer


class TestExplorer(TestCase):

    def test_file_construction(self):
        test_path = Path(__file__).parent
        cfg = {
            "input_file": os.path.join(test_path, "classification/data.txt")
        }
        explorer = DatasetExplorer(cfg)
        self.assertEqual(explorer._count_images(), 20)
        self.assertEqual(explorer.case, "classification")
