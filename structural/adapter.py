class Korean(object):
    """Korean speaker."""

    def __init__(self) -> None:
        self._name: str = 'Korean'

    def name(self) -> str:
        return self._name

    def speak_korean(self) -> str:
        return 'An-neyong?'


class British(object):
    """English speaker"""

    def __init__(self):
        self._name: str = 'British'

    def name(self) -> str:
        return self._name

    # Note the difference method name here!
    def speak_english(self) -> str:
        return 'Hello'


class Adapter(object):
    """Change the generic method name to individualized method names."""

    def __init__(self, obj, **adapted_method) -> None:
        """Change the name of method."""
        self._object = obj

        # Add a new dictionary item that establishes the mapping between the generic method name: speak() and the concrete method
        # For example, speak() will be translated to speak_korean() is the mapping says so

        self.__dict__.update(adapted_method)

    def __getattr__(self, item):
        """Return the rest of attributes!"""

        return getattr(self._object, item)


# List to store speaker objects
objects: list = []

# Create a Korean object
korean = Korean()

# Create a British object
british = British()

# Append the object to the objects list, dynamically
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for o in objects:
    print(f"{o.name()} says '{o.speak()}'\n")
