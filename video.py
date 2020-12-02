from os.path import exists

from cv2.cv2 import VideoCapture, CAP_PROP_FRAME_COUNT, VideoWriter, VideoWriter_fourcc
from numpy import uint8

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
        raise NotImplementedError

    @property
    def bitrate(self):
        raise NotImplementedError

    @property
    def dimension(self):
        raise NotImplementedError

    @property
    def codec(self):
        raise NotImplementedError

    @property
    def length(self):
        return int(self.cap.get(CAP_PROP_FRAME_COUNT))

    @property
    def frames(self):
        return self._handler.frames

    @staticmethod
    def create_image(image):
        return Image(image)

    @staticmethod
    def write(frames, path, codec, bitrate, dimension):

        with Writer(path, codec, bitrate, dimension) as vw:
            vw.write(frames)


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