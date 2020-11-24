
import unittest
from os.path import join

from numpy import array

from image import Image, write


class ImageCreate(unittest.TestCase):

    path = './test_data/'
    w = 100
    h = 100
    c = 3

    def test_create_black_image(self):
        reference_color = array([0, 0, 0])
        img = Image.create(size=(self.w, self.h))
        write(join(self.path, 'text_image_create_black.png'), img)
        test_color = img[int(self.h/2)][int(self.w/2)]
        check = test_color == reference_color[::-1]
        self.assertTrue(check.all())

    def test_create_white_image(self):
        reference_color = array([255, 255, 255])
        img = Image.create(size=(self.w, self.h), background=reference_color)
        write(join(self.path, 'text_image_create_white.png'), img)
        test_color = img[int(self.h/2)][int(self.w/2)]
        check = test_color == reference_color[::-1]
        self.assertTrue(check.all())

    def test_create_red_image(self):
        reference_color = array([255, 0, 0])
        img = Image.create(size=(self.w, self.h), background=reference_color)
        write(join(self.path, 'text_image_create_red.png'), img)
        test_color = img[int(self.h/2)][int(self.w/2)]
        check = test_color == reference_color[::-1]
        self.assertTrue(check.all())

    def test_create_green_image(self):
        reference_color = array([0, 255, 0])
        img = Image.create(size=(self.w, self.h), background=reference_color)
        write(join(self.path, 'text_image_green.png'), img)
        test_color = img[int(self.h/2)][int(self.w/2)]
        check = test_color == reference_color[::-1]
        self.assertTrue(check.all())

    def test_create_blue_image(self):
        reference_color = array([0, 0, 255])
        img = Image.create(size=(self.w, self.h), background=reference_color)
        write(join(self.path, 'text_image_blue.png'), img)
        test_color = img[int(self.h/2)][int(self.w/2)]
        check = test_color == reference_color[::-1]
        self.assertTrue(check.all())


if __name__ == '__main__':
    unittest.main()
