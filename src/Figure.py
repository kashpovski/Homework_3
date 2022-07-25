class Figure:
    _name = None
    _perimetr = None
    _area = None

    @property
    def name(self):
        return self._name

    @property
    def perimetr(self):
        return round(self._perimetr)

    @property
    def area(self):
        return round(self._area)

    def add_area(self, other_figure):
        if isinstance(other_figure, Figure):
            return self.area + other_figure.area
        else:
            raise ValueError
