import unittest

from helpers import TestFileHelper
from image import read
from time import time
from numba import jit, njit
import numpy as np

from skimage.metrics import mean_squared_error


# class TestPerformanceMSE(unittest.TestCase, TestFileHelper):
#
#     def test_performance(self):
#
#         t0 = self.initial()
#         t1 = self.improved()
#
#         print(t0, t1, ((t1 - t0)/t0) * 100)
#
#
#     def improved(self):
#
#         img1 = read(self._test_file('test_image_0.jpg'))
#         img3 = read(self._test_file('test_image_1.jpg'))
#         start = time()
#         for i in range(100):
#             mse_numba(img1, img3)
#         end = time()
#
#         return end - start
#
#     def initial(self):
#
#         img1 = read(self._test_file('test_image_0.jpg'))
#         img3 = read(self._test_file('test_image_1.jpg'))
#         start = time()
#         for i in range(100):
#             mean_squared_error(img1, img3)
#         end = time()
#
#         return end - start
#


def mse_numba(image0, image1):
    float_type = np.result_type(image0.dtype, image1.dtype, np.float32)
    image0 = np.asarray(image0, dtype=float_type)
    image1 = np.asarray(image1, dtype=float_type)
    return mean(image0, image1)

@jit
def mean(image0, image1):
    return np.mean((image0 - image1) ** 2)

def initial():

    img1 = read(r"D:\PyProjects\blurTelegramNotifications\tests\performance\test_data\test_image_0.jpg")
    img3 = read(r"D:\PyProjects\blurTelegramNotifications\tests\performance\test_data\test_image_1.jpg")
    start = time()
    for i in range(500):
        mean_squared_error(img1, img3)
    end = time()

    return end - start


def improved():

    img1 = read(r"D:\PyProjects\blurTelegramNotifications\tests\performance\test_data\test_image_0.jpg")
    img3 = read(r"D:\PyProjects\blurTelegramNotifications\tests\performance\test_data\test_image_1.jpg")
    start = time()
    for i in range(500):
        mse_numba(img1, img3)
    end = time()

    return end - start

def main():
    t0 = initial()
    t1 = improved()
    print(t0, t1, ((t1 - t0)/t0) * 100)

if __name__ == '__main__':
    # unittest.main()
    main()
