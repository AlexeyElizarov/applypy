from abc import abstractmethod

from cv2.cv2 import inRange, bitwise_and, morphologyEx, MORPH_OPEN, MORPH_CLOSE, cvtColor, COLOR_RGB2GRAY, \
    findContours, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE, boundingRect
from numpy import ones, uint8, array

from contours import Contour
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

    def find_contours(self, image: Image, color: tuple, k: tuple = (0, 0), kernel: int = 0,
                      offset=None) -> list:
        """
        Finds external contours with given color coefficients and kernel.
        :param offset: offset by which every contour point is shifted.
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
        tmp, contours, hierarchy = findContours(tmp, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE, offset=offset)

        return [Contour(contour) for contour in contours]

    @abstractmethod
    def detect(self, *args):
        """Implement detection logic here."""
        pass


class TelegramNotificationElement(BaseElement):
    """
    Telegram notification is a solid rectangle area of the specific color range.
    The notification always pops up at specific X coordinate at the bottom right corner of the screen.
    Notifications come in two types of the specific width and height: primary and secondary.
    Secondary notification pops up only if there's at least one primary notification on the screen.
    """

    _COLOR = 22, 32, 41
    _X = 1594
    _PRIMARY_NOTIFICATION = 320, 80
    _SECONDARY_NOTIFICATION = 320, 36
    _ROI = None

    @staticmethod
    def _area(w: int, h: int) -> int:
        """
        Calculates the area of the rectangle
        :param w: width
        :param h: height
        :return: rectangle area.
        """
        return w * h

    def detect(self, image: Image, k: tuple = (0.4, 0.4), kernel: int = 5, offset=None) -> list:
        """
        Returns the list of notification pop-ups using TelegramNotification parameters.
        :param offset: offset by which every contour point is shifted.
        :param kernel: kernel size.
        :param k: tuple of coefficients for lower and upper color boundary.
        :type image: Image object
        """

        if self._ROI:
            x_roi, y_roi = self._ROI
            roi = image.set_roi(image.width * x_roi, image.height * y_roi)
            offset = roi.width, roi.height
        else:
            roi = image

        contours = self.find_contours(roi, self._COLOR, k, kernel, offset=offset)
        elements = []

        # Find primary notification pop-up
        if contours:
            for contour in contours:
                x, y, w, h = contour.rectangle
                if w * h == self._area(*self._PRIMARY_NOTIFICATION) and x == self._X:
                    elements.append(contour)

        # Find secondary notification pop-up
        if elements:
            for contour in contours:
                x, y, w, h = contour.rectangle
                if w * h == self._area(*self._SECONDARY_NOTIFICATION) and x == self._X:
                    elements.append(contour)

        return elements