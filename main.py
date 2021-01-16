from cv2.cv2 import boundingRect

from video import Video
from elements import TelegramNotificationElement


def baseline(input_video, output_video):
    """Baseline scenario is to detect Telegram Notifications in the video file and blur them out."""

    element = TelegramNotificationElement()

    with Video(input_video) as video:
        frames = []
        print('detect')
        elements = video.detect(element)
        # elements is the list of tuples of frame and element contour

        print('apply filter')
        for element in elements:

            frame, contours = element

            for contour in contours:
                x, y, w, h = contour.rectangle
                region = (x, y), (x + w, y + h)
                frame = frame.filter.blur.gaussian(kernel_size=(99, 99), sigma_x=0, region=region)

            frames.append(frame)

        # frames is the list of tuples of frame number and frame to be replaced in the input video
        # TODO: video.write() to be implemented
        print('write')
        video.write(frames, output_video, codec=video.codec, framerate=video.framerate, dimension=video.dimension)


if __name__ == '__main__':

    video_in = r"D:\Videos\Screenbits\SAP Summit 2020\Stocks\_tests\contours\test_contours_03.mp4"
    video_out = r"D:\Videos\Screenbits\SAP Summit 2020\Stocks\_tests\contours\test_contours_03_out.mp4"

    baseline(video_in, video_out)

