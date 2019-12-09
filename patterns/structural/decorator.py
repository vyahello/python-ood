from functools import wraps
from typing import Callable
from abc import ABC, abstractmethod


def make_blink(function: Callable[[str], str]) -> Callable[..., str]:
    """Defines the decorator function."""

    @wraps(function)
    def decorator(*args, **kwargs) -> str:
        result: str = function(*args, **kwargs)
        return f"<blink>{result}</blink>"

    return decorator


@make_blink
def hello_world(name: str) -> str:
    """Original function."""
    return f'Hello World said "{name}"!'


print(hello_world(name="James"))
print(hello_world.__name__)
print(hello_world.__doc__)


class Number(ABC):
    """Abstraction of a number object."""

    @abstractmethod
    def value(self) -> int:
        pass


class Integer(Number):
    """A subclass of a number."""

    def __init__(self, value: int) -> None:
        self._value = value

    def value(self) -> int:
        return self._value


class Float(Number):
    """Decorator object converts `int` datatype into `float` datatype."""

    def __init__(self, number: Number) -> None:
        self._number: Number = number

    def value(self) -> float:
        return float(self._number.value())


class SumOfFloat(Number):
    """Sum of two `float` numbers."""

    def __init__(self, one: Number, two: Number) -> None:
        self._one: Float = Float(one)
        self._two: Float = Float(two)

    def value(self) -> float:
        return self._one.value() + self._two.value()


integer_one: Number = Integer(value=5)
integer_two: Number = Integer(value=6)
sum_float: Number = SumOfFloat(integer_one, integer_two)
print(sum_float.value())
