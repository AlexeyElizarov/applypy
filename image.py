from os import getcwd, mkdir, chdir
from os.path import dirname, basename, exists

from cv2 import imread, imwrite

from handler import ImageHandler


class Image:

    """This class represents an Image object"""

    def __init__(self, array):
        self.array = array
        self._handler = ImageHandler(self)

    @property
    def size(self):
        return self.array.size

    @property
    def height(self):
        return self.array.shape[0]

    @property
    def width(self):
        return self.array.shape[1]

    @property
    def channels(self):
        try:
            return self.array.shape[2]
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


def write(path: str, image: Image) -> bool:
    """
    Saves the image to the specified path.
    :param image: Image object
    :param path: output path.
    :return: true if the image has been saved successfully.
    """

    dir_name = dirname(path)

    if not exists(dir_name):
        mkdir(dir_name)

    return imwrite(path, image.array)
