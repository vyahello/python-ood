import pytest

from patterns.creational.builder import (
    Builder,
    Car,
    Director,
    Machine,
    SkyLarkBuilder,
)


@pytest.fixture
def car() -> Machine:
    return Car()


@pytest.fixture
def skylark_builder() -> Builder:
    return SkyLarkBuilder()


@pytest.fixture
def director(skylark_builder: Builder) -> Director:
    return Director(skylark_builder)


def test_car_summary(car: Machine) -> None:
    assert car.summary() == "Car details: None | None | None"


def test_skylark_builder_machine(skylark_builder: Builder) -> None:
    assert isinstance(skylark_builder.machine(), Machine)


def test_director_release_machine(director: Director) -> None:
    assert isinstance(director.release_machine(), Machine)
