from typing import Iterator, Tuple, List


def count_to(count: int) -> Iterator[Tuple[int, str]]:
    """Our iterator implementation."""
    numbers_in_german: List[str] = ["einn", "zwei", "drei", "veir", "funf"]
    iterator: Iterator[Tuple[int, str]] = zip(range(1, count + 1), numbers_in_german)
    for position, number in iterator:  # type: int, str
        yield position, number


for number_ in count_to(3):  # type: Tuple[int]
    print("{} in german is {}".format(*number_))


class IteratorSequence:
    """Represent iterator sequence object."""

    def __init__(self, capacity: int) -> None:
        self._range: Iterator[int] = iter(range(capacity))

    def __next__(self) -> int:
        return next(self._range)

    def __iter__(self) -> Iterator[int]:
        return self


iterator_: IteratorSequence = IteratorSequence(capacity=10)
for _ in range(10):  # type: int
    print(next(iterator_))
