import unittest

from helpers import TestFileHelper
from image import read


class ReadImage(unittest.TestCase, TestFileHelper):
    ref_size = 9133995

    def test_valid_path(self):
        # Test a valid image path
        test_file_name = self._test_file('test_read_image.jpg')
        self.assertTrue(read(test_file_name).size == self.ref_size)

    def test_invalid_path(self):
        # Test an invalid image path
        test_file_name = self._test_file('foo.jpg')
        with self.assertRaises(FileNotFoundError):
            read(test_file_name)

    def test_cyrillic_filename(self):
        # Test cyrillic filename
        test_file_name = self._test_file('изображение.jpg')
        self.assertTrue(read(test_file_name).size == self.ref_size)

    def test_cyrillic_path(self):
        # Test cyrillic filename
        test_file_name = self._test_file('изображения', 'изображение.jpg')
        self.assertTrue(read(test_file_name).size == self.ref_size)


if __name__ == '__main__':
    unittest.main()
