import cv2
import numpy as np
from skimage.metrics import mean_squared_error

from handlers.image import Mode


class Image(np.ndarray):
    """Implements additional methods to process the Image as ndarray."""

    def __new__(cls, input_array):
        # http://docs.scipy.org/doc/numpy/user/basics.subclassing.html#slightly-more-realistic-example-attribute-added-to-existing-array
        obj = np.asarray(input_array).view(cls)
        return obj

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
        return Mode(self)

    def compare(self, image) -> float:
        """
        Compute the mean-squared error between two images.
        :param image: Image to compare, must have same shape.
        :return: the mean-squared error (MSE) metric.
        """
        img1 = cv2.cvtColor(self, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        return mean_squared_error(img1, img2)

    def smooth(self, region: tuple = None, k_size=(99, 99), sigma_x=0, *kwargs):
        """
        Smooths the rectangle area of the image using Gaussian  blur.
        :param sigma_x: Gaussian kernel standard deviation in X direction.
        :param k_size: Gaussian kernel size. ksize.width and ksize.height can differ but they both must be
    .   positive and odd. Or, they can be zero's and then they are computed from sigma.
        :type region: a tuple of top left and bottom right coordinates of the rectangle region.
        """

        if region:
            top_left, bottom_right = region
        else:
            top_left, bottom_right = (0, 0), (self.shape[1], self.shape[0])

        try:
            rect = self[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
            rect = cv2.GaussianBlur(rect, k_size, sigma_x, kwargs)
            self[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]] = rect
        except Exception as e:
            raise e
