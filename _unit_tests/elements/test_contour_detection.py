import unittest

from image import Image, write


def prepare_test_data():
    img = Image.create(size=(200, 200))
    img.draw.rectangle()
    write(r'.\test_data\test_contours_1.png', img)


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
