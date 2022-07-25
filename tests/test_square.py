from src.Square import Square
import pytest


@pytest.mark.parametrize("a", [-2, 0])
def test_square_created_negative(a):
    with pytest.raises(ValueError):
        Square(a)


def test_square_name(default_square):
    assert default_square.name == "Квадрат"


def test_square_area(default_square):
    assert default_square.area == 9


def test_square_perimetr(default_square):
    assert default_square.perimetr == 12


def test_square_add_area_negative(default_square):
    class NotFigure:
        pass

    with pytest.raises(ValueError):
        default_square.add_area(NotFigure)


def test_square_add_area_positive(default_square, default_rectangle):
    default_square.add_area(default_rectangle)


def test_square_add_area(default_square, default_rectangle):
    assert default_square.add_area(default_rectangle) == 18
