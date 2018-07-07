from typing import Tuple, Iterator
import abc


class Interface(abc.ABC):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def run(self) -> str:
        pass


class A(Interface):
    """Implement interface."""

    def run(self) -> str:
        return 'A.run()'


class B(Interface):
    """Implement interface."""

    def run(self) -> str:
        return 'B.run()'


class C(Interface):
    """Implement interface."""

    def run(self) -> str:
        return 'C.run()'


class Facade(Interface):
    """Facade object."""

    def __init__(self):
        self._all: Tuple[Interface] = (A, B, C)

    def run(self) -> Iterator[Interface]:
        for obj in self._all:
            yield obj


if __name__ == '__main__':
    lst = [cls().run() for cls in Facade().run()]
    print(*lst)
