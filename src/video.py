from binascii import unhexlify
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

    def _detect(self, element):

        frames = []
        elements = []

        while True:
            ret, frame = self.cap.read()

            if ret:
                frames.append(Image(frame))
            else:
                break

        for frame in frames:

            contours = element.detect(frame)
            elements.append((frame, contours))

        return elements

    def detect(self, element):

        frames = []
        elements = []

        while True:
            ret, frame = self.cap.read()

            if ret:
                frames.append(Image(frame))
            else:
                break

        key_frame = frames[0]
        contours = element.detect(key_frame)
        hist0 = key_frame.metrics.histogram('L')

        for frame in frames:

            hist = frame.metrics.histogram('L')
            dist = hist.compare(hist0)

            if dist > 20000:
                key_frame = frame
                contours = element.detect(key_frame)
                hist0 = hist

            elements.append((frame, contours))

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

    def write(self, frames, path, codec=None, framerate=None, dimension=None):

        codec = codec if codec else self.codec
        framerate = framerate if framerate else self.framerate
        dimension = dimension if dimension else self.dimension

        with Writer(path, codec, framerate, dimension) as vw:
            vw.write(frames)

    def read(self):
        """
        Reads all frames from the video file.
        :return: List of Image objects.
        """

        frames = []

        while True:
            ret, frame = self.cap.read()

            if ret is False:
                break

            frames.append(Image(frame))

        return frames


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