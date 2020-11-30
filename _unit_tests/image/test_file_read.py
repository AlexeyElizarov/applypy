import unittest

from image import read


class TestFileHelper(object):
    _test_class_path = None

    @staticmethod
    def _data_subdir():
        return 'test_data'

    def __get_test_class_path(self):
        self_class = self.__class__
        path = self_class._test_class_path
        if path is None:
            import sys
            import os
            module_name = self_class.__module__
            module_file = sys.modules[module_name].__file__
            path = os.path.dirname(module_file)
            self_class._test_class_path = path
        return path

    def _test_file(self, *names: str) -> str:
        import os
        class_path = self.__get_test_class_path()
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
