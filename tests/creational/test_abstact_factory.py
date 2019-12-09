from typing import Sequence
import pytest
from patterns.creational.abstract_factory import (
    Pet,
    PetFactory,
    Dog,
    Cat,
    DogFood,
    CatFood,
    DogFactory,
    CatFactory,
    FluffyStore,
    PetStore,
)
from tests.marker import unittest


@pytest.fixture(scope="module")
def dog() -> Pet:
    return Dog(name="Spike", type_="bulldog")


@pytest.fixture(scope="module")
def cat() -> Pet:
    return Cat(name="Miya", type_="persian")


@pytest.fixture(scope="module")
def dog_factory() -> PetFactory:
    return DogFactory()


@pytest.fixture(scope="module")
def cat_factory() -> PetFactory:
    return CatFactory()


@unittest
def test_dog_speak(dog: Pet) -> None:
    assert dog.speak() == '"Spike" says Woof!'


@unittest
def test_dog_type(dog: Pet) -> None:
    assert dog.type() == "bulldog dog"


@unittest
def test_cat_speak(cat: Pet) -> None:
    assert cat.speak() == '"Miya" says Moew!'


@unittest
def test_cat_type(cat: Pet) -> None:
    assert cat.type() == "persian cat"


@unittest
def test_dog_food() -> None:
    assert DogFood().show() == "Pedigree"


@unittest
def test_cat_food() -> None:
    assert CatFood().show() == "Whiskas"


@unittest
def test_dog_factory_pet(dog_factory: PetFactory) -> None:
    assert isinstance(dog_factory.pet(), Dog)


@unittest
def test_dog_factory_food(dog_factory: PetFactory) -> None:
    assert isinstance(dog_factory.food(), DogFood)


@unittest
def test_cat_factory_pet(dog_factory: PetFactory) -> None:
    assert isinstance(dog_factory.pet(), Dog)


@unittest
def test_cat_factory_food(dog_factory: PetFactory) -> None:
    assert isinstance(dog_factory.food(), DogFood)


@unittest
@pytest.mark.parametrize(
    "store, result",
    (
        (
            FluffyStore(CatFactory()),
            ("Our pet is persian cat", 'persian cat "Hope" says Moew!', "It eats Whiskas food"),
        ),
        (
            FluffyStore(DogFactory()),
            ("Our pet is bulldog dog", 'bulldog dog "Spike" says Woof!', "It eats Pedigree food"),
        ),
    ),
)
def test_fluffy_store(store: PetStore, result: Sequence[str]) -> None:
    assert tuple(store.show_pet()) == result
