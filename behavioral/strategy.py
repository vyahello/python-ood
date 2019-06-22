import types
from typing import Callable, Any


class Strategy:
    """A strategy pattern class."""

    def __init__(self, func: Callable[["Strategy"], Any] = None) -> None:
        self._name: str = "Default strategy"
        if func:
            self.execute = types.MethodType(func, self)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise ValueError(f'"{name}" value should be a string data type!')
        self._name = name

    def execute(self):
        print(f"{self._name} is used")


def strategy_function_one(strategy: Strategy) -> None:
    print(f"{strategy.name} is used to execute method one")


def strategy_function_two(strategy: Strategy) -> None:
    print(f"{strategy.name} is used to execute method two")


default_strategy = Strategy()
default_strategy.execute()

first_strategy = Strategy(func=strategy_function_one)
first_strategy.name = "Strategy one"
first_strategy.execute()

second_strategy = Strategy(func=strategy_function_two)
second_strategy.name = "Strategy two"
second_strategy.execute()
