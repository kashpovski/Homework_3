from src.Figure import Figure
import abc


class Rectangle(Figure):

    def __init__(self, a, b):
        self.side_1 = a
        self.side_2 = b
        self._name = "Прямоугольник"
        self._area = self.area_calc()
        self._perimetr = self.perimetr_calc()

    @abc.abstractmethod
    def perimetr_calc(self):
        return (self.side_1 + self.side_2) * 2

    @abc.abstractmethod
    def area_calc(self):
        return self.side_1 * self.side_2


f = Rectangle(3, 4)

f.name
f.area
f.perimetr