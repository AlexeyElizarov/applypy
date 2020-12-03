import unittest
from random import randint

import image
from video import Video


class TestFrames(unittest.TestCase):

    path = r'.\test_data\video_write.mp4'

    def test_read(self):

        frame_num = 128

        with Video(self.path) as video:
            frame = video.frames.read(frame_num)
            image.write(r'.\test_data\frame_read.png', frame)

        frame = frame.mode.to_greyscale()

        for i in range(100):
            rand_x = randint(0, frame.width - 1)
            rand_y = randint(0, frame.height - 1)
            self.assertAlmostEqual(frame[rand_x][rand_y], frame_num, delta=3)


if __name__ == '__main__':
    unittest.main()
