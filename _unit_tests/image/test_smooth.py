import unittest

from image import read, write


class TestSmoothImage(unittest.TestCase):

    def test_smooth(self):
        # Smooth entire image
        img = read('./test_data/test_smooth.png')
        org = img.copy()
        img.smooth()
        write('./test_data/test_smoothed.png', img)
        self.assertGreater(org.compare(img), 0)

    def test_region(self):
        # Smooth region
        img = read("./test_data/test_smooth.png")
        org = img.copy()
        w, h, _ = img.shape
        region = (int(w/2 - w/4), int(h/2 - h/4)), (int(w/2 + w/4), int(h/2 + h/4))
        img.smooth(region=region)
        write('./test_data/test_smoothed_region.png', img)
        self.assertGreater(org.compare(img), 0)


if __name__ == '__main__':
    unittest.main()
