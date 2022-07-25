from src.Triangle import Triangle
import pytest


@pytest.mark.parametrize("a, b, c", [(1, 1, 3), (-2, -2, -3), (0, 0, 0), (1, 2, 3)])
def test_triangle_created_negative(a, b, c):
    with pytest.raises(ValueError):
        Triangle(a, b, c)


def test_triangle_name(default_triangle):
    assert default_triangle.name == "Треугольник"


def test_triangle_area(default_triangle):
    assert default_triangle.area == 4


def test_triangle_perimetr(default_triangle):
    assert default_triangle.perimetr == 9


def test_triangle_add_area_negative(default_triangle):
    class NotFigure:
        pass

    with pytest.raises(ValueError):
        default_triangle.add_area(NotFigure)


def test_triangle_add_area_positive(default_triangle, default_circle):
    default_triangle.add_area(default_circle)


def test_triangle_add_area(default_triangle, default_circle):
    assert default_triangle.add_area(default_circle) == 32
