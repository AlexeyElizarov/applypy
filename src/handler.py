from cv2 import cvtColor, COLOR_BGR2GRAY, GaussianBlur, rectangle, drawContours, circle, calcHist
from histogram import Histogram
from skimage.metrics import mean_squared_error


class BaseHandler:
    """Base class for media handlers"""

    def __init__(self, obj):
        self._obj = obj


class FrameHandler(BaseHandler):

    def get(self, frame_num):
        """
        Gets a single frame from the video file by its number.
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


class ImageDraw(BaseHandler):

    def rectangle(self, top_left: tuple, bottom_right: tuple, color: tuple, thickness: int = 1, filled: bool = False):
        """
        Draws a simple, thick, or filled up-right rectangle.
        :param filled: If True then the function has to draw a filled rectangle.
        :param top_left: Top-left coordinates of the rectangle.
        :param bottom_right: Bottom-right coordinates of the rectangle
        :param color: Rectangle color or brightness (grayscale image).
        :param thickness: Thickness of lines that make up the rectangle.
        Negative values, like FILLED, mean that the function has to draw a filled rectangle.
        :return: Image object.
        """

        img = self._obj.copy()

        if filled:
            thickness = -1

        return self._obj.new(rectangle(img, top_left, bottom_right, color[::-1], thickness))

    def contours(self, contours, contour_id: int = None, color: tuple = (255, 255, 255)):
        """
        Draws contours outlines or filled contours.
        :param contours: All the input contours. Each contour is stored as a point vector.
        :param contour_id: Parameter indicating a contour to draw. If not specified, all contours will be drawn.
        :param color: Color of the contours. White by default.
        :return: Image object.
        """

        img = self._obj.copy()

        if contour_id is None:
            contour_id = -1

        return self._obj.new(drawContours(img, contours, contour_id, color[::-1]))

    def circle(self, center, radius, color: tuple = (255, 255, 255), thickness: int = 1, filled: bool = False):
        """
        Draws a circle.
        :param center:	Center of the circle.
        :param radius: 	Radius of the circle.
        :param color: Circle color.
        :param thickness: Thickness of the circle outline
        :param filled: If True, filled circle to be drawn.
        :return: Image object.
        """

        img = self._obj.copy()

        if filled:
            thickness = -1

        return self._obj.new(circle(img, center, radius, color[::-1], thickness))


class ImageHandler(BaseHandler):

    @property
    def draw(self):
        return ImageDraw(self._obj)

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
        :param kernel_size: Gaussian kernel size. kernel_size.width and kernel_size.height can differ
        but they both must be positive and odd. Or, they can be zero's and then they are computed from sigma.
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

        return self._obj.new(smoothed)


class ImageFilter(BaseHandler):

    @property
    def blur(self):
        return ImageBlur(self._obj)


class ImageMode(BaseHandler):
    """ Implements color mode conversions."""

    def to_greyscale(self):
        """Convert to grey scale"""
        array = cvtColor(self._obj, COLOR_BGR2GRAY)
        return self._obj.new(array)


class ImageMetrics(BaseHandler):

    def histogram(self, channels):
        """
        Returns Histogram object
        :param channels: color channel to build histogram. Could be R for red, G for green, B for blue,
        L for luminosity (greyscale).
        :return: Histogram object
        """
        return Histogram(self._obj, channels)

    def mse(self, image, roi) -> float:

        """
        Compute the mean-squared error between two images.
        :param image: Image to compare, must have same shape.
        :return: the mean-squared error (MSE) metric.
        """

        img1 = self._obj
        img2 = image

        if roi:
            x_roi, y_roi = roi
            img1 = self._obj.set_roi(self._obj.width * x_roi, self._obj.height * y_roi)
            img2 = image.set_roi(image.width * x_roi, image.height * y_roi)

        img1 = self._obj.mode.to_greyscale()
        img2 = image.mode.to_greyscale()

        return mean_squared_error(img1, img2)