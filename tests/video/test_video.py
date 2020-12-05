import unittest
from video import Video
from helpers import TestFileHelper


class TestVideo(unittest.TestCase, TestFileHelper):

    def test_valid_path(self):
        # Test valid video path
        path = self._test_file('test_video_read.mp4')
        with Video(path) as video:
            self.assertGreater(video.length, 0)

    def test_invalid_path(self):
        # Test invalid video path
        path = self._test_file('invalid.mp4')
        with self.assertRaises(FileNotFoundError):
            with Video(path):
                pass


if __name__ == '__main__':
    unittest.main()
