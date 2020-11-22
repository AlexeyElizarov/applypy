from cv2 import cvtColor, COLOR_BGR2GRAY, GaussianBlur
from skimage.metrics import mean_squared_error


class BaseHandler:
    """Base class for media handlers"""

    def __init__(self, obj):
        self._obj = obj


class FrameHandler(BaseHandler):

    def read(self, frame_num):
        """
        Reads a frame from the video file by its number.
        :return: Image object
        """

        self._obj.cap.set(1, frame_num)
        ret, frame = self._obj.cap.read()

        return self._obj.create_image(frame)

    def extract(self, threshold=0):
        """
        Extracts frames from the video file with the given MSE threshold.
        If threshold not provided, than all frames will be extracted
        :param threshold: MSE threshold.
        :return: list of frames.
        """

        frames = []
        base_frame = self._obj.frames.read(0)
        frames.append(base_frame)

        for i in range(1, self._obj.length):
            frame = self._obj.frames.read(i)
            mse = frame.metrics.mse(base_frame)
            if mse >= threshold:
                frames.append(frame)
                base_frame = frame

        return frames


class VideoHandler(BaseHandler):

    @property
    def frames(self):
        return FrameHandler(self._obj)


class ImageHandler(BaseHandler):

    @property
    def mode(self):
        return ImageMode(self._obj)

    @property
    def metrics(self):
        return ImageMetrics(self._obj)

    @property
    def filter(self):
        return ImageFilter(self._obj)


class ImageBlur(BaseHandler):

    def gaussian(self, kernel_size, sigma_x, *args, region: tuple = None):
        """
        Smooths a rectangle area of the image using Gaussian  blur.
        :param sigma_x: Gaussian kernel standard deviation in X direction.
        :param kernel_size: Gaussian kernel size. kernel_size.width and kernel_size.height can differ but they both must be
        positive and odd. Or, they can be zero's and then they are computed from sigma.
        :param region: a tuple of top left and bottom right points of the smoothing area.
        The whole image will smoothed if not provided.
        :return: smoothed image.
        """

        if not region:
            top_left, bottom_right = (0, 0), (self._obj.width, self._obj.height)
        else:
            top_left, bottom_right = region

        smoothed = self._obj.copy()
        smoothed_region = smoothed[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
        smoothed_region = GaussianBlur(smoothed_region, kernel_size, sigma_x, *args)
        smoothed[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]] = smoothed_region

        return self._obj.create(smoothed)


class ImageFilter(BaseHandler):

    @property
    def blur(self):
        return ImageBlur(self._obj)


class ImageMode(BaseHandler):
    """ Implements color mode conversions."""

    def to_greyscale(self):
        """Convert to grey scale"""
        array = cvtColor(self._obj, COLOR_BGR2GRAY)
        return self._obj.create(array)


class ImageMetrics(BaseHandler):

    def mse(self, image) -> float:

        """
        Compute the mean-squared error between two images.
        :param image: Image to compare, must have same shape.
        :return: the mean-squared error (MSE) metric.
        """

        img1 = self._obj.mode.to_greyscale()
        img2 = image.mode.to_greyscale()

        return mean_squared_error(img1, img2)