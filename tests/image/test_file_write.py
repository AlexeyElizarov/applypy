import os
import unittest

import cv2
import numpy

from helpers import TestFileHelper
from image import read, write


class WriteImage(unittest.TestCase, TestFileHelper):

    def test_valid_path(self):
        # Test writing a valid image
        image = read(self._test_file('test_read_image.jpg'))
        with self._temp_dir() as temp_dir:
            path = os.path.join(temp_dir, 'test_write_image.png')
            write(path, image)
            self.assertTrue(os.path.exists(path))

            new_image = read(path)
            numpy.testing.assert_array_equal(new_image, image)

    def test_invalid_path(self):
        # Test writing a valid image
        image = read(self._test_file('test_read_image.jpg'))
        with self._temp_dir() as temp_dir:
            path = os.path.join(temp_dir, 'not_exist_dir', 'test_write_image.png')

            self.assertFalse(os.path.exists(os.path.dirname(path)))

            write(path, image)
            self.assertTrue(os.path.exists(path))

            new_image = read(path)
            numpy.testing.assert_array_equal(new_image, image)

    def test_invalid_ext(self):
        # Test writing a valid image with improper file extension
        image = read(self._test_file('test_read_image.jpg'))
        with self._temp_dir() as temp_dir:
            path = os.path.join(temp_dir, 'foo.xxx')
            with self.assertRaises(cv2.error):
                write(path, image)


if __name__ == '__main__':
    unittest.main()
