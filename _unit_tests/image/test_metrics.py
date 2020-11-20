import unittest

from image import read, write


class MSEMetric(unittest.TestCase):

    img1 = read('./test_data/test_image_0.jpg')
    img2 = img1
    img3 = read('./test_data/test_image_1.jpg')
    img4 = read('./test_data/test_image_2.jpg')  # shrunk
    img5 = read('./test_data/test_image_3.jpg')  # rotated
    img6 = read('./test_data/test_smooth.png')   # smooth
    img7 = read('./test_data/test_smoothed.png')  # smoothed

    def test_identical_images(self):
        # Compare identical images with the same shape.
        self.assertEqual(self.img1.metrics.mse(self.img2), 0)

    def test_different_images(self):
        # Compare different images with the same shape.
        self.assertGreater(self.img1.metrics.mse(self.img3), 0)

    def test_shrunk_shape(self):
        # Compare images with different shapes / shrunk.

        with self.assertRaises(ValueError):
            self.img1.metrics.mse(self.img4)

    def test_rotated_shape(self):
        # Compare images with different shapes / rotated.

        with self.assertRaises(ValueError):
            self.img1.metrics.mse(self.img5)

    def test_smoothed(self):
        # Compare different images with the same shape / smoothed.
        self.assertGreater(self.img6.metrics.mse(self.img7), 0)

if __name__ == '__main__':
    unittest.main()