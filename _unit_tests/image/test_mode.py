import unittest
from image import read, write


class ModeConversions(unittest.TestCase):

    def test_to_greyscale(self):
        rgb = read(r'./test_data/test_rgb.png')
        gray = rgb.mode.to_greyscale()
        write(r'./test_data/test_greyscale.png', gray)
        self.assertEqual(gray.channels, 0)


if __name__ == '__main__':
    unittest.main()
