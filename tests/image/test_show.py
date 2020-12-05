import unittest
from helpers import TestFileHelper
from image import read


class ShowImage(unittest.TestCase, TestFileHelper):

    def test_show(self):
        path = self._test_file('test_image_0.jpg')
        image = read(path)
        image.show()


if __name__ == '__main__':
    unittest.main()
