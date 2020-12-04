import unittest

import numpy

from helpers import TestFileHelper
from image import read


class ModeConversions(unittest.TestCase, TestFileHelper):

    def test_to_greyscale(self):
        rgb = read(self._test_file('test_rgb.png'))
        grey = rgb.mode.to_greyscale()
        self.assertEqual(rgb.channels, 3)
        self.assertEqual(grey.channels, 0)
        # ожидаемая картинка размером 100*100 и с одним планом
        # левая половина заполнена 91, а правая 123
        expected = numpy.full((100, 100), [91] * 50 + [123] * 50)
        numpy.testing.assert_array_equal(grey, expected)


if __name__ == '__main__':
    unittest.main()
