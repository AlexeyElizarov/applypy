# import cv2
#
#
# class Writer:
#
#     def __init__(self, path, codec, bitrate, dimension):
#         self._path = path
#         self._codec = codec
#         self._bitrate = bitrate
#         self._dimension = dimension
#
#     def __enter__(self):
#         self._writer = cv2.VideoWriter(self._path, self._codec, self._bitrate, self._dimension)
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self._writer.release()