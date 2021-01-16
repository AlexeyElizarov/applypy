import unittest
from random import randint
from video import Video
from helpers import TestFileHelper


class TestFrames(unittest.TestCase, TestFileHelper):

    def test_get_frame(self):

        path = self._test_file('test_video_write.mp4')
        frame_num = 128

        with Video(path) as video:
            frame = video.frames.get(frame_num)

        frame = frame.mode.to_greyscale()

        for i in range(100):
            rand_x = randint(0, frame.width - 1)
            rand_y = randint(0, frame.height - 1)
            self.assertAlmostEqual(frame[rand_x][rand_y], frame_num, delta=3)


if __name__ == '__main__':
    unittest.main()
