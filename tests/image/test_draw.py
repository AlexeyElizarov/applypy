import unittest
from os.path import join

from helpers import TestFileHelper
from image import Image, write


class DrawRect(unittest.TestCase, TestFileHelper):
    w, h = 200, 300
    top_left = int((w * 1 / 4)), int(h * 1 / 4)
    bottom_right = int((w * 3 / 4)), int(h * 3 / 4)

    def test_rect_baseline(self):
        img = Image.create(size=(self.w, self.h))
        rect = img.draw.rectangle(self.top_left, self.bottom_right, color=(255, 255, 255))
        with self._temp_dir() as temp_dir:
            write(join(temp_dir, 'test_draw_rect_base.png'), rect)

    def test_rect_blue(self):
        img = Image.create(size=(self.w, self.h))
        rect = img.draw.rectangle(self.top_left, self.bottom_right, color=(0, 0, 255))
        with self._temp_dir() as temp_dir:
            write(join(temp_dir, 'test_draw_rect_blue.png'), rect)

    def test_rect_red(self):
        img = Image.create(size=(self.w, self.h))
        rect = img.draw.rectangle(self.top_left, self.bottom_right, color=(255, 0, 0))
        with self._temp_dir() as temp_dir:
            write(join(temp_dir, 'test_draw_rect_red.png'), rect)

    def test_rect_green(self):
        img = Image.create(size=(self.w, self.h))
        rect = img.draw.rectangle(self.top_left, self.bottom_right, color=(0, 255, 0))
        with self._temp_dir() as temp_dir:
            write(join(temp_dir, 'test_draw_rect_green.png'), rect)

    def test_rect_thick(self):
        img = Image.create(size=(self.w, self.h))
        rect = img.draw.rectangle(self.top_left, self.bottom_right, color=(255, 255, 255), thickness=5)
        with self._temp_dir() as temp_dir:
            write(join(temp_dir, 'test_draw_rect_thick.png'), rect)

    def test_rect_filled(self):
        img = Image.create(size=(self.w, self.h))
        rect = img.draw.rectangle(self.top_left, self.bottom_right, color=(255, 255, 255), filled=True)
        with self._temp_dir() as temp_dir:
            write(join(temp_dir, 'test_draw_rect_filled.png'), rect)


if __name__ == '__main__':
    unittest.main()
