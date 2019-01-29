# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt


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
        if self.point_c[0] > self.point_b[0]:
            self.point_b, self.point_c = self.point_c, self.point_b

    def sides(self):
        TrEug.orient(self)
        side = lambda p1, p2 : sqrt((int(p1[0]) - int(p2[0]))**2 + (int(p1[1]) - int(p2[1]))**2)
        side_a = side(self.point_a, self.point_b)
        side_b = side(self.point_b, self.point_c)
        side_c = side(self.point_c, self.point_a)

        return side_a, side_b, side_c


    def perimetr(self):
        list_sides = list(TrEug.sides(self))
        per = list_sides[0] + list_sides[1] + list_sides[2]

        return round(per, 2)


    def visota(self):
        list_sides = list(TrEug.sides(self))
        p = TrEug.perimetr(self)/2
        vis =2/list_sides[1] * sqrt(p*(p-list_sides[0])*(p-list_sides[1])*(p-list_sides[2]))

        return round(vis, 2)

    def face(self):
        list_sides = list(TrEug.sides(self))
        v = TrEug.visota(self)
        f = (list_sides[1]*v)/2

        return round(f, 2)



# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class TrapRavn:
    def __init__(self, point_a: list, point_b: list, point_c: list, point_d: list):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.point_d = point_d

    def orient(self):
        if self.point_b[1] > self.point_a[1]:
            self.point_a, self.point_b = self.point_b, self.point_a
        elif self.point_c[1] > self.point_a[1]:
            self.point_a, self.point_c = self.point_c, self.point_a
        elif self.point_d[1] > self.point_a[1]:
            self.point_a, self.point_d = self.point_d, self.point_a

        if self.point_c[1] > self.point_b[1]:
            self.point_b, self.point_c = self.point_c, self.point_b
        elif self.point_d[1] > self.point_b[1]:
            self.point_b, self.point_d = self.point_d, self.point_b

        if self.point_b[0] < self.point_a[0]:
            self.point_a, self.point_b = self.point_b, self.point_a

        if self.point_c[0] < self.point_d[0]:
            self.point_c, self.point_d = self.point_d, self.point_c

        print(self.point_a)
        print(self.point_b)
        print(self.point_c)
        print(self.point_d)

    def sides(self):
        TrapRavn.orient(self)
        side = lambda p1, p2: sqrt((int(p1[0]) - int(p2[0])) ** 2 + (int(p1[1]) - int(p2[1])) ** 2)
        side_a = side(self.point_a, self.point_b)
        side_b = side(self.point_b, self.point_c)
        side_c = side(self.point_c, self.point_d)
        side_d = side(self.point_d, self.point_a)

        return (side_a, side_b, side_c, side_d) if side_b == side_d else "Фигура не является равнобочной трапецией"


TrapRavn_1 = TrapRavn([3, 4], [-7, -2], [-5, 4], [5, -2])
TrapRavn_1.orient()
print(TrapRavn_1.sides())