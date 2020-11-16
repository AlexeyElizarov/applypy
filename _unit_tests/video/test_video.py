import unittest

from video import read


class TestVideo(unittest.TestCase):

    # test properties
    def test_length(self):
        pass
        # video = read('test_video_read.mp4')
        # print(video.length)
        # self.assertGreater(video.length, 0)


if __name__ == '__main__':
    unittest.main()
