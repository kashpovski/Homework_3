from src.Figure import Figure
import abc


class Circle(Figure):
    _name = "Круг"

    def __init__(self, a):
        self.radius = a
        self._area = self.area_calc()
        self._perimetr = self.l_circle_calc()

    @abc.abstractmethod
    def l_circle_calc(self):
        return 2 * 3.14 * self.radius

    @abc.abstractmethod
    def area_calc(self):
        return 3.14 * (self.radius ** 2)

