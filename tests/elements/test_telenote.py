import unittest

import image
from elements import TelegramNotificationElement


class TeleNote(unittest.TestCase):

    element = TelegramNotificationElement()

    def test_detect(self):

        img = image.read(r"D:\Videos\Screenbits\SAP Summit 2020\Stocks\_tests\contours\_test_contours_01\frame_0000.png")
        elements = self.element.detect(img, k=(0.4, 0.4), kernel=5)

        for element in elements:
            img = img.draw.rectangle(*element, color=(0, 255, 0))

        image.write(r'.\test_data\test_telenote_0.png', img)


if __name__ == '__main__':
    unittest.main()
