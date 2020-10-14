import copy
from abc import ABC, abstractmethod
from typing import Dict, Any


class Machine(ABC):
    """Abstract machine interface."""

    @abstractmethod
    def summary(self) -> str:
        pass


class Car(Machine):
    """A car object."""

    def __init__(self) -> None:
        self._name: str = "Skylar"
        self._color: str = "Red"
        self._options: str = "Ex"

    def summary(self) -> str:
        return "Car details: {} | {} | {}".format(
            self._name, self._color, self._options
        )


class Prototype:
    """A prototype object."""

    def __init__(self) -> None:
        self._elements: Dict[Any, Any] = {}

    def register_object(self, name: str, machine: Machine) -> None:
        self._elements[name] = machine

    def unregister_object(self, name: str) -> None:
        del self._elements[name]

    def clone(self, name: str, **attr: Any) -> Car:
        obj: Any = copy.deepcopy(self._elements[name])
        obj.__dict__.update(attr)
        return obj


# prototypical car object to be cloned
primary_car: Machine = Car()
print(primary_car.summary())
prototype: Prototype = Prototype()
prototype.register_object("skylark", primary_car)

# clone a car object
cloned_car: Machine = prototype.clone("skylark")
print(cloned_car.summary())
