import unittest

import numpy

from helpers import TestFileHelper
from image import Image


class ImageCreate(unittest.TestCase, TestFileHelper):
    SIZE = (100, 100)

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    def test_default_background(self):
        created_image = Image.create(size=self.SIZE, background=None)
        self.assertIsNotNone(created_image)
        expected_image = numpy.full((self.SIZE[1], self.SIZE[0], len(self.BLACK)), self.BLACK[::-1])
        numpy.testing.assert_array_equal(created_image, expected_image)

    def test_black(self):
        created_image = Image.create(size=self.SIZE, background=self.BLACK)
        self.assertIsNotNone(created_image)
        expected_image = numpy.full((self.SIZE[1], self.SIZE[0], len(self.BLACK)), self.BLACK[::-1])
        numpy.testing.assert_array_equal(created_image, expected_image)

    def test_white(self):
        created_image = Image.create(size=self.SIZE, background=self.WHITE)
        self.assertIsNotNone(created_image)
        expected_image = numpy.full((self.SIZE[1], self.SIZE[0], len(self.WHITE)), self.WHITE[::-1])
        numpy.testing.assert_array_equal(created_image, expected_image)

    def test_red(self):
        created_image = Image.create(size=self.SIZE, background=self.RED)
        self.assertIsNotNone(created_image)
        expected_image = numpy.full((self.SIZE[1], self.SIZE[0], len(self.RED)), self.RED[::-1])
        numpy.testing.assert_array_equal(created_image, expected_image)

    def test_green(self):
        created_image = Image.create(size=self.SIZE, background=self.GREEN)
        self.assertIsNotNone(created_image)
        expected_image = numpy.full((self.SIZE[1], self.SIZE[0], len(self.GREEN)), self.GREEN[::-1])
        numpy.testing.assert_array_equal(created_image, expected_image)

    def test_blue(self):
        created_image = Image.create(size=self.SIZE, background=self.BLUE)
        self.assertIsNotNone(created_image)
        expected_image = numpy.full((self.SIZE[1], self.SIZE[0], len(self.BLUE)), self.BLUE[::-1])
        numpy.testing.assert_array_equal(created_image, expected_image)


if __name__ == '__main__':
    unittest.main()
