import unittest

from helpers import TestFileHelper
from image import read


class ImageProperties(unittest.TestCase, TestFileHelper):

    def test_width(self):
        img1 = read(self._test_file('test_image_0.jpg'))
        self.assertEqual(img1.width, 1511)

    def test_height(self):
        img1 = read(self._test_file('test_image_0.jpg'))
        self.assertEqual(img1.height, 2015)

    def test_channels(self):
        img1 = read(self._test_file('test_image_0.jpg'))
        img2 = read(self._test_file('test_greyscale.png'))
        self.assertEqual(img1.channels, 3)
        self.assertEqual(img2.channels, 3)

    def test_size(self):
        img3 = read(self._test_file('test_rgb.png'))
        self.assertEqual(img3.size, img3.width * img3.height * img3.channels)


if __name__ == '__main__':
    unittest.main()
