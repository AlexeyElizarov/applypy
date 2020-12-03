import unittest
from os import getcwd
from os.path import exists, dirname, join, abspath, relpath

import cv2
import numpy

from helpers import TestFileHelper
from image import read, write


class WriteImage(unittest.TestCase, TestFileHelper):

    def test_absolute_path(self):
        # Test writing a valid image
        # image = read(self._test_file('test_read_image.jpg'))
        image = read(self._test_file('test_write_image.jpg'))
        with self._temp_dir() as temp_dir:
            path = join(temp_dir, 'test_write_image.jpg')
            path = abspath(path)
            write(path, image)
            self.assertTrue(exists(path))

            new_image = read(path)
            numpy.testing.assert_array_equal(new_image, image)

    def test_relative_path(self):
        # Test writing a valid image
        # image = read(self._test_file('test_read_image.jpg'))
        image = read(self._test_file('test_write_image.jpg'))
        with self._temp_dir() as temp_dir:
            path = join(temp_dir, 'test_write_image.jpg')
            path = relpath(path, getcwd())
            write(path, image)
            self.assertTrue(exists(path))

            new_image = read(path)
            numpy.testing.assert_array_equal(new_image, image)

    def test_invalid_path(self):
        # Test writing a valid image
        # image = read(self._test_file('test_read_image.jpg'))
        image = read(self._test_file('test_write_image.jpg'))
        with self._temp_dir() as temp_dir:
            path = join(temp_dir, 'not_exist_dir', 'test_write_image.jpg')

            self.assertFalse(exists(dirname(path)))

            write(path, image)
            self.assertTrue(exists(path))

            new_image = read(path)
            numpy.testing.assert_array_equal(new_image, image)

    def test_invalid_ext(self):
        # Test writing a valid image with improper file extension
        # image = read(self._test_file('test_read_image.jpg'))
        image = read(self._test_file('test_write_image.jpg'))
        with self._temp_dir() as temp_dir:
            path = join(temp_dir, 'foo.xxx')
            with self.assertRaises(cv2.error):
                write(path, image)


if __name__ == '__main__':
    unittest.main()
