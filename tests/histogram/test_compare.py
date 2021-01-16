import unittest

import image
from helpers import TestFileHelper
from histogram import Histogram


class TestHistogramCompare(unittest.TestCase, TestFileHelper):

    def test_identical_histograms(self):
        path = self._test_file('test_rgb.png')
        img1 = image.read(path)
        img2 = image.read(path)
        hist1 = Histogram(image=img1, channels='L')
        hist2 = Histogram(image=img2, channels='L')
        dist = hist1.compare(hist2)
        self.assertEqual(dist, 0)

    def test_different_histograms(self):
        path1 = self._test_file('test_red.png')
        path2 = self._test_file('test_green.png')
        img1 = image.read(path1)
        img2 = image.read(path2)
        hist1 = Histogram(image=img1, channels='L')
        hist2 = Histogram(image=img2, channels='L')
        dist = hist1.compare(hist2)
        self.assertGreater(dist, 0)


if __name__ == '__main__':
    unittest.main()
