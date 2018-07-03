class Subject(object):
    """Represent what is being observed."""

    def __init__(self):
        self._observers = [] # Reference to all the observers are being kept.
                             # This is one to many relationship: there will be one subject to be observed by multiple _observers

    def attach(self, observer):
        # Append observer is it is not in a list
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):  # Simply remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:  # For all observers in a list
            if modifier != observer:  # Dont notify the observer whi is actually updating the temperature
                observer.update(self)  # Alert the observers!


class Core(Subject):  # Inherits from the Subject class

    def __init__(self, name: str = '') -> None:
        Subject.__init__(self)
        self._name: str = name  # Set name of the core
        self._temp: int = 0  # Initialize the temperature of the core

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


class TempViewer(object):
    """Observer class."""

    def update(self, subject):  # Alert method is invoked when the notify() method in a concrete subject is invoked
        print("Temperature Viewer: {} has Temperature {}".format(subject.name, subject.temp))


# Create subjects
c1 = Core("Core1")
c2 = Core("Core2")

# Create observers
v1 = TempViewer()
v2 = TempViewer()

# Attach our observers to the first core
c1.attach(v1)
c1.attach(v2)

# change the temp
c1.temp = 80
c1.notify()

c1.temp = 90
c1.notify()