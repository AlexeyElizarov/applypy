from image import Image


class Shot:

    def __init__(self, video, start_frame: int, end_frame: int = None):
        self._video = video
        self.start = start_frame
        self.end = end_frame if end_frame else self._video.length

    @property
    def length(self):
        return self.end - self.start

    @property
    def duration(self):
        return self.finish - self.begin

    @property
    def begin(self):
        return self.start / self._video.framerate

    @property
    def finish(self):
        return self.end / self._video.framerate

    def write(self, path):

        frames = []
        frame_num = 0

        while frame_num < self.end:
            ret, frame = self._video.cap.read()

            if frame_num >= self.start:
                frames.append(Image(frame))

            frame_num += 1

        self._video.write(frames, path)