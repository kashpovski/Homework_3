import pytest

from src.Triangle import Triangle


@pytest.fixture
def default_figure():
    return Triangle(3, 3, 3)


@pytest.fixture
def other_figure():
    figure = Triangle(4, 4, 4)
    yield figure
    del figure
