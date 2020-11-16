import unittest

from image import read, write


class MSEMetric(unittest.TestCase):

    def test_identical_images(self):
        # Compare identical images with the same shape.
        img1 = read('./test_data/test_image_0.jpg')
        img2 = read('./test_data/test_image_0.jpg')
        self.assertEqual(img1.metrics.mse(img2), 0)

    def test_different_images(self):
        # Compare different images with the same shape.
        img1 = read('./test_data/test_image_0.jpg')
        img2 = read('./test_data/test_image_1.jpg')
        self.assertGreater(img1.metrics.mse(img2), 0)

    def test_shrunk_shape(self):
        # Compare images with different shapes.
        img1 = read('./test_data/test_image_0.jpg')
        img2 = read('./test_data/test_image_2.jpg')  # shrunk

        with self.assertRaises(ValueError):
            img1.metrics.mse(img2)

    def test_rotated_shape(self):
        img1 = read('./test_data/test_image_0.jpg')
        img3 = read('./test_data/test_image_3.jpg')  # rotated

        with self.assertRaises(ValueError):
            img1.metrics.mse(img3)


if __name__ == '__main__':
    unittest.main()