from os.path import exists

import cv2

from image.base import Image


class Reader:

    def __init__(self, path):

        if exists(path):
            self._path = path
        else:
            raise FileNotFoundError

    def __enter__(self):
        self._capture = cv2.VideoCapture(self._path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._capture.release()

    def __len__(self):
        return int(self._capture.get(cv2.CAP_PROP_FRAME_COUNT))

    def read_frame(self, frame_num: int):
        """
        Reads a frame from the video file by its number.
        :return: Image object
        """

        self._capture.set(1, frame_num)
        ret, frame = self._capture.read()

        return Image(frame)