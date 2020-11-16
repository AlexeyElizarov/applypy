import unittest
from image import read, write
from image.mode import Mode


class ModeConversions(unittest.TestCase):

    def test_mode(self):
        rgb_img = read(r'./test_data/test_rgb.png')
        self.assertIsInstance(rgb_img.mode, Mode)


    def test_to_greyscale(self):
        rgb_img = read(r'./test_data/test_rgb.png')
        gray_im = rgb_img.mode.to_greyscale()
        write(r'./test_data/test_greyscale.png', gray_im)

        for x in range(gray_im.width):
            for y in range(gray_im.hieght):
                r, g, b = gray_im[x][y]
                print(r, g, b)





if __name__ == '__main__':
    unittest.main()
