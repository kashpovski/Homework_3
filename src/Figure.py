

class Figure:
    _name = None
    _perimetr = None
    _area = None

    @property
    def name(self):
        return print(self._name)

    @property
    def perimetr(self):
        return print(self._perimetr)

    @property
    def area(self):
        return print(self._area)

    def add_area(self, other_figure):
        if isinstance(other_figure, Figure):
            print(self._area + other_figure._area)
        else:
            raise ValueError


