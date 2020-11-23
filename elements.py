from abc import abstractmethod

from cv2.cv2 import inRange, bitwise_and, morphologyEx, MORPH_OPEN, MORPH_CLOSE, cvtColor, COLOR_RGB2GRAY, \
    findContours, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE, boundingRect
from numpy import ones, uint8, array

from image import Image


class BaseElement:

    @staticmethod
    def calculate_color_range(color: tuple, k: tuple) -> tuple:
        """
        Calculates lower and upper color boundary used in contour detection.
        :param color: RGB color tuple.
        :param k: tuple of coefficients for lower and upper limits (e.g. (0.5, 0.3))
        :return: lower and upper color boundary.
        """
        lower_k, upper_k = k
        lower = array([int(round(c * (1 - lower_k), 0)) for c in color])
        upper = array([int(round(c * (1 + upper_k), 0)) for c in color])
        return lower, upper

    def find_contours(self, image: Image, color: tuple, k: tuple, kernel: int) -> list:
        """
        Finds external contours with given color coefficients and kernel.
        :param color: RGB color tuple.
        :rtype: object
        :type image: Image object
        :param k: tuple of coefficients for lower and upper color boundary.
        :param kernel: kernel size.
        :return: list of contours.
        """
        lower, upper = self.calculate_color_range(color, k)
        mask = inRange(image, lower[::-1], upper[::-1])
        tmp = 255 * bitwise_and(image, image, mask=mask)
        kernel = ones((kernel, kernel), uint8)
        tmp = morphologyEx(tmp, MORPH_OPEN, kernel)
        tmp = morphologyEx(tmp, MORPH_CLOSE, kernel)
        tmp = cvtColor(tmp, COLOR_RGB2GRAY)
        tmp, contours, hierarchy = findContours(tmp, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE)
        return contours

    @abstractmethod
    def detect(self, *args):
        """Implement detection logic here."""
        pass


class TestElement(BaseElement):

    def detect(self, *args):
        pass


class TelegramNotificationElement(BaseElement):
    _COLOR = 22, 32, 41
    _X = 1594
    _PRIMARY_NOTIFICATION = 320, 80
    _SECONDARY_NOTIFICATION = 320, 36

    @staticmethod
    def _area(w: int, h: int) -> int:
        """
        Calculates the area of the rectangle
        :param w: width
        :param h: height
        :return: rectangle area.
        """
        return w * h

    def detect(self, image: Image, k: tuple, kernel: int) -> list:
        """
        Returns the list of notification pop-ups using TelegramNotification parameters.
        :param kernel: kernel size.
        :param k: tuple of coefficients for lower and upper color boundary.
        :type image: Image object
        """

        notifications = []
        contours = self.find_contours(image, self._COLOR, k, kernel)

        # Find primary notification pop-up
        if contours:
            for contour in contours:
                x, y, w, h = boundingRect(contour)
                if w * h == self._area(*self._PRIMARY_NOTIFICATION) and x == self._X:
                    notifications.append((x, y, w, h))

        # Find secondary notification pop-up
        if notifications:
            for contour in contours:
                x, y, w, h = boundingRect(contour)
                if w * h == self._area(*self._SECONDARY_NOTIFICATION) and x == self._X:
                    notifications.append((x, y, w, h))

        return notifications