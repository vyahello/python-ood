from functools import wraps
from typing import Callable


def make_blink(function: Callable[[str], str]) -> Callable[..., str]:
    """Define the decorator."""

    # This makes the decorator transperant in terms of its name and docstring
    @wraps(function)

    # Define the inner function
    def decorator(*args, **kwargs) -> str:

        # Return value of the function being decorated
        ret = function(*args, **kwargs)

        # Add new functionality to the function being decorated
        return f"<blink>{ret}</blink>"

    return decorator

@make_blink
def hello_world(name: str) -> str:
    """Original function!"""

    return f"Hello World said {name}!"


# Decorated function
print(hello_world('James'))

# Check if the function name is still the same name of the function being decorated
print(hello_world.__name__)

# Check if the docstring is still the same name of the function being decorated
print(hello_world.__doc__)
