from abc import ABC, abstractmethod


class Pet(ABC):
    """Abstraction of a pet."""

    @abstractmethod
    def speak(self) -> str:
        """Interface for a pet to speak."""
        pass


class Dog(Pet):
    """A simple dog class."""

    def __init__(self, name: str) -> None:
        self._dog_name: str = name

    def speak(self) -> str:
        return f'{self._dog_name} says Woof!'


class Cat(Pet):
    """A simple cat class."""

    def __init__(self, name: str) -> None:
        self._cat_name: str = name

    def speak(self) -> str:
        return f'{self._cat_name} says Meow!'


def get_pet(pet: str) -> Pet:
    """The factory method."""
    return {
        'dog': Dog("Hope"),
        'cat': Cat("Faith")
    }[pet]


get_pet('cat')  # returns Cat class object
