import unittest

import cv2

from image import read


class ReadImage(unittest.TestCase):

    def test_valid_image(self):
        # Test a valid image path
        self.assertTrue(read('./test_data/test_read_image.jpg').size > 0)

    def test_invalid_image(self):
        # Test an invalid image path
        with self.assertRaises(FileNotFoundError):
            read('foo')




if __name__ == '__main__':
    unittest.main()