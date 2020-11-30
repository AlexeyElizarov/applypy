import unittest

from helpers import TestFileHelper
from image import read


class MSEMetric(unittest.TestCase, TestFileHelper):

    def test_identical_images(self):
        # Compare identical images with the same shape.
        img1 = read(self._test_file('test_image_0.jpg'))
        img2 = read(self._test_file('test_image_0.jpg'))
        self.assertEqual(img1.metrics.mse(img2), 0)

    def test_different_images(self):
        # Compare different images with the same shape.
        img1 = read(self._test_file('test_image_0.jpg'))
        img3 = read(self._test_file('test_image_1.jpg'))
        self.assertGreater(img1.metrics.mse(img3), 0)

    def test_shrunk_shape(self):
        # Compare images with different shapes / shrunk.
        img1 = read(self._test_file('test_image_0.jpg'))
        img4 = read(self._test_file('test_image_2.jpg'))  # shrunk

        with self.assertRaises(ValueError):
            img1.metrics.mse(img4)

    def test_rotated_shape(self):
        # Compare images with different shapes / rotated.
        img1 = read(self._test_file('test_image_0.jpg'))
        img5 = read(self._test_file('test_image_3.jpg'))  # rotated

        with self.assertRaises(ValueError):
            img1.metrics.mse(img5)

    def test_smoothed(self):
        # Compare different images with the same shape / smoothed.
        img6 = read(self._test_file('test_smooth.png'))  # smooth
        img7 = read(self._test_file('test_smoothed.png'))  # smoothed
        self.assertGreater(img6.metrics.mse(img7), 0)


if __name__ == '__main__':
    unittest.main()
