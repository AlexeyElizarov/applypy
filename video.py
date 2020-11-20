from os.path import exists

from cv2.cv2 import VideoCapture, CAP_PROP_FRAME_COUNT


class Video:

    def __init__(self, path):
        self._path = path

    def __enter__(self):
        if exists(self._path):
            self._cap = VideoCapture(self._path)
            return self
        else:
            raise FileNotFoundError

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cap.release()

    @property
    def length(self):
        return int(self._cap.get(CAP_PROP_FRAME_COUNT))