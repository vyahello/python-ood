from typing import Type
import pytest
from patterns.creational.factory_method import (
    Shape,
    Circle,
    Square,
    ShapeFactory,
    ShapeError,
    Dog,
    Cat,
    Pet,
    get_pet,
)
from tests.marker import unittest

pytestmark = unittest


@pytest.fixture(scope="module")
def circle() -> Shape:
    return Circle()


@pytest.fixture(scope="module")
def square() -> Shape:
    return Square()


def test_draw_circle(circle: Shape) -> None:
    assert circle.draw() == "Circle.draw"


def test_draw_square(square: Shape) -> None:
    assert square.draw() == "Square.draw"


@pytest.mark.parametrize(
    "shape, instance", (("circle", Circle), ("square", Square))
)
def test_shape_factory(shape: str, instance: Type[Shape]) -> None:
    assert isinstance(ShapeFactory(shape).get_shape(), instance)


def test_shape_error() -> None:
    with pytest.raises(ShapeError):
        ShapeFactory("fooo").get_shape()


def test_dog_speak() -> None:
    assert Dog("Spike").speak() == "Spike says Woof!"


def test_cat_speak() -> None:
    assert Cat("Miya").speak() == "Miya says Meow!"


@pytest.mark.parametrize("pet, instance", (("dog", Dog), ("cat", Cat)))
def test_get_pet(pet: str, instance: Type[Pet]) -> None:
    assert isinstance(get_pet(pet), instance)


def test_get_wrong_pet() -> None:
    with pytest.raises(KeyError):
        get_pet("foo")
