from abc import ABC, abstractmethod


class Shape(ABC):
    """Interface that defines the shape."""

    @abstractmethod
    def draw(self) -> str:
        pass


class ShapeError(Exception):
    """Represent shape error message."""

    pass


class Circle(Shape):
    """Concrete shape subclass."""

    def draw(self) -> str:
        return "Circle.draw"


class Square(Shape):
    """Concrete shape subclass."""

    def draw(self) -> str:
        return "Square.draw"


class ShapeFactory:
    """Concrete shape factory."""

    def __init__(self, shape: str) -> None:
        self._shape: str = shape

    def get_shape(self) -> Shape:
        if self._shape == "circle":
            return Circle()
        if self._shape == "square":
            return Square()
        raise ShapeError(f'Could not find shape "{self._shape}"')


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
        return f"{self._dog_name} says Woof!"


class Cat(Pet):
    """A simple cat class."""

    def __init__(self, name: str) -> None:
        self._cat_name: str = name

    def speak(self) -> str:
        return f"{self._cat_name} says Meow!"


def get_pet(pet: str) -> Pet:
    """The factory method."""
    return {"dog": Dog("Hope"), "cat": Cat("Faith")}[pet]


if __name__ == "__main__":
    factory: ShapeFactory = ShapeFactory(shape="circle")
    circle: Shape = factory.get_shape()  # returns our shape
    circle.draw()  # draw a circle

    # return Cat class object
    get_pet("cat")
