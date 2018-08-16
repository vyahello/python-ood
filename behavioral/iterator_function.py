from typing import Iterator, Tuple


def count_to(count: int) -> Iterator[Tuple[int, str]]:
    """Our iterator implementation."""

    # Our list
    number_in_german = ['einn', 'zwei', 'drei', 'veir', 'funf']

    # Our built-in iterator
    # Creates a tuple as (1, 'eins')
    iterator = zip(range(1, count + 1), number_in_german)

    # Iterate through our iterable list
    # Extract the German numbers
    # Out them in a generator called number
    for position, number in iterator:

        # Return a 'generator' containing numbers in German
        yield position, number


# Let's test the generator returned by our iterator
for num in count_to(3):
    print("{} in german is {}".format(*num))
