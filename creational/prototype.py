import copy
from typing import Any


class Car(object):
    """A car object."""

    def __init__(self) -> None:
        self._name = 'Skylar'
        self._color = 'Red'
        self._options = 'Ex'

    def __str__(self) -> str:
        return '{} | {} | {}'.format(self._name, self._color, self._options)


class Prototype:
    """A prototype object."""

    def __init__(self):
        self._objects = {}

    def register_object(self, name: str, obj: Car) -> None:
        """Register an object."""

        self._objects[name] = obj

    def unregister_object(self, name: str) -> None:
        """Unregister an object."""

        del self._objects[name]

    def clone(self, name: str, **attr: Any) -> Car:
        """Clone a registered object and update its attributes."""

        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(attr)
        return obj


# Prototypical object to be cloned
car = Car()
prototype = Prototype()
prototype.register_object('skylark', car)

# Clone the object
car1 = prototype.clone('skylark')
print(car1)
