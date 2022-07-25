from src.Circle import Circle
import pytest


@pytest.mark.parametrize("a", [-2, 0])
def test_circle_created_negative(a):
    with pytest.raises(ValueError):
        Circle(a)


def test_circle_name(default_circle):
    assert default_circle.name == "Круг"


def test_circle_area(default_circle):
    assert default_circle.area == 28


def test_circle_perimetr(default_circle):
    assert default_circle.perimetr == 19


def test_circle_add_area_negative(default_circle):
    class NotFigure:
        pass

    with pytest.raises(ValueError):
        default_circle.add_area(NotFigure)


def test_circle_add_area_positive(default_circle, default_triangle):
    default_circle.add_area(default_triangle)


def test_circle_add_area(default_circle, default_triangle):
    assert default_circle.add_area(default_triangle) == 32
