import unittest

from shot import Shot
from video import Video


class TestShotWriter(unittest.TestCase):

    path = r"D:\PyProjects\blurTelegramNotifications\tests\video\test_data\test_video_read.mp4"

    def test_shot_writer1(self):

        with Video(self.path) as video:
                shot = Shot(video, 0, 19)
                shot.write(r'test_shot_write1.mp4')

    def test_shot_writer2(self):

        with Video(self.path) as video:
                shot = Shot(video, 19, 65)
                shot.write(r'test_shot_write2.mp4')

    def test_shot_writer3(self):

        with Video(self.path) as video:
                shot = Shot(video, 65, 168)
                shot.write(r'test_shot_write3.mp4')

    def test_shot_writer4(self):

        with Video(self.path) as video:
                shot = Shot(video, 168)
                shot.write(r'test_shot_write4.mp4')

if __name__ == '__main__':
    unittest.main()
