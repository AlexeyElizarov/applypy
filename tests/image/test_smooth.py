import unittest

from helpers import TestFileHelper
from image import read


class TestSmoothImage(unittest.TestCase, TestFileHelper):

    def test_smooth(self):
        # Smooth entire image
        img = read(self._test_file('test_smooth.png'))
        smoothed = img.filter.blur.gaussian(kernel_size=(99, 99), sigma_x=0)
        self.assertAlmostEqual(img.metrics.mse(smoothed), 2326.74, delta=0.01)

    def test_region(self):
        # Smooth region
        img = read(self._test_file('test_smooth.png'))
        w, h, = img.width, img.height
        region = (int(w / 2 - w / 4), int(h / 2 - h / 4)), (int(w / 2 + w / 4), int(h / 2 + h / 4))
        smoothed = img.filter.blur.gaussian(kernel_size=(99, 99), sigma_x=0, region=region)
        self.assertAlmostEqual(img.metrics.mse(smoothed), 1215.21, delta=0.01)


if __name__ == '__main__':
    unittest.main()
