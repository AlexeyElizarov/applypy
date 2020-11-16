from os import getcwd, mkdir, chdir
from os.path import dirname, basename, exists

from cv2 import imread, imwrite

from image import Image

"""
Implements read/write functions to handle images.
"""


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

    if dirname(path):
        dir_name = dirname(path)
    else:
        dir_name = getcwd()

    file_name = basename(path)

    if not exists(dir_name):
        mkdir(dir_name)

    chdir(dir_name)

    return imwrite(file_name, image)