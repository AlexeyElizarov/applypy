import unittest

import image
from helpers import TestFileHelper
from numpy import array

class TestImageHistogram(unittest.TestCase, TestFileHelper):

    def test_green(self):

        ref_hist = [[0] for i in range(256)]
        ref_hist[255] = [100 * 100]
        ref_hist = array(ref_hist)

        path = self._test_file('test_image_create_green.png')
        img = image.read(path)
        hist = img.metrics.histogram('G')

        comparison = hist.array == ref_hist
        is_equal = comparison.all()
        self.assertTrue(is_equal)

    def test_red(self):

        ref_hist = [[0] for i in range(256)]
        ref_hist[255] = [100 * 100]
        ref_hist = array(ref_hist)

        path = self._test_file('test_image_create_red.png')
        img = image.read(path)
        hist = img.metrics.histogram(channels='R')

        comparison = hist.array == ref_hist
        is_equal = comparison.all()
        self.assertTrue(is_equal)

    def test_blue(self):

        ref_hist = [[0] for i in range(256)]
        ref_hist[255] = [100 * 100]
        ref_hist = array(ref_hist)

        path = self._test_file('test_image_create_blue.png')
        img = image.read(path)
        hist = img.metrics.histogram(channels='B')

        comparison = hist.array == ref_hist
        is_equal = comparison.all()
        self.assertTrue(is_equal)

    def test_luminosity(self):

        ref_hist = [[0] for i in range(256)]
        # Gray = 0.299*Red + 0.587*Green + 0.114*Blue
        ref_hist[int(round(0.299 * 255))] = [100 * 100]  # Red
        ref_hist[int(round(0.587 * 255))] = [100 * 100]  # Green
        ref_hist[int(round(0.114 * 255))] = [100 * 100]  # Blue
        ref_hist = array(ref_hist)

        path = self._test_file('test_image_create_rgb.png')
        img = image.read(path)
        hist = img.metrics.histogram(channels='L')

        comparison = hist.array == ref_hist
        is_equal = comparison.all()
        self.assertTrue(is_equal)

if __name__ == '__main__':
    unittest.main()
