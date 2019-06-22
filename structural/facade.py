from abc import ABC, abstractmethod
import time
from typing import List, Tuple, Iterator

_sleep: float = 0.2


class TestCase(ABC):
    """Abstract test case interface."""

    @abstractmethod
    def run(self) -> None:
        pass


class TestCaseOne(TestCase):
    """Concrete test case."""

    def __init__(self, name: str) -> None:
        self._name: str = name

    def run(self) -> None:
        print("{:#^20}".format(self._name))
        time.sleep(_sleep)
        print("Setting up")
        time.sleep(_sleep)
        print("Running test")
        time.sleep(_sleep)
        print("Tearing down")
        time.sleep(_sleep)
        print("Test Finished\n")


class TestCaseTwo(TestCase):
    """Concrete test case."""

    def __init__(self, name: str) -> None:
        self._name: str = name

    def run(self) -> None:
        print("{:#^20}".format(self._name))
        time.sleep(_sleep)
        print("Setting up")
        time.sleep(_sleep)
        print("Running test")
        time.sleep(_sleep)
        print("Tearing down")
        time.sleep(_sleep)
        print("Test Finished\n")


class TestCaseThree(TestCase):
    """Concrete test case."""

    def __init__(self, name: str) -> None:
        self._name: str = name

    def run(self) -> None:
        print("{:#^20}".format(self._name))
        time.sleep(_sleep)
        print("Setting up")
        time.sleep(_sleep)
        print("Running test")
        time.sleep(_sleep)
        print("Tearing down")
        time.sleep(_sleep)
        print("Test Finished\n")


class TestSuite:
    """Represents simpler unified interface to run all test cases.

    A facade class itself.
    """

    def __init__(self, test_cases: List[TestCase]) -> None:
        self._test_cases = test_cases

    def run(self) -> None:
        for test_case in self._test_cases:
            test_case.run()


test_cases: List[TestCase] = [TestCaseOne("TC1"), TestCaseTwo("TC2"), TestCaseThree("TC3")]
test_suite = TestSuite(test_cases)
test_suite.run()


class Interface(ABC):
    """Abstract interface."""

    @abstractmethod
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
