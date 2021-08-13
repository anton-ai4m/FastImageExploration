from unittest import TestCase

import fast_image_exploration


class TestMain(TestCase):
    def test_correct_output(self):
        output = fast_image_exploration.main()
        self.assertEquals(output, "Hello world")
