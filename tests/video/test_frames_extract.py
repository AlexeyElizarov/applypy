import unittest

from video import Video


class TestFrames(unittest.TestCase):

    path = r'.\test_data\test_video_read.mp4'

    def test_extract_threshold(self):

        with Video(self.path) as video:
            frames = video.frames.extract(threshold=200)
            self.assertEqual(len(frames), 7)

    def test_extract_all(self):

        with Video(self.path) as video:
            frames = video.frames.extract()
            self.assertEqual(len(frames), video.length)


if __name__ == '__main__':
    unittest.main()
