import os
import sys


class TestFileHelper(object):
    """
    Класс-примесь к тестам, помогает искать файлы данных относительно файла класса.

    Упрощает указание имён файлов для тестов, при поиске не использует текущий каталог.
    Предполагается, что файлы хранятся в 'каталоге данных', положение которого относительно класса тестов не меняется.
    Метод _test_file конструирует имя файла из частей, отсчитывая путь от 'каталоге данных'.
    По умолчанию каталог данных - это кодкаталог 'test_data' от класса тестов.

    Импользование:
    class MyTestSuit(unittest.TestCase, TestFileHelper):
        def test_file1(self):
            test_file_name = self._test_file('test_file_1.data')
            self.assertTrue(do_test(file_name=test_file_name))
    """

    # резервируем имя в классе, во избежание AttributeError при первом обращении
    _test_class_path = None

    @staticmethod
    def _data_subdir() -> str:
        """
        Относительный путь к каталогу данных.

        Путь считается относительно каталога с классом исполняемого теста.
        Класс тестов при необходимости может перекрыть данный метод и вернуть альтернативный путь.

        :return: относительный путь к каталогу
        """
        return 'test_data'

    def __get_test_class_path(self) -> str:
        """
        Путь к каталогу с классом теста.

        Относительно этого каталога вычисляется путь к файлу с тестовыми данными.
        :return: путь к каталогу
        """
        self_class = self.__class__
        path = self_class._test_class_path
        if path is None:
            module_name = self_class.__module__
            module_file = sys.modules[module_name].__file__
            path = os.path.dirname(module_file)
            self_class._test_class_path = path
        return path

    def _test_file(self, *names: str) -> str:
        """
        Строит путь к файлу с тестовыми данными.

        Строит путь к файлу относительно каталога с данными.
        Каталог с данными - это каталог с файлами данных для тестов.
        Предпологается, что каталог с данными находится рядом с файлом пекета тестов.
        По умолчанию это подкаталог 'test_data', подробнее смотри _data_subdir().

        Дополнительное преимущество метода - возможность получить путь к файлу не используя разделители.
        Если в строке задать путь в стиле Windows - с обратными слешами, то под Linux он не будет восприниматься правильно.
        В обратную сторону работает автоматическое преобразование.

        :param names: части пути и имя файла
        :return: путь к файлу
        """
        class_path = self.__get_test_class_path()
        data_subdir = self._data_subdir()
        full_path = os.path.join(class_path, data_subdir, *names)
        return os.path.normpath(full_path)
