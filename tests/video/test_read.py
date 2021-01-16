import unittest

from helpers import TestFileHelper
from video import Video


class TestReadVideo(unittest.TestCase, TestFileHelper):

    def test_read_video(self):
        path = self._test_file('test_video_read.mp4')

        with Video(path) as video:
            frames = video.read()
            self.assertEqual(len(frames), video.length)


if __name__ == '__main__':
    unittest.main()
