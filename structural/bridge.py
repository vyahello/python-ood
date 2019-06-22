from abc import ABC, abstractmethod


class DrawApi(ABC):
    """Provides draw interface."""

    @abstractmethod
    def draw_circle(self, x: int, y: int, radius: int) -> None:
        pass


class Circle(ABC):
    """Provides circle shape interface."""

    @abstractmethod
    def draw(self) -> None:
        pass

    @abstractmethod
    def scale(self, percentage: int) -> None:
        pass


class DrawApiOne(DrawApi):
    """Implementation-specific abstraction: concrete class one."""

    def draw_circle(self, x: int, y: int, radius: int) -> None:
        print(f"API 1 drawing a circle at ({x}, {y} with radius {radius}!)")


class DrawApiTwo(DrawApi):
    """Implementation-specific abstraction: concrete class two."""

    def draw_circle(self, x: int, y: int, radius: int) -> None:
        print(f"API 2 drawing a circle at ({x}, {y} with radius {radius}!)")


class DrawCircle(object):
    """Implementation-independent abstraction: e.g there could be a rectangle class!."""

    def __init__(self, x: int, y: int, radius: int, draw_api: DrawApi) -> None:
        self._x: int = x
        self._y: int = y
        self._radius: int = radius
        self._draw_api: DrawApi = draw_api

    def draw(self) -> None:
        self._draw_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percentage: int) -> None:
        if not isinstance(percentage, int):
            raise ValueError(f'"{percentage}" value should be an integer data type!')
        self._radius *= percentage


circle_one: Circle = DrawCircle(1, 2, 3, DrawApiOne())
circle_one.draw()
circle_two: Circle = DrawCircle(3, 4, 6, DrawApiTwo())
circle_two.draw()
