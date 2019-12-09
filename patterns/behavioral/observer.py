from typing import List


class Subject:
    """Represents what is being observed. Needs to be monitored."""

    def __init__(self, name: str = "") -> None:
        self._observers: List["TempObserver"] = []
        self._name: str = name
        self._temperature: int = 0

    def attach(self, observer: "TempObserver") -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: "TempObserver") -> None:
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None) -> None:
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

    @property
    def name(self) -> str:
        return self._name

    @property
    def temperature(self) -> int:
        return self._temperature

    @temperature.setter
    def temperature(self, temperature: int) -> None:
        if not isinstance(temperature, int):
            raise ValueError(f'"{temperature}" value should be an integer data type!')
        self._temperature = temperature


class TempObserver:
    """Represents an observer class. Needs to be notified."""

    def update(self, subject: Subject) -> None:
        print(f"Temperature Viewer: {subject.name} has Temperature {subject.temperature}")


subject_one = Subject("Subject One")
subject_two = Subject("Subject Two")

observer_one = TempObserver()
observer_two = TempObserver()

subject_one.attach(observer_one)
subject_one.attach(observer_two)

subject_one.temperature = 80
subject_one.notify()

subject_one.temperature = 90
subject_one.notify()
