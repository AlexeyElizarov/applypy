from binascii import unhexlify
from time import time
from os.path import exists

from cv2.cv2 import VideoCapture, VideoWriter, VideoWriter_fourcc
from numpy import uint8
from tqdm import tqdm

from handler import VideoHandler
from image import Image


class Video:

    def __init__(self, path):
        self._path = path
        self._handler = VideoHandler(self)

    def __enter__(self):
        if exists(self._path):
            self.cap = VideoCapture(self._path)
            return self
        else:
            raise FileNotFoundError

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cap.release()

    def detect(self, element):

        elements = []

        for i in tqdm(range(self.length)):
            frame = self.frames.read(i)
            contours = element.detect(frame)
            if contours:
                elements.append((i, contours))

        return elements

    @property
    def framerate(self):
        return self.cap.get(5)

    @property
    def width(self):
        return int(self.cap.get(3))

    @property
    def height(self):
        return int(self.cap.get(4))

    @property
    def dimension(self):
        return self.width, self.height

    @property
    def codec(self):
        return unhexlify('%x' % int(self.cap.get(6)))[::-1].decode()

    @property
    def length(self):
        return int(self.cap.get(7))

    @property
    def frames(self):
        return self._handler.frames

    @staticmethod
    def create_image(image):
        return Image(image)

    @staticmethod
    def write(frames, path, codec, bitrate, dimension):
        raise NotImplementedError

        # with Writer(path, codec, bitrate, dimension) as vw:
        #     vw.write(frames)


class Writer:

    def __init__(self, path, codec, bitrate, dimension):
        self._path = path
        self._codec = codec
        self._bitrate = bitrate
        self._dimension = dimension

    def __enter__(self):
        self._writer = VideoWriter(self._path, VideoWriter_fourcc(*self._codec), self._bitrate, self._dimension)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._writer.release()

    def write(self, frames):

        for frame in frames:
            frame = uint8(frame)
            self._writer.write(frame)