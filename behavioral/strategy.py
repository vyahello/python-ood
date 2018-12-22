import types
from typing import Callable, Any


class Strategy:
    """The strategy pattern class."""

    def __init__(self, func: Callable[['Strategy'], Any] = None) -> None:
        self._name = "Default strategy"

        # If a reference to a function is provided, replace the execute() method with the given function
        if func:
            self._execute: Callable = types.MethodType(func, self)  # dynamically add a new method to a class

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    def execute(self):  # gets replace by another version if another strategy is provided.
        print("{} is used".format(self._name))


# Replacement method 1
def strategy_one(strategy: Strategy) -> None:
    print("{} is used to execute method 1".format(strategy.name))


# Replacement method 2
def strategy_two(strategy: Strategy) -> None:
    print("{} is used to execute method 2".format(strategy.name))


# Default strategy
s0 = Strategy()

# Execute our default strategy
s0.execute()

# Let'screate the first variation of our default strategy by providing a new behavior
s1 = Strategy(func=strategy_one)

# Set it's name
s1.name = 'Strategy one'

# Execute the strategy
s1.execute()

s2 = Strategy(func=strategy_two)
s2.name = 'Strategy two'
s2.execute()
