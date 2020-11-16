from cv2 import cvtColor, COLOR_BGR2GRAY

from handlers.base import BaseHandler


class ModeHandler(BaseHandler):
    """ Implements color mode conversions."""

    def to_greyscale(self):
        """Convert to grey scale"""
        self._obj.array = cvtColor(self._obj.array, COLOR_BGR2GRAY)
        return self._obj