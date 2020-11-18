import unittest

from image import read, write, Image


class TestSmoothImage(unittest.TestCase):

    def test_smooth(self):
        # Smooth entire image
        img = read('./test_data/test_smooth.png')
        org = Image(img.array.copy())
        img.filter.blur.gaussian(kernel_size=(99, 99), sigma_x=0)
        write('./test_data/test_smoothed.png', img)
        self.assertGreater(org.metrics.mse(img), 0)

    def test_region(self):
        # Smooth region
        img = read("./test_data/test_smooth.png")
        org = Image(img.array.copy())
        w, h, = img.width, img.height
        region = (int(w/2 - w/4), int(h/2 - h/4)), (int(w/2 + w/4), int(h/2 + h/4))
        img.filter.blur.gaussian(kernel_size=(99, 99), sigma_x=0, region=region)
        write('./test_data/test_smoothed_region.png', img)
        self.assertGreater(org.metrics.mse(img), 0)


if __name__ == '__main__':
    unittest.main()
