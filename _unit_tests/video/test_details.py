import unittest
from video import Video


class TestVideoDetails(unittest.TestCase):

    def test_width(self):

        path = r"D:\PyProjects\blurTelegramNotifications\_unit_tests\video\test_data\test_video_read.mp4"
        ref_width = 1092

        with Video(path) as video:
            self.assertEqual(video.width, ref_width)

    def test_height(self):

        path = r"D:\PyProjects\blurTelegramNotifications\_unit_tests\video\test_data\test_video_read.mp4"
        ref_height = 614

        with Video(path) as video:
            self.assertEqual(video.height, ref_height)

    def test_dimension(self):

        path = r"D:\PyProjects\blurTelegramNotifications\_unit_tests\video\test_data\test_video_read.mp4"
        ref_dimension = (1092, 614)

        with Video(path) as video:
            self.assertEqual(video.dimension, ref_dimension)

    def test_framerate(self):

        path = r"D:\PyProjects\blurTelegramNotifications\_unit_tests\video\test_data\test_video_read.mp4"
        ref_framerate = 30.0

        with Video(path) as video:
            self.assertEqual(video.framerate, ref_framerate)

    def test_codec(self):

        path = r"D:\PyProjects\blurTelegramNotifications\_unit_tests\video\test_data\test_video_read.mp4"
        ref_codec = 'avc1'

        with Video(path) as video:
            self.assertEqual(video.codec, ref_codec)


if __name__ == '__main__':
    unittest.main()
