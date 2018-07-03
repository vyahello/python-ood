from abc import ABC, abstractmethod


class Subject(ABC):
    """Abstract subject."""

    @abstractmethod
    def attach(self, observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer) -> None:
        pass

    @abstractmethod
    def notify(self, modifier=None) -> None:
        pass

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def temp(self) -> None:
        pass


class Core(Subject):
    """Represent what is being observed. Need to be monitored."""

    def __init__(self, name: str = '') -> None:
        self._observers = []  # Reference to all the observers are being kept.
                              # This is one to many relationship: there will be one subject to be observed by multiple _observers
        self._name: str = name  # Set name of the core
        self._temp: int = 0  # Initialize the temperature of the core

    def attach(self, observer) -> None:
        # Append observer is it is not in a list
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer) -> None:  # Simply remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None) -> None:
        for observer in self._observers:  # For all observers in a list
            if modifier != observer:  # Don't notify the observer which is actually updating the temperature
                observer.update(self)  # Alert the observers!

    @property
    def name(self) -> str:
        return self._name

    @property  # Getter that gets the core temperature
    def temp(self) -> int:
        return self._temp

    @temp.setter # Setter that sets the core temperature
    def temp(self, temp: int) -> None:
        self._temp = temp
        # Notify the observers whenever somebody changes the core temperature


class TempObserver(object):
    """Observer class. Need to be notified."""

    def update(self, subject: Subject):  # Alert method is invoked when the notify() method in a concrete subject is invoked
        print("Temperature Viewer: {} has Temperature {}".format(subject.name, subject.temp))


# Create subjects
c1 = Core("Core1")
c2 = Core("Core2")

# Create observers
v1 = TempObserver()
v2 = TempObserver()

# Attach our observers to the first core
c1.attach(v1)
c1.attach(v2)


# change the temp
c1.temp = 80
c1.notify()

c1.temp = 90
c1.notify()
