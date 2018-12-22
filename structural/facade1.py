from abc import ABC, abstractmethod
import time
from typing import Iterator, Tuple

_sleep: float = 0.2


class TestCase(ABC):
    """Abstraction provides `run()` interface."""

    @abstractmethod
    def run(self) -> None:
        """Abstract interface that has to be reused by child objects."""
        pass


# Complex Parts
class TestCase1(TestCase):
    """Concrete test case."""

    def __init__(self, name: str) -> None:
        self._name: str = name

    def run(self) -> None:
        print('{:#^20}'.format(self._name))
        time.sleep(_sleep)
        print("Setting up")
        time.sleep(_sleep)
        print("Running test")
        time.sleep(_sleep)
        print("Tearing down")
        time.sleep(_sleep)
        print("Test Finished\n")


class TestCase2(TestCase):
    """Concrete test case."""

    def __init__(self, name: str) -> None:
        self._name: str = name

    def run(self) -> None:
        print('{:#^20}'.format(self._name))
        time.sleep(_sleep)
        print("Setting up")
        time.sleep(_sleep)
        print("Running test")
        time.sleep(_sleep)
        print("Tearing down")
        time.sleep(_sleep)
        print("Test Finished\n")


class TestCase3(TestCase):
    """Concrete test case."""

    def __init__(self, name: str) -> None:
        self._name: str = name

    def run(self) -> None:
        print('{:#^20}'.format(self._name))
        time.sleep(_sleep)
        print("Setting up")
        time.sleep(_sleep)
        print("Running test")
        time.sleep(_sleep)
        print("Tearing down")
        time.sleep(_sleep)
        print("Test Finished\n")


# Facade
class TestRunner:
    """Represent simpler unified interface to run all test cases."""

    def __init__(self) -> None:
        self._tcs: Tuple[TestCase] = (TestCase1('Test Case 1'),
                                      TestCase2('Test Case 2'),
                                      TestCase3('Test Case 3'))

    def _tests(self) -> Iterator[TestCase]:
        yield from self._tcs

    def run(self) -> None:
        c = 0
        tests = self._tests()
        while c < len(self._tcs):
            next(tests).run()
            c += 1


# Client
class Client:
    """Client runner."""

    def __init__(self) -> None:
        self._runner: TestRunner = TestRunner()

    def run(self) -> None:
        self._runner.run()


if __name__ == '__main__':
    client: Client = Client()
    client.run()
