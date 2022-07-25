from src.Rectangle import Rectangle
import pytest


@pytest.mark.parametrize("a, b", [(-2, 1), (0, 3)])
def test_rectangle_created_negative(a, b):
    with pytest.raises(ValueError):
        Rectangle(a, b)


def test_rectangle_name(default_rectangle):
    assert default_rectangle.name == "Прямоугольник"


def test_rectangle_area(default_rectangle):
    assert default_rectangle.area == 9


def test_rectangle_perimetr(default_rectangle):
    assert default_rectangle.perimetr == 12


def test_rectangle_add_area_negative(default_rectangle):
    class NotFigure:
        pass

    with pytest.raises(ValueError):
        default_rectangle.add_area(NotFigure)


def test_rectangle_add_area_positive(default_rectangle, default_triangle):
    default_rectangle.add_area(default_triangle)


def test_rectangle_add_area(default_rectangle, default_triangle):
    assert default_rectangle.add_area(default_triangle) == 13
