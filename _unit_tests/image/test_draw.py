import unittest

from numpy import array

from image import Image, write


class DrawRect(unittest.TestCase):

    w, h = 200, 300
    top_left = int((w * 1/4)), int(h * 1/4)
    bottom_right = int((w * 3/4)), int(h * 3/4)

    def test_rect_baseline(self):

        img = Image.create(size=(self.w, self.h))
        img.draw.rectangle(self.top_left, self.bottom_right, color=(255, 255, 255))
        write(r'.\test_data\test_draw_rect_base.png', img)

    def test_rect_blue(self):

        img = Image.create(size=(self.w, self.h))
        img.draw.rectangle(self.top_left, self.bottom_right, color=(0, 0, 255))
        write(r'.\test_data\test_draw_rect_blue.png', img)

    def test_rect_red(self):

        img = Image.create(size=(self.w, self.h))
        img.draw.rectangle(self.top_left, self.bottom_right, color=(255, 0, 0))
        write(r'.\test_data\test_draw_rect_red.png', img)

    def test_rect_green(self):

        img = Image.create(size=(self.w, self.h))
        img.draw.rectangle(self.top_left, self.bottom_right, color=(0, 255, 0))
        write(r'.\test_data\test_draw_rect_green.png', img)

    def test_rect_thick(self):

        img = Image.create(size=(self.w, self.h))
        img.draw.rectangle(self.top_left, self.bottom_right, color=(255, 255, 255), thickness=5)
        write(r'.\test_data\test_draw_rect_thick.png', img)

    def test_rect_filled(self):

        img = Image.create(size=(self.w, self.h))
        img.draw.rectangle(self.top_left, self.bottom_right, color=(255, 255, 255), filled=True)
        write(r'.\test_data\test_draw_rect_filled.png', img)

if __name__ == '__main__':
    unittest.main()
