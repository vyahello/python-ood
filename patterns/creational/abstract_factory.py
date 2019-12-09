from abc import ABC, abstractmethod
from typing import Generator


class Pet(ABC):
    """Abstract interface of a pet."""

    @abstractmethod
    def speak(self) -> str:
        pass

    @abstractmethod
    def type(self) -> str:
        pass


class Food(ABC):
    """Abstract interface of a food."""

    @abstractmethod
    def show(self) -> str:
        pass


class PetFactory(ABC):
    """Abstract interface of a pet factory."""

    @abstractmethod
    def pet(self) -> Pet:
        pass

    @abstractmethod
    def food(self) -> Food:
        pass


class PetStore(ABC):
    """Abstract interface of a pet store."""

    @abstractmethod
    def show_pet(self) -> str:
        pass


class Dog(Pet):
    """A dog pet."""

    def __init__(self, name: str, type_: str) -> None:
        self._name: str = name
        self._type: str = type_

    def speak(self) -> str:
        return f'"{self._name}" says Woof!'

    def type(self) -> str:
        return f"{self._type} dog"


class DogFood(Food):
    """A dog food."""

    def show(self) -> str:
        return "Pedigree"


class DogFactory(PetFactory):
    """A dog factory."""

    def __init__(self) -> None:
        self._dog: Pet = Dog(name="Spike", type_="bulldog")
        self._food: Food = DogFood()

    def pet(self) -> Pet:
        return self._dog

    def food(self) -> Food:
        return self._food


class Cat(Pet):
    """A cat pet."""

    def __init__(self, name: str, type_: str) -> None:
        self._name: str = name
        self._type: str = type_

    def speak(self) -> str:
        return f'"{self._name}" says Moew!'

    def type(self) -> str:
        return f"{self._type} cat"


class CatFood(Food):
    """A cat food."""

    def show(self) -> str:
        return "Whiskas"


class CatFactory(PetFactory):
    """A dog factory."""

    def __init__(self) -> None:
        self._cat: Pet = Cat(name="Hope", type_="persian")
        self._food: Food = CatFood()

    def pet(self) -> Pet:
        return self._cat

    def food(self) -> Food:
        return self._food


class FluffyStore(PetStore):
    """Houses our abstract pet factory."""

    def __init__(self, pet_factory: PetFactory) -> None:
        self._pet: Pet = pet_factory.pet()
        self._pet_food: Food = pet_factory.food()

    def show_pet(self) -> Generator[str, None, None]:
        yield f"Our pet is {self._pet.type()}"
        yield f"{self._pet.type()} {self._pet.speak()}"
        yield f"It eats {self._pet_food.show()} food"


if __name__ == "__main__":
    # cat factory
    cat_factory: PetFactory = CatFactory()
    store: PetStore = FluffyStore(cat_factory)
    print(tuple(store.show_pet()))

    # dog factory
    dog_factory: PetFactory = DogFactory()
    store: PetStore = FluffyStore(dog_factory)
    print(tuple(store.show_pet()))
