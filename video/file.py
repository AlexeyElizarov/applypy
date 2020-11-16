#
#
# """
# Implements read/write functions to handle videos.
# """
# from os.path import exists
#
# import cv2
# from tqdm import tqdm
#
# from video.reader import Reader
# from video.base import Video
#
#
# def read(path: str):
#     """
#     Reads a video file at specific location and returns Video object. If the video file cannot be
#     read (because of missing file, improper permissions, unsupported or invalid format), the function
#     raises FileNotFound exception.
#     :param path: input path.
#     :return: Video object.
#     """
#     with open
#
#     if exists(path):
#         with Reader(path) as video:
#             return Video(video.frames)
#     else:
#         raise FileNotFoundError


# def write(frames, path, codec, bitrate, dimension):
#
#     """
#     Saves the video to the specified path.
#     :return: true if the image has been saved successfully.
#     """
#
#
#     out = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*codec), bitrate, dimension)
#
#     for frame in tqdm(frames, "Writing..."):
#         out.write(frame)
#
#     out.release()