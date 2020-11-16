import unittest
from image import read, write
from image.mode import Mode


class ImageProperties(unittest.TestCase):

    img1 = read(r'./test_data/test_image_0.jpg')
    img2 = read(r'./test_data/test_greyscale.png')

    def test_width(self):
        self.assertEqual(self.img1.width, 1511)

    def test_height(self):
        self.assertEqual(self.img1.height, 2015)

    def test_channels(self):
        self.assertEqual(self.img1.channels, 3)
        self.assertEqual(self.img2.channels, 3)


if __name__ == '__main__':
    unittest.main()
