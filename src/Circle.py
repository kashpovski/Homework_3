from src.Figure import Figure
import abc


class Circle(Figure):

    def __init__(self, a):
        self.radius = a
        self._name = "Круг"
        self._area = self.area_calc()
        self._perimetr = self.l_circle_calc()

    @abc.abstractmethod
    def l_circle_calc(self):
        return 2 * 3.14 * self.radius

    @abc.abstractmethod
    def area_calc(self):
        return 3.14 * (self.radius ** 2)

