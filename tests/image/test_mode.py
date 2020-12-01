import unittest
from os.path import join

from helpers import TestFileHelper
from image import read, write


class ModeConversions(unittest.TestCase, TestFileHelper):

    def test_to_greyscale(self):
        rgb = read(self._test_file('test_rgb.png'))
        grey = rgb.mode.to_greyscale()
        with self._temp_dir() as temp_dir:
            path = join(temp_dir, 'test_greyscale.png')
            write(path, grey)
        self.assertEqual(rgb.channels, 3)
        self.assertEqual(grey.channels, 0)


if __name__ == '__main__':
    unittest.main()
