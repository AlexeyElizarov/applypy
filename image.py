from os import mkdir
from os.path import exists, dirname

from cv2 import imread, imwrite
from numpy import ndarray, asarray

from handler import ImageHandler


class Image(ndarray):

    """This class represents an Image object"""

    def __new__(cls, input_array):
        # http://docs.scipy.org/doc/numpy/user/basics.subclassing.html#slightly-more-realistic-example-attribute-added-to-existing-array
        obj = asarray(input_array).view(cls)
        obj._handler = ImageHandler(obj)
        return obj

    def __array_finalize__(self, obj):

        if obj is None:
            return

        self._handler = getattr(obj, '_handler', None)

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
    def metrics(self):
        return self._handler.metrics

    @property
    def filter(self):
        return self._handler.filter

    @staticmethod
    def create(array):
        """Creates an Image object from the array"""
        return Image(array)


def read(path: str):
    """
    Loads an image from the specified file and returns Image object. If the image cannot be
    read (because of missing file, improper permissions, unsupported or invalid format), the function
    raises FileNotFound exception.
    :param path: input path.
    :return: Image object or False.
    """

    if exists(path):
        return Image(imread(path))
    else:
        raise FileNotFoundError


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

    return imwrite(path, image)