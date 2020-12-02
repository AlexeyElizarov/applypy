from video import Video
from elements import TelegramNotificationElement


def baseline(input_video, output_video):
    """Baseline scenario is to detect Telegram Notifications in the video file and blur them."""

    element = TelegramNotificationElement()

    with Video(input_video) as video:
        frames = []
        elements = video.detect(element)
        # elements is the list of tuples of frame number and element contour

        for element in elements:

            frame_num, contour = element
            frame = video.frames.read(frame_num)
            frame = frame.filter.blur(contour)
            frames.append((frame_num, frame))

        # frames is the list of tuples of frame number and frame to be replaced in the input video
        video.write(output_video, frames, codec=video.codec, bitrate=video.bitrate, dimension=video.dimension)


if __name__ == '__main__':

    video_in = r".\_unit_tests\video\test_data\test_video_read.mp4"
    video_out = r".\_unit_tests\video\test_data\test_video_write.mp4"

    baseline(video_in, video_out)

