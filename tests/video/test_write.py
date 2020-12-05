import unittest

from numpy import array

from image import Image
from video import Video


class TestFrames(unittest.TestCase):

    def test_write(self):
        path = r'.\test_data\video_write.mp4'
        frames = []
        codec = 'MP4V'
        framerate = 30
        dimension = 100
        for color in range(256):
            img = Image(array([[[color, color, color] for i in range(dimension)] for j in range(dimension)]))
            frames.append(img)

        Video.write(frames, path, codec, framerate, (dimension, dimension))

        with Video(path) as v:
            self.assertEqual(v.length, 256)


if __name__ == '__main__':
    unittest.main()
