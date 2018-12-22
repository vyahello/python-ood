from typing import Iterator


class IteratorSequence:
    """Represent iterator sequence object."""

    def __init__(self, capacity: int) -> None:
        self._rng: Iterator[int] = iter(range(capacity))

    def __next__(self) -> int:
        return next(self._rng)

    def __iter__(self) -> Iterator[int]:
        return self


iterator = IteratorSequence(capacity=10)

for _ in range(10):
    print(next(iterator))
