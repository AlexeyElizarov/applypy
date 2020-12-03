import unittest

from video import Video


class TestVideo(unittest.TestCase):

    vid1 = r'.\test_data\test_video_read.mp4'
    vid2 = r'.\test_data\invalid.mp4'

    def test_length(self):
        # Test valid video path

        with Video(self.vid1) as video:
            self.assertGreater(video.length, 0)

    def test_invalid_path(self):
        # Test invalid video path

        with self.assertRaises(FileNotFoundError):

            with Video(self.vid2) as video:
                pass


if __name__ == '__main__':
    unittest.main()
