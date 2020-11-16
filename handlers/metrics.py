from skimage.metrics import mean_squared_error

from handlers.base import BaseHandler


class MetricsHandler(BaseHandler):

    def mse(self, image) -> float:

        """
        Compute the mean-squared error between two images.
        :param image: Image to compare, must have same shape.
        :return: the mean-squared error (MSE) metric.
        """
        img1 = self._obj.mode.to_greyscale()
        img2 = image.mode.to_greyscale()

        return mean_squared_error(img1.array, img2.array)