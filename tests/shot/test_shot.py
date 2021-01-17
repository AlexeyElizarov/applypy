import unittest

from shot import Shot
from video import Video


class TestShotProperties(unittest.TestCase):

    path = r"D:\PyProjects\blurTelegramNotifications\tests\video\test_data\test_video_read.mp4"

    def test_end(self):
        with Video(self.path) as video:
            shot = Shot(video, 0)
            self.assertEqual(shot.length, video.length)

    def test_length(self):
        with Video(self.path) as video:
            shot = Shot(video, 0, 100)
            self.assertEqual(shot.length, 100)

    def test_begin(self):
        with Video(self.path) as video:
            shot = Shot(video, 0, 100)
            self.assertEqual(shot.begin, 0)

    def test_finish(self):
        with Video(self.path) as video:
            shot = Shot(video, 0, 100)
            self.assertEqual(shot.finish, 100/30)

    def test_duration(self):
        with Video(self.path) as video:
            shot = Shot(video, 0, 100)
            self.assertEqual(shot.duration, 100/30)


if __name__ == '__main__':
    unittest.main()
