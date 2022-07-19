from src.Triangle import Triangle
import pytest


def test_figure_created():
    with pytest.raises(ValueError):
        Triangle(1, 1, 3)


def test_name(default_figure):
    triangle = default_figure
    assert triangle.name == "Треугольник"


def test_area(default_figure):
    triangle = default_figure
    assert triangle.area == 4


def test_perimetr(default_figure):
    triangle = default_figure
    assert triangle.perimetr == 9


def test_add_area_negative(default_figure):
    triangle = default_figure

    class Object:
        pass

    with pytest.raises(ValueError):
        triangle.add_area(Object())


def test_add_area_positive(default_figure):
    triangle = default_figure
    triangle.add_area(Triangle(4, 4, 4))


def test_add_area(default_figure, other_figure):
    triangle = default_figure
    triangle_2 = other_figure
    assert triangle.add_area(triangle_2) == 4 + 7

