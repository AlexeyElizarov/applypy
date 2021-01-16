"""Implements class for an image histogram"""
# https://helpx.adobe.com/hk_en/photoshop/using/viewing-histograms-pixel-values.html
# https://docs.opencv.org/master/d1/db7/tutorial_py_histogram_begins.html

from cv2 import calcHist, norm, NORM_L2
from matplotlib import pyplot as plt


class Histogram:

    _PARAMS = {'R': ([2], [256], [0, 256]),
               'G': ([1], [256], [0, 256]),
               'B': ([0], [256], [0, 256]),
               'L': ([0], [256], [0, 256]),
               'RGB': ([0, 1, 2], [256, 256, 256], [0, 256, 0, 256, 0, 256])}

    def __init__(self, image, channels):
        self._image = image
        self._channels = channels
        self.array = self._calculate()

    def _calculate(self):
        channels, bins, ranges = self._PARAMS[self._channels]

        if self._channels == 'L':
            image = self._image.mode.to_greyscale()
        else:
            image = self._image

        return calcHist([image], channels, None, bins, ranges)

    def plot(self):
        plt.plot(self.array)
        plt.show()

    @property
    def mean(self):
        return NotImplemented

    @property
    def std(self):
        return NotImplemented

    @property
    def median(self):
        return NotImplemented

    @property
    def pixels(self):
        return NotImplemented

    def compare(self, histogram):
        return norm(self.array, histogram.array, NORM_L2)

    def __str__(self):
        return self.array.__str__()