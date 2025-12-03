import math

def shapes(shape_type, **kwargs):
    shape_type = shape_type.lower()

    if shape_type == 'круг':
        if 'r' in kwargs:
            r = kwargs['r']
            area = 3.14 * (r ** 2)
            return area
        else:
            return "Ошибка: Для круга требуется параметр 'r'."

    elif shape_type == 'прямоугольник':
        if 'S' in kwargs and 'h' in kwargs:
            S = kwargs['S']
            h = kwargs['h']
            area = S * h
            return area
        else:
            return "Ошибка: Для прямоугольника требуются параметры 'S' и 'h'."

    elif shape_type == 'треугольник':
        if 'base' in kwargs and 'h' in kwargs:
            base = kwargs['base']
            h = kwargs['h']
            area = 0.5 * base * h
            return area
        else:
            return "Ошибка: Для треугольника требуются параметры 'base' и 'h'."

    else:
        return f"Ошибка: Неизвестный тип фигуры '{shape_type}'. Используйте 'круг', 'прямоугольник' или 'треугольник'."



area_circle = shapes('круг', radius=5)
print(f"Площадь круга: {area_circle:.2f}")


area_rectangle = shapes('прямоугольник', S=4, h=10)
print(f"Площадь прямоугольника: {area_rectangle}")


area_triangle = shapes('треугольник', base=6, h=8)
print(f"Площадь треугольника: {area_triangle}")

