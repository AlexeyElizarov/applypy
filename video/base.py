# from os.path import join
#
# import cv2
# from tqdm import tqdm
#
# import image
from video.reader import Reader


class Video(Reader):
    pass

    # def __init__(self, frames):
    #     self.frames = frames
    #
    # def __len__(self):
    #     return len(self.frames)

    # def __init__(self, path):
    #     self._path = path
    #
    # def __enter__(self):
    #     self._cap = cv2.VideoCapture(self._path)
    #     return self
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self._cap.release()
    #
    # @property
    # def frames(self):
    #     return [self.read_frame(i) for i in range(self.length + 1)]
    #
    # @property
    # def length(self):
    #     return int(self._cap.get(cv2.CAP_PROP_FRAME_COUNT))
    #
    # def read_frame(self, frame_num: int):
    #     """
    #     Reads a frame from the video file by its number.
    #     :return: Frame object
    #     """
    #
    #     self._cap.set(1, frame_num)
    #     ret, frame = self._cap.read()
    #
    #     return frame
    #     # return Frame(frame, frame_num)
    #
    # def extract_key_frames(self, path, step: int = 1, threshold: float = 1000):
    #     """
    #     Extracts key frames from the video file.
    #     :param path: output location.
    #     :param step: frame step.
    #     :param threshold: MSE threshold.
    #     :return: None
    #     """
    #
    #     _frame = None
    #
    #     for i in tqdm(range(0, self.length + 1, step)):
    #
    #         frame = self.read_frame(i)
    #         location = join(path, frame.file_name)
    #         mse = threshold + 1 if i == 0 else frame.compare(_frame)
    #
    #         if mse >= threshold:
    #             image.write(location, frame)
    #             _frame = frame
