import os
import unittest

from numpy import array

from helpers import TestFileHelper
from image import Image
from video import Video, Writer


class TestFrames(unittest.TestCase, TestFileHelper):

    def test_write(self):
        codec = ('a', 'v', 'c', '1')
        frame_rate = 30
        width = 320
        height = 240

        with self._temp_dir() as temp_dir:
            path = os.path.join(temp_dir, 'test_video_write.mp4')

            with Writer(path, codec, frame_rate, (width, height)) as writer:
                for color in range(256):
                    img = Image(array([[[color, color, color] for x in range(width)] for y in range(height)]))
                    writer.write([img])

            with Video(path) as v:
                self.assertEqual(256, v.length)
                self.assertEqual(width, v.width)
                self.assertEqual(height, v.height)
                self.assertEqual(frame_rate, v.framerate)


if __name__ == '__main__':
    unittest.main()
