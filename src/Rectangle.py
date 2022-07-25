from src.Figure import Figure
import abc


class Rectangle(Figure):
    _name = "Прямоугольник"

    def __init__(self, a, b):
        if a > 0:
            self.side_1 = a
            self.side_2 = b
            self._area = self.area_calc()
            self._perimetr = self.perimetr_calc()
        else:
            raise ValueError

    @abc.abstractmethod
    def perimetr_calc(self):
        return (self.side_1 + self.side_2) * 2

    @abc.abstractmethod
    def area_calc(self):
        return self.side_1 * self.side_2
