
def cg_distance(x1, y1, x2, y2, x3, y3, x4, y4) -> float:
    """
    Функция возвращающая расстояние между углами
    :param x1: левая верхняя x коорданата 1 прямоугольника
    :type x1: int
    :param y1 левая вехння y координата 1 прямоугольника
    :type y1: int
    :param x2: правая нижняя x координата 1 прямоугольника
    :type x2: int
    :param y2: правая нижняя y координата 1 прямоугольника
    :type y2: int
    :param x3: левая верхння x координата 2 прямоугольника
    :type x3
    :param y3: левая вехння y координата 2 прямоугольника
    :type y3: int
    :param x4: int правая нижняя x координата 2 прямоугольника
    :type x4: int
    :param y4: правая нижняя y координата 2 прямоугольника
    :type y4: int
    :return: расстояние между центрами прямоугольника
    :rtype: float
    :raise: TypeError when argument not number type

    """
    middle_side_a = (x2 + x1) / 2, (y1 + y2) / 2
    middle_side_b = (x3 + x4) / 2, (y4 + y3) / 2
    dist = (middle_side_b[0] - middle_side_a[0]) ** 2 + (middle_side_b[1] - middle_side_a[1]) ** 2
    return round(dist ** 0.5, 2)


def corner_distance(x1, y1, x2, y2, x3, y3, x4, y4) -> float:
    """
    Функция возвращающая расстояния между углами прямоугольников

    :param x1: левая верхняя x коорданата 1 прямоугольника
    :type x1: int
    :param y1 левая вехння y координата 1 прямоугольника
    :type y1: int
    :param x2: правая нижняя x координата 1 прямоугольника
    :type x2: int
    :param y2: правая нижняя y координата 1 прямоугольника
    :type y2: int
    :param x3: левая верхння x координата 2 прямоугольника
    :type x3
    :param y3: левая вехння y координата 2 прямоугольника
    :type y3: int
    :param x4: int правая нижняя x координата 2 прямоугольника
    :type x4: int
    :param y4: правая нижняя y координата 2 прямоугольника
    :type y4: int
    :return: расстояние между центрами прямоугольника
    :rtype: float
    :raise: TypeError when argument not number type

    """
    vector_a = x3 - x1, y3 - y1
    vector_b = x4 - x2, y4 - y2
    sum_vector = (vector_a[0] ** 2 + vector_a[1] ** 2) ** 0.5 \
                 + (vector_b[0] ** 2 + vector_b[1] ** 2) ** 0.5
    return round(sum_vector, 2)


