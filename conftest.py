import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.fixture
def default_triangle():
    return Triangle(3, 3, 3)


@pytest.fixture
def default_circle():
    return Circle(3)


@pytest.fixture
def default_rectangle():
    return Rectangle(3, 3)


@pytest.fixture
def default_square():
    return Square(3)


@pytest.fixture
def other_figure():
    figure = Triangle(4, 4, 4)
    yield figure
    del figure
