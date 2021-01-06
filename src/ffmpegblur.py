from pathlib import PurePath
from typing import List, Dict, Any

import ffmpeg


def _calc_size(values_dict, start_name, end_name, size_name):
    """ Получает из параметров настроенный диапазон

    Получает из словаря значения для вычисления положения и размера диапазона.
    Диапазон может быть задан комбинацией любых двух параметров из трёх:
        - начало
        - конец
        - длина
    Отсутствие двух параметров считается ошибкой.
    Если заданы все три, то берутся значения начала и длины, значение конца не анализируется.
    Тип значений не проверяется.

    :param values_dict: Словарь значений
    :param start_name: имя параметра начала диапазона
    :param end_name: имя параметра конца диапазона
    :param size_name: имя параметра длины диапазона
    :return: начало и длина диапазона
    :raise ValueError: если отсутствует более двух параметров
    """
    start = values_dict.get(start_name)
    end = values_dict.get(end_name)
    size = values_dict.get(size_name)

    if start is None:
        if end is None:
            raise ValueError(f"Не заданы {start_name} и {end_name}")
        if size is None:
            raise ValueError(f"Не заданы {start_name} и {size_name}")
        start = end - size

    if size is None:
        if end is None:
            raise ValueError(f"Не заданы {size_name} и {end_name}")
        size = end - start

    return start, size


def blur_softly(matrix: List[Dict[str, Any]], video_in, video_out=""):
    """ Запускает обработку видео через ffmpeg

    Обработываемых областей может быть несколько, они могут пересекаться по координатам и времени.
    Для непересекающихся областей порядок их следования в массиве не имеет значения.
    Параметры разных областей друг на друга не влияют, массив и словари не модифицируются при работе.

    Если путь к результату не задан, то он помещается рядом с исходным файлом, с припиской к имени "_blurred".

    Обрабатываемая область описывается тремя диапазонами: ширина, высота и продолжительносью, и двумя параметрами обработки: радиусом и степенью.
    Ширина может быть задана любыми двумя параметрами из списка: 'left', 'right', 'width'
    Высота может быть задана любыми двумя параметрами из списка: 'top', 'bottom', 'height'
    Продолжительность тоже задаётся двумя параметрами, но их имена и значения зависят от желаемого спасоба измерения времени.

    Для задания продолжительности можно использовать разные единицы измерения: секунды или кадры.
    Секунды могут быть дробными, задаются в виде чисел с плавающей точкой.
    Продолжительность в секундах задаётся любыми двумя параметрами из списка: 'timestart', 'timeend', 'length'
    Кадры могут быть только целыми, начальный кадр имеет номер 0.
    Продолжительность в кадрах задаётся любыми двумя параметрами из списка: 'framestart', 'frameend', 'length'

    Радиус размытия по умолчанию ставится как четверть от меньшего из размеров области.
    Задать его явно можно через параметр 'radius'.
    При превышении допустимого значения ffmpeg откажется от работы и выведет соответствующее сообщение.

    Степень размытия задаётся через параметр 'power'.
    По умолчанию его значение 5.

    :param matrix: список областей обработки
    :param video_in: путь к исходному видео
    :param video_out: путь к результату
    """
    input_file = ffmpeg.input(video_in)

    source_stream = input_file.video
    st0 = source_stream

    for d in matrix:
        top, height = _calc_size(d, 'top', 'bottom', 'height')
        left, width = _calc_size(d, 'left', 'right', 'width')
        if 'timestart' in d or 'timeend' in d:
            start, length = _calc_size(d, 'timestart', 'timeend', 'length')
            time_unit = 't'
        else:
            start, length = _calc_size(d, 'framestart', 'frameend', 'length')
            time_unit = 'n'

        radius = d.get('radius')
        if radius is None:
            radius = min(width, height) / 4
        power = d.get('power')
        if power is None:
            power = 5

        enable = f'between({time_unit},{start},{start + length})'

        st1 = ffmpeg.crop(source_stream, left, top, width, height)
        st2 = ffmpeg.filter_(st1, 'boxblur', lr=radius, lp=power, enable=enable)
        st0 = ffmpeg.overlay(st0, st2, x=left, y=top, enable=enable)

    if video_out == "":
        video_in = PurePath(video_in)
        video_out = str(video_in.parent.joinpath(video_in.stem + "_blurred" + video_in.suffix))

    output = ffmpeg.output(st0, input_file.audio, video_out,
                           vcodec='libx264',
                           acodec='copy',
                           crf=17,
                           preset='fast',
                           tune='stillimage')

    ffmpeg.run(output, overwrite_output=True)
