from src.Figure import Figure
import abc


class Square(Figure):
    _name = "Квадрат"

    def __init__(self, a):
        if a > 0:
            self.side_1 = a
            self._area = self.area_calc()
            self._perimetr = self.perimetr_calc()
        else:
            raise ValueError

    @abc.abstractmethod
    def perimetr_calc(self):
        return self.side_1 * 4

    @abc.abstractmethod
    def area_calc(self):
        return self.side_1 ** 2



