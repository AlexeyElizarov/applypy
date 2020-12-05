import unittest

import numpy

from helpers import TestFileHelper
from image import Image, read


class DrawRect(unittest.TestCase, TestFileHelper):
    WIDTH = 200
    HEIGHT = 300
    SIZE = (WIDTH, HEIGHT)
    RECT_POINT1 = (int(WIDTH * 1 / 4), int(HEIGHT * 1 / 4))
    RECT_POINT2 = (int(WIDTH * 3 / 4), int(HEIGHT * 3 / 4))

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    def test_rect_baseline(self):
        img = Image.create(size=self.SIZE)
        rect = img.draw.rectangle(self.RECT_POINT1, self.RECT_POINT2, color=self.WHITE)
        expected = read(self._test_file('test_draw_rect_base.png'))
        numpy.testing.assert_array_equal(rect, expected)

    def test_rect_blue(self):
        img = Image.create(size=self.SIZE)
        rect = img.draw.rectangle(self.RECT_POINT1, self.RECT_POINT2, color=self.BLUE)
        expected = read(self._test_file('test_draw_rect_blue.png'))
        numpy.testing.assert_array_equal(rect, expected)

    def test_rect_red(self):
        img = Image.create(size=self.SIZE)
        rect = img.draw.rectangle(self.RECT_POINT1, self.RECT_POINT2, color=self.RED)
        expected = read(self._test_file('test_draw_rect_red.png'))
        numpy.testing.assert_array_equal(rect, expected)

    def test_rect_green(self):
        img = Image.create(size=self.SIZE)
        rect = img.draw.rectangle(self.RECT_POINT1, self.RECT_POINT2, color=self.GREEN)
        expected = read(self._test_file('test_draw_rect_green.png'))
        numpy.testing.assert_array_equal(rect, expected)

    def test_rect_thick(self):
        img = Image.create(size=self.SIZE)
        rect = img.draw.rectangle(self.RECT_POINT1, self.RECT_POINT2, color=self.WHITE, thickness=5)
        expected = read(self._test_file('test_draw_rect_thick.png'))
        numpy.testing.assert_array_equal(rect, expected)

    def test_rect_filled(self):
        img = Image.create(size=self.SIZE)
        rect = img.draw.rectangle(self.RECT_POINT1, self.RECT_POINT2, color=self.WHITE, filled=True)
        expected = read(self._test_file('test_draw_rect_filled.png'))
        numpy.testing.assert_array_equal(rect, expected)


if __name__ == '__main__':
    unittest.main()
