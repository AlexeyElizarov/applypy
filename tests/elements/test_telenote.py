import unittest

import image
from elements import TelegramNotificationElement
from helpers import TestFileHelper
from pallet import GREEN


class TeleNote(unittest.TestCase, TestFileHelper):

    element = TelegramNotificationElement()

    def test_detect(self):

        img = image.read(self._test_file('telenote', 'test_telenote_00.png'))
        elements = self.element.detect(img, k=(0.5, 0.5), kernel=5)

        for element in elements:
            img = img.draw.contours(element, color=GREEN)

        img.show()


if __name__ == '__main__':
    unittest.main()
