import unittest

from video import Video
from helpers import TestFileHelper


class TestFrames(unittest.TestCase, TestFileHelper):

    def test_extract_threshold(self):

        path = self._test_file('test_video_read.mp4')

        with Video(path) as video:
            frames = video.frames.extract(threshold=200)
            self.assertEqual(len(frames), 7)

    def test_extract_all(self):

        path = self._test_file('test_video_read.mp4')

        with Video(path) as video:
            frames = video.frames.extract()
            self.assertEqual(len(frames), video.length)


if __name__ == '__main__':
    unittest.main()
