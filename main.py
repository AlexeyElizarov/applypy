from cv2.cv2 import boundingRect

from video import Video
from elements import TelegramNotificationElement


def baseline(input_video, output_video):
    """Baseline scenario is to detect Telegram Notifications in the video file and blur them out."""

    element = TelegramNotificationElement()

    with Video(input_video) as video:
        frames = []
        elements = video.detect(element)
        # elements is the list of tuples of frame number and element contour

        for element in elements:

            frame_num, contours = element
            frame = video.frames.read(frame_num)

            for contour in contours:
                x, y, w, h = contour.rectangle
                region = (x, y), (x + w, y + h)
                frame = frame.filter.blur(kernel_size=(99, 99), sigma_x=0, region=region)

            frames.append((frame_num, frame))

        # frames is the list of tuples of frame number and frame to be replaced in the input video
        # TODO: video.write() to be implemented
        video.write(output_video, frames, codec=video.codec, bitrate=video.framerate, dimension=video.dimension)


if __name__ == '__main__':

    video_in = r""
    video_out = r""

    baseline(video_in, video_out)

