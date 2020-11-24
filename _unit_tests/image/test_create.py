import unittest

import numpy

from image import Image, write


class ImageCreate(unittest.TestCase):

    arr = numpy.array([[128 for i in range(100)] for j in range(100)])
    path = './test_data/test_image_created.png'

    def test_create_image(self):
        img = Image.create(self.arr)
        write(self.path, img)
        self.assertEqual(img.size, self.arr.size)


if __name__ == '__main__':
    unittest.main()
