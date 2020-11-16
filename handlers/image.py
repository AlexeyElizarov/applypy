from handlers.base import BaseHandler
from handlers.metrics import MetricsHandler
from handlers.mode import ModeHandler


class ImageHandler(BaseHandler):

    @property
    def mode(self):
        return ModeHandler(self._obj)

    @property
    def metrics(self):
        return MetricsHandler(self._obj)