import math


class Trapezoid:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3
        self.x4, self.y4 = x4, y4

    def is_isosceles(self):
        # Вычисление длины сторон
        a = math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)
        c = math.sqrt((self.x3 - self.x4) ** 2 + (self.y3 - self.y4) ** 2)

        # Проверка, является ли фигура равнобедренной
        if a == c:
            return True
        else:
            return False

    @staticmethod
    def side_lengths(x1, y1, x2, y2, x3, y3, x4, y4):
        # Вычисление длины сторон
        a = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        b = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
        c = math.sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2)
        d = math.sqrt((x4 - x1) ** 2 + (y4 - y1) ** 2)
        return a, b, c, d

    @staticmethod
    def area(x1, y1, x2, y2, x3, y3, x4, y4):
        # Вычисление длины сторон
        a, b, c, d = Trapezoid.side_lengths(x1, y1, x2, y2, x3, y3, x4, y4)
        # Вычисление высоты
        height = math.sqrt(a ** 2 - ((d - b) ** 2 + a ** 2 - c ** 2) / (2 * (d - b)))
        # Вычисление площади
        return round((b + d) / 2 * height, 2)

    @staticmethod
    def perimeter(x1, y1, x2, y2, x3, y3, x4, y4):
        # Вычисление периметра
        a, b, c, d = Trapezoid.side_lengths(x1, y1, x2, y2, x3, y3, x4, y4)
        return round(a + b + c + d, 2)


# Пример использования класса
trap = Trapezoid(0, 0, 2, 4, 6, 4, 8, 0)
print("Площадь:", Trapezoid.area(0, 0, 2, 4, 6, 4, 8, 0))
print("Периметр:", Trapezoid.perimeter(0, 0, 2, 4, 6, 4, 8, 0))
if trap.is_isosceles():
    print("Фигура является равнобедренной трапецией.")
else:
    print("Фигура не является равнобедренной трапецией.")
