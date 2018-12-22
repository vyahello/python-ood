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
        return 'Circle.draw'


class Square(Shape):
    """Concrete shape subclass."""

    def draw(self) -> str:
        return 'Square.draw'


class ShapeFactory:
    """Concrete shape factory."""

    def __init__(self, shape: str) -> None:
        self._shape: str = shape

    def get_shape(self) -> Shape:
        if self._shape == 'circle':
            return Circle()
        if self._shape == 'square':
            return Square()
        raise ShapeError(f'Could not find shape "{self._shape}"')


factory = ShapeFactory(shape='circle')
circle: Shape = factory.get_shape()  # returns our shape
circle.draw()  # draw a circle
