import unittest

from image import read


class TestFileHelper(object):

    def _data_subdir(self):
        return 'test_data'

    def _test_file(self, *names: str) -> str:
        import os
        class_path = os.path.dirname(__file__)
        data_subdir = self._data_subdir()
        full_path = os.path.join(class_path, data_subdir, *names)
        return os.path.normpath(full_path)


class ReadImage(unittest.TestCase, TestFileHelper):
    ref_size = 9133995

    def test_valid_path(self):
        # Test a valid image path
        test_file_name = self._test_file('test_read_image.jpg')
        self.assertTrue(read(test_file_name).size == self.ref_size)

    def test_invalid_path(self):
        # Test an invalid image path
        test_file_name = self._test_file('foo.jpg')
        with self.assertRaises(FileNotFoundError):
            read(test_file_name)

    def test_cyrillic_filename(self):
        # Test cyrillic filename
        test_file_name = self._test_file('изображение.jpg')
        self.assertTrue(read(test_file_name).size == self.ref_size)

    def test_cyrillic_path(self):
        # Test cyrillic filename
        test_file_name = self._test_file('изображения', 'изображение.jpg')
        self.assertTrue(read(test_file_name).size == self.ref_size)


if __name__ == '__main__':
    unittest.main()