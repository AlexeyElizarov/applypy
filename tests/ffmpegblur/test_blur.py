from ffmpegblur import blur_softly


class TestFFMPEGBlur:
    def test_case_1(self):
        video_in = r"D:\test_contours_01.mp4"
        # video_in = "test_contours_01.mp4"
        blur_softly([
            {'timestart': 0, 'timeend': 170, 'top': 952, 'bottom': 1033, 'left': 1592, 'right': 1915, 'blur': 20}
        ], video_in)


if __name__ == '__main__':
    TestFFMPEGBlur().test_case_1()
