from os import mkdir
from os.path import exists, dirname, splitext

import cv2
import numpy

from handler import ImageHandler


class Image(numpy.ndarray):
    """This class represents an Image object"""

    def __new__(cls, input_array):
        # http://docs.scipy.org/doc/numpy/user/basics.subclassing.html#slightly-more-realistic-example-attribute-added-to-existing-array
        obj = numpy.asarray(input_array).view(cls)
        obj._handler = ImageHandler(obj)
        return obj

    def __array_finalize__(self, obj):

        if obj is None:
            return

        self._handler = getattr(obj, '_handler', None)

    def __str__(self):
        return super().__str__()

    def set_roi(self, x, y, w=None, h=None):
        """
        Sets region of interest.
        :param x: x-coordinate.
        :param y: y-coordinate.
        :param w: width of the region. Optional. (width - x) if not specified.
        :param h: height of the region. Optional. (height - y) if not specified.
        """
        x = int(x)
        y = int(y)
        w = w if w else self.width - x
        h = h if h else self.height - y
        return self[y:y + h, x:x + w]

    @property
    def height(self):
        return self.shape[0]

    @property
    def width(self):
        return self.shape[1]

    @property
    def channels(self):
        try:
            return self.shape[2]
        except IndexError:
            return 0

    @property
    def mode(self):
        return self._handler.mode

    @property
    def draw(self):
        return self._handler.draw

    @property
    def metrics(self):
        return self._handler.metrics

    @property
    def filter(self):
        return self._handler.filter

    def show(self):
        """Displays an image in the specified window."""

        cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('image', self)
        wait_time = 1000
        while cv2.getWindowProperty('image', 0) >= 0:
            key_code = cv2.waitKey(wait_time)
            if key_code & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

    @staticmethod
    def create(size: tuple, background=None):
        """Creates an Image of the specified size and background color"""

        w, h = size
        array = numpy.zeros((h, w, 3), numpy.uint8)

        if background is not None:
            array[::] = background[::-1]

        return Image(array)

    @staticmethod
    def new(array):
        """Creates an Image from the array"""
        return Image(array)


def read(path: str):
    """
    Loads an image from the specified file and returns Image object. If the image cannot be
    read (because of missing file, improper permissions, unsupported or invalid format), the function
    raises FileNotFound exception.
    :param path: input path.
    :return: Image object or False.
    """

    if not exists(path):
        from errno import ENOENT
        raise FileNotFoundError(ENOENT, 'File not found', path)

    with open(path, "rb") as file:
        chunk = file.read()

    nbuffer = numpy.frombuffer(chunk, dtype=numpy.uint8)
    img = cv2.imdecode(nbuffer, cv2.IMREAD_COLOR)

    return Image(img)


def write(path: str, image) -> bool:
    """
    Saves the image to the specified path.
    :param image: Image object
    :param path: output path.
    :return: true if the image has been saved successfully.
    """

    dir_name = dirname(path)

    if dir_name:
        if not exists(dir_name):
            mkdir(dir_name)

    ext = splitext(path)[1]
    retcode, nbuffer = cv2.imencode(ext, image)
    chunk = nbuffer.tobytes()

    with open(path, "wb") as file:
        file.write(chunk)

    return retcode
