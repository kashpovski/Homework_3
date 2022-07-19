

class Figure:
    _name = None
    _perimetr = None
    _area = None

    @property
    def name(self):
        return self._name

    @property
    def perimetr(self):
        return self._perimetr

    @property
    def area(self):
        return self._area

    def add_area(self, other_figure):
        if isinstance(other_figure, Figure):
            return self._area + other_figure._area
        else:
            raise ValueError
