from abc import ABC, abstractmethod


class Int(ABC):
    """Abstraction of and `int` object"""

    @abstractmethod
    def value(self) -> int:
        pass


class ToFloat:
    """Decorator object converts `int` datatype into `float` datatype."""

    def __init__(self, int_obj: Int) -> None:
        self._int_obj: Int = int_obj

    def value(self) -> float:
        return float(self._int_obj.value())


class IntA(Int):
    """Int object A."""

    def __init__(self, a_obj: int) -> None:
        self._int_a: int = a_obj

    def value(self) -> int:
        return self._int_a


class IntB(Int):
    """Int object B."""

    def __init__(self, b_obj: int) -> None:
        self._int_b: int = b_obj

    def value(self) -> int:
        return self._int_b


class SumFloat:
    """Sum `float` numbers."""

    def __init__(self, a_obj: Int, b_obj: Int) -> None:
        self._int_a: ToFloat = ToFloat(a_obj)
        self._int_b: ToFloat = ToFloat(b_obj)

    def value(self) -> float:
        return self._int_a.value() + self._int_b.value()


int_a: Int = IntA(5)
int_b: Int = IntB(6)

sum_f = SumFloat(int_a, int_b)
print(sum_f.value())
