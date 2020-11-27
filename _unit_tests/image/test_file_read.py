import unittest

import cv2

from image import read


class ReadImage(unittest.TestCase):

    ref_size = 9133995

    def test_valid_path(self):
        # Test a valid image path
        self.assertTrue(read(r'.\test_data\test_read_image.jpg').size == self.ref_size)

    def test_invalid_path(self):
        # Test an invalid image path
        with self.assertRaises(FileNotFoundError):
            read('foo')

    def test_cyrillic_filename(self):
        # Test cyrillic filename
        self.assertTrue(read(r'.\test_data\изображение.jpg').size == self.ref_size)

    def test_cyrillic_path(self):
        # Test cyrillic filename
        self.assertTrue(read(r".\test_data\изображения\изображение.jpg").size == self.ref_size)


if __name__ == '__main__':
    unittest.main()