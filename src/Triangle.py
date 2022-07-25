from src.Figure import Figure
import math as m
import abc


class Triangle(Figure):
    _name = "Треугольник"

    def __init__(self, a, b, c):
        if a + b > c and b + c > a and c + a > b:
            self.side_1 = a
            self.side_2 = b
            self.side_3 = c
            self._area = self.area_calc()
            self._perimetr = self.perimetr_calc()
        else:
            raise ValueError

    @abc.abstractmethod
    def perimetr_calc(self):
        return self.side_1 + self.side_2 + self.side_3

    @abc.abstractmethod
    def area_calc(self):
        perimetr_half = (self.side_1 + self.side_2 + self.side_3) / 2
        return round(m.sqrt(perimetr_half * (perimetr_half - self.side_1) *
                            (perimetr_half - self.side_2) * (perimetr_half - self.side_3)))

a = Triangle(2, 2, 3)


