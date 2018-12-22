from abc import ABC, abstractmethod


class DrawAPI(ABC):
    """Provide `draw_circle()` interface for child objects."""

    @abstractmethod
    def draw_circle(self, x: int, y: int, radius: int) -> None:
        pass


class Circle(ABC):
    """Provide two interfaces `draw()` and `scale` interfaces for child objects."""

    @abstractmethod
    def draw(self) -> None:
        pass

    @abstractmethod
    def scale(self, percent: int) -> None:
        pass


class DrawAPIOne(DrawAPI):
    """Implementation-specific abstraction: concrete class one."""

    def draw_circle(self, x: int, y: int, radius: int) -> None:
        print("API 1 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))


class DrawAPITwo(DrawAPI):
    """Implementation-specific abstraction: concrete class two."""

    def draw_circle(self, x: int, y: int, radius: int) -> None:
        print("API 2 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))


class DrawCircle:
    """Implementation-independent abstraction: e.g there could be a rectangle class!."""

    def __init__(self, x: int, y: int, radius: int, draw_api: DrawAPI) -> None:
        """Initialize the necessary attributes."""
        self._x: int = x
        self._y: int = y
        self._radius: int = radius
        self._draw_api: DrawAPI = draw_api

    def draw(self) -> None:
        """Implementation-specific abstraction taken care of another class: DrawAPI."""

        self._draw_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent: int) -> None:
        """Implementation-independent."""

        self._radius *= percent


# Build the first Circle object using API One
circle1: Circle = DrawCircle(1, 2, 3, DrawAPIOne())

# Draw a circle
circle1.draw()

# Build the second Circle object sing APi Two
circle2: Circle = DrawCircle(3, 4, 6, DrawAPITwo())

# Draw a circle
circle2.draw()
