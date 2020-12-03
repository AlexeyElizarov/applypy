import unittest

from elements import TestElement

from numpy import array


class ColorRange(unittest.TestCase):

    color = 128, 128, 128
    k0 = 0
    k1 = 1
    k2 = 0.5

    def test_color_range_k0(self):
        test_range = TestElement.calculate_color_range(self.color, (self.k0, self.k0))
        reference_range = (array([128, 128, 128]), array([128, 128, 128]))

        test_top, test_bottom = test_range
        reference_top, reference_bottom = reference_range

        comparison_top = test_top == reference_top
        comparison_bottom = test_bottom == reference_bottom
        self.assertTrue(comparison_top.all())
        self.assertTrue(comparison_bottom.all())

    def test_color_range_k1(self):
        test_range = TestElement.calculate_color_range(self.color, (self.k1, self.k1))
        reference_range = (array([0, 0, 0]), array([256, 256, 256]))

        test_top, test_bottom = test_range
        reference_top, reference_bottom = reference_range

        comparison_top = test_top == reference_top
        comparison_bottom = test_bottom == reference_bottom
        self.assertTrue(comparison_top.all())
        self.assertTrue(comparison_bottom.all())

    def test_color_range_k2(self):
        test_range = TestElement.calculate_color_range(self.color, (self.k2, self.k2))
        reference_range = (array([int(128*0.5), int(128*0.5), int(128*0.5)]),
                           array([int(128*1.5), int(128*1.5), int(128*1.5)]))

        test_top, test_bottom = test_range
        reference_top, reference_bottom = reference_range

        comparison_top = test_top == reference_top
        comparison_bottom = test_bottom == reference_bottom
        self.assertTrue(comparison_top.all())
        self.assertTrue(comparison_bottom.all())


if __name__ == '__main__':
    unittest.main()
