from elements import TelegramNotificationElement
from helpers import TestFileHelper, profile
from video import Video
from time import time


class TestPerformanceDetect(TestFileHelper):

    def test_performance(self):
        t0 = self.initial()
        t2 = self.detect_hist()

        print(t0, t2, ((t2 - t0) / t0) * 100)

    def initial(self):

        vid = self._test_file('test_perf_roi.mp4')
        element = TelegramNotificationElement()

        with Video(vid) as video:
            start = time()
            video.detect(element)

        return time() - start

    def detect_hist(self):

        vid = self._test_file('test_perf_roi.mp4')
        element = TelegramNotificationElement()

        with Video(vid) as video:
            start = time()
            video._detect_hist(element)

        return time() - start


if __name__ == '__main__':
    test = TestPerformanceDetect()
    test.test_performance()
    # test.detect_mse()

