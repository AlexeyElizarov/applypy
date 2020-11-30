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
        raise FileNotFoundError

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

    if not exists(dir_name):
        mkdir(dir_name)

    ext = splitext(path)[1]
    retcode, nbuffer = cv2.imencode(ext, image)
    chunk = nbuffer.tobytes()

    with open(path, "wb") as file:
        file.write(chunk)

    return retcode
