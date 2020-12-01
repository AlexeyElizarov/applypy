import unittest
from os.path import join

from helpers import TestFileHelper
from image import read, write


class TestSmoothImage(unittest.TestCase, TestFileHelper):

    def test_smooth(self):
        # Smooth entire image
        img = read(self._test_file('test_smooth.png'))
        smoothed = img.filter.blur.gaussian(kernel_size=(99, 99), sigma_x=0)
        with self._temp_dir() as temp_dir:
            path = join(temp_dir, 'test_smoothed.png')
            write(path, smoothed)
        self.assertGreater(img.metrics.mse(smoothed), 0)

    def test_region(self):
        # Smooth region
        img = read(self._test_file('test_smooth.png'))
        w, h, = img.width, img.height
        region = (int(w / 2 - w / 4), int(h / 2 - h / 4)), (int(w / 2 + w / 4), int(h / 2 + h / 4))
        smoothed = img.filter.blur.gaussian(kernel_size=(99, 99), sigma_x=0, region=region)
        with self._temp_dir() as temp_dir:
            path = join(temp_dir, 'test_smoothed_region.png')
            write(path, smoothed)
        self.assertGreater(img.metrics.mse(smoothed), 0)


if __name__ == '__main__':
    unittest.main()
