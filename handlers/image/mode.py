from cv2 import cvtColor, COLOR_BGR2GRAY

from handlers import Handler
from image import Image


class Mode(Handler):
    """ Implements color mode conversions."""

    def to_greyscale(self):
        """Convert to greyscale."""
        return Image(cvtColor(self._obj, COLOR_BGR2GRAY))