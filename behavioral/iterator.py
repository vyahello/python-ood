from typing import Iterator, Tuple


def count_to(count: int) -> Iterator[Tuple[int, str]]:
    """Our iterator implementation."""
    numbers_in_german = ["einn", "zwei", "drei", "veir", "funf"]
    iterator = zip(range(1, count + 1), numbers_in_german)
    for position, number in iterator:
        yield position, number


for number in count_to(3):
    print("{} in german is {}".format(*number))


class IteratorSequence(object):
    """Represent iterator sequence object."""

    def __init__(self, capacity: int) -> None:
        self._range: Iterator[int] = iter(range(capacity))

    def __next__(self) -> int:
        return next(self._range)

    def __iter__(self) -> Iterator[int]:
        return self


iterator = IteratorSequence(capacity=10)
for _ in range(10):
    print(next(iterator))
