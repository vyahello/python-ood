from abc import ABC, abstractmethod


class Int(ABC):
    """Abstraction of and `int` object"""

    @abstractmethod
    def value(self) -> int:
        pass


class ToFloat(object):
    """Decorator object converts `int` datatype into `float` datatype."""

    def __init__(self, int_obj: Int) -> None:
        self._int_obj: Int = int_obj

    def value(self) -> float:
        return float(self._int_obj.value())


class IntA(Int):
    """Int object A."""

    def __init__(self, int_a: int) -> None:
        self._int_a: int = int_a

    def value(self) -> int:
        return self._int_a


class IntB(Int):
    """Int object B."""

    def __init__(self, int_b: int) -> None:
        self._int_b: int = int_b

    def value(self) -> int:
        return self._int_b


class SumFloat:
    """Sum `float` numbers."""

    def __init__(self, int_a: Int, int_b: Int) -> None:
        self._int_a: ToFloat = ToFloat(int_a)
        self._int_b: ToFloat = ToFloat(int_b)

    def value(self) -> float:
        return self._int_a.value() + self._int_b.value()


int_a: Int = IntA(5)
int_b: Int = IntB(6)

sum_f = SumFloat(int_a, int_b)
print(sum_f.value())
