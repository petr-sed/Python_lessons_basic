# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math
class TrEug:
    def __init__(self, point_a: list, point_b: list, point_c: list):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    def orient(self):
        if self.point_b[1] > self.point_a[1]:
            self.point_a, self.point_b= self.point_b, self.point_a
        if self.point_c[1] > self.point_a[1]:
            self.point_a, self.point_c = self.point_c, self.point_a
        if  self.point_c[0] > self.point_b[0]:
            self.point_b, self.point_c = self.point_c, self.point_b

        print(self.point_a)
        print(self.point_b)
        print(self.point_c)

    def sides(self):
        side = lambda p1, p2 : math.sqrt((int(p1[0]) - int(p2[0]))**2 + (int(p1[1]) - int(p2[1]))**2)
        side_a = side(self.point_a, self.point_b)
        side_b = side(self.point_b, self.point_c)
        side_c = side(self.point_c, self.point_a)
        print(side_a)
        print(side_b)
        print(side_c)

TrEug_1 = TrEug([-2, -2], [1, 1], [2, -3])
TrEug_1.orient()
TrEug_1.sides()

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

