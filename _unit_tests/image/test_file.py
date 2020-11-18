import unittest

import cv2

from image import read, write


class ReadImage(unittest.TestCase):

    def test_valid_image(self):
        # Test a valid image path
        self.assertTrue(read('./test_data/test_read_image.jpg').size > 0)

    def test_invalid_image(self):
        # Test an invalid image path
        with self.assertRaises(FileNotFoundError):
            read('foo')


class WriteImage(unittest.TestCase):

    img = read('./test_data/test_read_image.jpg')

    def test_valid_image(self):
        # Test writing a valid image
        self.assertTrue(write('./test_data/test_write_image.jpg', self.img))

    def test_cv2_error(self):
        # Test writing a valid image with improper file extension
        with self.assertRaises(cv2.error):
            write('./test_data/foo.xxx', self.img)


if __name__ == '__main__':
    unittest.main()