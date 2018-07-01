from typing import Any


class Borg(object):
    """Borg class making class attributes global.
    Safe the same state of all instances but instances are all different."""

    _shared_state: dict = {}  # Attribute dictionary

    def __init__(self) -> None:
        # Make it an attribute dictionary
        self.__dict__ = self._shared_state


class BorgSingleton(Borg):
    """This class shares all its attribute among its instances. Store the same state."""
    # Makes a singleton an object-oriented global variable

    def __init__(self, **kwargs: Any) -> None:
        Borg.__init__(self)
        # Update the attribute dictionary by inserting a new key-value pair
        self._shared_state.update(kwargs)

    def __str__(self) -> str:
        # Return the attribute dict for printing
        return str(self._shared_state)


# Create a singleton object and add out first acronym
x = BorgSingleton(HTTP='Hyper Text Transfer Protocol')
print(x)

# Create another singleton which will add to the existent dict attribute
y = BorgSingleton(SNMP='Simple Network Management Protocol')
print(y)
