from handlers.base import BaseHandler
from handlers.mode import ModeHandler


class ImageHandler(BaseHandler):

    @property
    def mode(self):
        return ModeHandler(self._obj)