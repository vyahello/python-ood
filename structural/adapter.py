from abc import ABC, abstractmethod


class Speaker(ABC):
    """Abstract interface for some speaker."""

    @abstractmethod
    def type(self) -> str:
        pass


class Korean(Speaker):
    """Korean speaker."""

    def __init__(self) -> None:
        self._type: str = "Korean"

    def type(self) -> str:
        return self._type

    def speak_korean(self) -> str:
        return "An-neyong?"


class British(Speaker):
    """English speaker."""

    def __init__(self):
        self._type: str = "British"

    def type(self) -> str:
        return self._type

    def speak_english(self) -> str:
        return "Hello"


class Adapter:
    """Changes the generic method name to individualized method names."""

    def __init__(self, obj, **adapted_method) -> None:
        self._object = obj
        self.__dict__.update(adapted_method)

    def __getattr__(self, item):
        return getattr(self._object, item)


speakers: list = []
korean = Korean()
british = British()
speakers.append(Adapter(korean, speak=korean.speak_korean))
speakers.append(Adapter(british, speak=british.speak_english))

for speaker in speakers:
    print(f"{speaker.type()} says '{speaker.speak()}'")
