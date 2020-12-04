from cv2.cv2 import boundingRect
from numpy import asarray, ndarray


class Contour(ndarray):

    def __new__(cls, input_array):
        obj = asarray(input_array).view(cls)
        return obj

    @property
    def rectangle(self):
        """
        Calculates the up-right bounding rectangle of a point set or non-zero pixels of gray-scale image.
        :return: x, y of the rectangle top-left point, rectangle width and height.
        """
        return boundingRect(self)
