import unittest

from image import read, write, Image


class TestSmoothImage(unittest.TestCase):

    img = read('./test_data/test_smooth.png')

    def test_smooth(self):
        # Smooth entire image
        smoothed = self.img.filter.blur.gaussian(kernel_size=(99, 99), sigma_x=0)
        write('./test_data/test_smoothed.png', smoothed)
        self.assertGreater(self.img.metrics.mse(smoothed), 0)

    def test_region(self):
        # Smooth region
        w, h, = self.img.width, self.img.height
        region = (int(w/2 - w/4), int(h/2 - h/4)), (int(w/2 + w/4), int(h/2 + h/4))
        smoothed = self.img.filter.blur.gaussian(kernel_size=(99, 99), sigma_x=0, region=region)
        write('./test_data/test_smoothed_region.png', smoothed)
        self.assertGreater(self.img.metrics.mse(smoothed), 0)


if __name__ == '__main__':
    unittest.main()
