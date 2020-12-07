import unittest

from os.path import dirname, basename, splitext, join
from random import randint

from image import Image, write, read
from elements import BaseElement
from helpers import TestFileHelper
from pallet import GREEN

TEST_CASES = {'rect_black': r'.\test_data\test_rect_black.png',
              'rect_white': r'.\test_data\test_rect_white.png',
              'rect_ranged': r'.\test_data\test_rect_ranged.png',
              'rect_noised': r'.\test_data\test_rect_noised.png',
              'test_roi': 'test_detect_roi.png'}

GRAY = 128, 128, 128
GRAY_50 = [int(c * 2 / 4) for c in GRAY]
GRAY_75 = [int(c * 3 / 4) for c in GRAY]
GRAY_125 = [int(c * 5 / 4) for c in GRAY]
GRAY_175 = [int(c * 6 / 4) for c in GRAY]
WHITE = 255, 255, 255


def prepare_test_data():
    w, h = 200, 200
    pt1 = int(w * 1 / 4), int(h * 1 / 4)
    pt2 = int(w * 3 / 4), int(h * 3 / 4)

    # Rectangle on black
    img = Image.create(size=(w, h))
    img = img.draw.rectangle(pt1, pt2, GRAY, filled=True)
    write(TEST_CASES['rect_black'], img)

    # Rectangle on white
    img = Image.create(size=(w, h), background=WHITE)
    img = img.draw.rectangle(pt1, pt2, GRAY, filled=True)
    write(TEST_CASES['rect_white'], img)

    # Ranged rectangles
    img = Image.create(size=(w, h))
    rect1 = (int(w * 1 / 4), int(h * 1 / 4)), (int(w * 2 / 4), int(w * 2 / 4))
    rect2 = (int(w * 2 / 4), int(h * 1 / 4)), (int(w * 3 / 4), int(w * 2 / 4))
    rect3 = (int(w * 1 / 4), int(h * 2 / 4)), (int(w * 2 / 4), int(w * 3 / 4))
    rect4 = (int(w * 2 / 4), int(h * 2 / 4)), (int(w * 3 / 4), int(w * 3 / 4))
    rect5 = (int(w * 3 / 8), int(h * 3 / 8)), (int(w * 5 / 8), int(w * 5 / 8))
    img = img.draw.rectangle(*rect1, GRAY_75, filled=True)
    img = img.draw.rectangle(*rect2, GRAY_50, filled=True)
    img = img.draw.rectangle(*rect3, GRAY_125, filled=True)
    img = img.draw.rectangle(*rect4, GRAY_175, filled=True)
    img = img.draw.rectangle(*rect5, GRAY, filled=True)
    write(TEST_CASES['rect_ranged'], img)

    # Rectangle with noise
    img = Image.create(size=(w, h))
    img = img.draw.rectangle(pt1, pt2, GRAY, filled=True)
    noise = []

    for i in range(50):
        x, y = randint(0, w), randint(0, h)
        noise.append((x, y))

    for center in noise:
        img = img.draw.circle(center, 3, GRAY, filled=True)

    write(TEST_CASES['rect_noised'], img)


prepare_test_data()


class TestElement(BaseElement):

    def detect(self, **kwargs):
        pass


class FindContours(unittest.TestCase, TestFileHelper):

    def test_rect_black(self):
        test_case_path = TEST_CASES['rect_black']
        img = read(test_case_path)
        contours = TestElement().find_contours(img, GRAY)
        img = img.draw.contours(contours, color=(0, 255, 0))
        write(self.get_path(test_case_path), img)

    def test_rect_white(self):
        test_case_path = TEST_CASES['rect_white']
        img = read(test_case_path)
        contours = TestElement().find_contours(img, GRAY)
        img = img.draw.contours(contours, color=(0, 255, 0))
        write(self.get_path(test_case_path), img)

    def test_rect_ranged(self):
        _ = [0, 25, 75]
        k_range = [(i/100, j/100) for i in _ for j in _]
        test_case_path = TEST_CASES['rect_ranged']

        for k in k_range:
            img = read(test_case_path)
            contours = TestElement().find_contours(img, GRAY, k)
            img = img.draw.contours(contours, color=(0, 255, 0))
            path = self.get_path(test_case_path)
            dir_name = dirname(path)
            base_name = basename(path)
            file_name, extension = splitext(base_name)
            file_name = f'{file_name}_{str(int(k[0]*100)).zfill(2)}_{str(int(k[1]*100)).zfill(2)}{extension}'
            write(join(dir_name, file_name), img)

    def test_rect_noised(self):
        test_case_path = TEST_CASES['rect_noised']
        img = read(test_case_path)
        contours = TestElement().find_contours(img, GRAY, kernel=7)
        img = img.draw.contours(contours, color=(0, 255, 0))
        write(self.get_path(test_case_path), img)

    def test_roi(self):
        path = self._test_file(TEST_CASES['test_roi'])
        img = read(path)
        roi = img.set_roi(img.width / 2, img.height / 2)
        offset = roi.width, roi.height
        contours = TestElement().find_contours(roi, WHITE, offset=offset)
        img = img.draw.contours(contours, color=GREEN)
        write(self.get_path(path), img)

    @staticmethod
    def get_path(in_path):
        dir_name = dirname(in_path)
        base_name = basename(in_path)
        file_name, extension = splitext(base_name)
        file_name = file_name + '_detected'
        base_name = f'{file_name}{extension}'
        return join(dir_name, base_name)


if __name__ == '__main__':
    prepare_test_data()
    unittest.main()
