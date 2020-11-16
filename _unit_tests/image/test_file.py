import unittest

import cv2

from image import read, write


class TestImageIO(unittest.TestCase):

    def test_read_image(self):
        # Test reading images
        self.assertTrue(read('./test_data/test_read_image.jpg').size > 0)
        with self.assertRaises(FileNotFoundError):
            read('foo')

    def test_write_image(self):
        # Test writing images
        img = read('./test_data/test_read_image.jpg')
        self.assertTrue(write('./test_data/test_write_image.jpg', img))
        with self.assertRaises(cv2.error):
            write('foo', img)


if __name__ == '__main__':
    unittest.main()