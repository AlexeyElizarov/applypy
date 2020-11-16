from handlers import ImageHandler


class Image:

    """This class represents an Image object"""

    def __init__(self, array):
        self.array = array
        self._handler = ImageHandler(self)

    @property
    def size(self):
        return self.array.size

    @property
    def height(self):
        return self.array.shape[0]

    @property
    def width(self):
        return self.array.shape[1]

    @property
    def channels(self):
        try:
            return self.array.shape[2]
        except IndexError:
            return 0

    @property
    def mode(self):
        return self._handler.mode

    @property
    def metrics(self):
        return self._handler.metrics