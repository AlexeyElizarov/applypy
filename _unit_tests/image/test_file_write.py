import unittest
from os.path import exists, dirname
from shutil import rmtree

import cv2

from image import read, write


class WriteImage(unittest.TestCase):

    img = read(r'.\test_data\test_read_image.jpg')

    def test_absolute_path(self):
        # Test writing a valid image
        path = r'C:\test\test_write_image.jpg'
        write(path, self.img)
        self.assertTrue(exists(path))

    def test_relative_path(self):
        # Test writing a valid image
        path = r'.\test_data\test_write_image.jpg'
        write(path, self.img)
        self.assertTrue(exists(path))

    def test_invalid_path(self):
        # Test writing a valid image
        path = r'C:\test2\test_write_image.jpg'

        if exists(dirname(path)):
            rmtree(dirname(path))

        write(path, self.img)
        self.assertTrue(exists(path))

    def test_invalid_ext(self):
        # Test writing a valid image with improper file extension
        path = r'.\test_data\foo.xxx'
        with self.assertRaises(cv2.error):
            write(path, self.img)


if __name__ == '__main__':
    unittest.main()
