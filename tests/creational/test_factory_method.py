import pytest
from patterns.creational.factory_method import Shape, Circle, Square
from tests.marker import unittest


@pytest.fixture(scope="module")
def circle() -> Shape:
    return Circle()


@pytest.fixture(scope="module")
def square() -> Shape:
    return Square()


@unittest
def test_draw_circle(circle: Shape) -> None:
    assert circle.draw() == "Circle.draw"


@unittest
def test_draw_square(square: Shape) -> None:
    assert square.draw() == "Square.draw"
