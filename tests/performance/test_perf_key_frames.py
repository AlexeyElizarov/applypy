import time
import unittest

from elements import TelegramNotificationElement
from helpers import TestFileHelper, profile
from video import Video


class TestPerformanceFindContours(TestFileHelper):

    def test_performance(self):

        t0 = self.initial()
        t1 = self.improved()

        print(t0, t1, ((t1 - t0)/t0) * 100)

    @profile
    def initial(self):

        path = self._test_file('test_perf_roi.mp4')
        element = TelegramNotificationElement()

        with Video(path) as video:
            start = time.time()
            video.detect(element)
            end = time.time()

        return end - start

    @profile
    def improved(self):

        path = self._test_file('test_perf_roi.mp4')
        element = TelegramNotificationElement()

        with Video(path) as video:
            start = time.time()
            video._detect(element)
            end = time.time()

        return end - start


if __name__ == '__main__':
    test = TestPerformanceFindContours()
    test.improved()
