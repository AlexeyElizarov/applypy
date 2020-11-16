import unittest
from image import read, write


class ModeConversions(unittest.TestCase):

    def test_to_greyscale(self):
        rgb = read(r'./test_data/test_rgb.png')
        rgb.mode.to_greyscale()
        write(r'./test_data/test_greyscale.png', rgb)
        self.assertEqual(rgb.channels, 0)


if __name__ == '__main__':
    unittest.main()
