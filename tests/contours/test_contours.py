import unittest

import pallet
from elements import TestElement
from helpers import TestFileHelper
from image import read


class ContourRect(unittest.TestCase, TestFileHelper):

    def test_rectangle(self):
        img = read(self._test_file('test_rect_black.png'))
        contours = TestElement().find_contours(img, pallet.GRAY)
        ref_rectangles = [(50, 50, 101, 101)]

        for i in range(len(contours)):
            self.assertTrue(contours[i].rectangle, ref_rectangles[i])


if __name__ == '__main__':
    unittest.main()
