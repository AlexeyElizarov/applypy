import unittest
from helpers import TestFileHelper
from image import read


class RegionOfInterest(unittest.TestCase, TestFileHelper):

    def test_roi(self):
        x, y, w, h = 25, 15, 50, 25
        img = read(self._test_file("test_rgb.png"))
        roi = img.set_roi(x, y, w, h)
        self.assertEqual((roi.width, roi.height), (w, h))

    def test_incomplete_roi(self):
        x, y = 25, 15
        img = read(self._test_file("test_rgb.png"))
        roi = img.set_roi(25, 15)
        self.assertEqual((roi.width, roi.height), (img.width - x, img.height - y))


if __name__ == '__main__':
    unittest.main()
