# import unittest
# from video import Video
#
#
# class OpenVideo(unittest.TestCase):
#
#     def test_open_valid_video_file(self):
#
#         with Video('test_video.mp4') as video:
#             self.assertGreater(len(video), 0)
#
#     def test_open_invalid_video_file(self):
#
#         with self.assertRaises(FileNotFoundError):
#             Video('foo')
#
#
# class WriteVideo(unittest.TestCase):
#
#     def test_write_video_file(self):
#
#         with Video('test_video.mp4') as video:
#             video.filter.blur.gaussian()
#             video.mode.to_greyscale()
#             video.mode.to_rgb()
#             video.mode.to_cmyk()
#             video.resize()
#             image.metrics.mse()
#
#             video.detect()
#
# if __name__ == '__main__':
#     unittest.main()
