import unittest
from image import read


class ImageProperties(unittest.TestCase):

    img1 = read(r'./test_data/test_image_0.jpg')
    img2 = read(r'./test_data/test_greyscale.png')
    img3 = read(r'./test_data/test_rgb.png')

    def test_width(self):
        self.assertEqual(self.img1.width, 1511)

    def test_height(self):
        self.assertEqual(self.img1.height, 2015)

    def test_channels(self):
        self.assertEqual(self.img1.channels, 3)
        self.assertEqual(self.img2.channels, 3)

    def test_size(self):
        self.assertEqual(self.img3.size, self.img3.width * self.img3.height * self.img3.channels)


if __name__ == '__main__':
    unittest.main()
