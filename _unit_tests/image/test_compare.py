import unittest

from image import read, write


class TestCompareImages(unittest.TestCase):

    def test_compare(self):
        # Compare images with the same shape.
        img1 = read('./test_data/test_image_0.jpg')
        img2 = img1
        img3 = read('./test_data/test_image_1.jpg')
        self.assertEqual(img1.compare(img2), 0)
        self.assertEqual(img2.compare(img1), 0)
        self.assertGreater(img1.compare(img3), 0)

    def test_shapes(self):
        # Compare images with different shapes.
        img1 = read('./test_data/test_image_0.jpg')
        img2 = read('./test_data/test_image_2.jpg')  # shrunk
        img3 = read('./test_data/test_image_3.jpg')  # rotated

        with self.assertRaises(ValueError):
            img1.compare(img2)

        with self.assertRaises(ValueError):
            img1.compare(img3)

        with self.assertRaises(ValueError):
            img2.compare(img3)


if __name__ == '__main__':
    unittest.main()