from typing import Any, Dict


class Singleton:
    """Makes all instances as the same object."""

    def __new__(cls) -> "Singleton":
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance


def singleton(cls: Any) -> Any:
    """A singleton decorator."""
    instances: Dict[Any, Any] = {}

    def get_instance() -> Any:
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instance


@singleton
class Bar:
    """A fancy object."""

    pass


singleton_one: Singleton = Singleton()
singleton_two: Singleton = Singleton()

print(id(singleton_one))
print(id(singleton_two))
print(singleton_one is singleton_two)

bar_one: Bar = Bar()
bar_two: Bar = Bar()
print(id(bar_one))
print(id(bar_two))
print(bar_one is bar_two)


class Borg:
    """Borg class making class attributes global.
    Safe the same state of all instances but instances are all different."""

    _shared_state: Dict[Any, Any] = {}

    def __init__(self) -> None:
        self.__dict__ = self._shared_state


class BorgSingleton(Borg):
    """This class shares all its attribute among its instances. Store the same state."""

    def __init__(self, **kwargs: Any) -> None:
        Borg.__init__(self)
        self._shared_state.update(kwargs)

    def __str__(self) -> str:
        return str(self._shared_state)


# Create a singleton object and add out first acronym
x: Borg = BorgSingleton(HTTP="Hyper Text Transfer Protocol")
print(x)

# Create another singleton which will add to the existent dict attribute
y: Borg = BorgSingleton(SNMP="Simple Network Management Protocol")
print(y)
