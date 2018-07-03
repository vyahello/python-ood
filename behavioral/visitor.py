from abc import ABC, abstractmethod


class Visitor(ABC):
    """Abstract visitor."""

    @abstractmethod
    def visit(self, house):
        pass

    def __str__(self) -> str:
        """Return the class name when the Visitor object is printed."""
        return self.__class__.__name__


class House(ABC):
    """Abstract house."""

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

    @abstractmethod
    def work_on_hvac(self, hvac_specialist: Visitor) -> None:
        pass

    @abstractmethod
    def work_on_electricity(self, electrician: Visitor) -> None:
        pass


class ConcreteHouse(House):  # class being visited
    """Represent concrete house."""

    def accept(self, visitor: Visitor):
        """Interface to accept a visitor."""
        # Trigger the visiting operation!
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist: Visitor) -> None:
        """Hvac specialist object."""
        print(self, "worked on by", hvac_specialist)

    def work_on_electricity(self, electrician: Visitor) -> None:
        """Electrician specialist object."""
        print(self, "worked on by", electrician)

    def __str__(self) -> str:
        """Return the class name when the House object is printed."""
        return self.__class__.__name__


class HvacSpecialist(Visitor):
    """Concrete visitor: HVAC specialist."""

    def visit(self, house: House) -> None:
        house.work_on_hvac(self)  # Visitor has a reference to the house object


class Electrician(Visitor):
    """Concrete visitor: electrician."""

    def visit(self, house: House) -> None:
        house.work_on_electricity(self)  # Visitor now has a reference to the house object.


# Create an HVAC specialist
hv: Visitor = HvacSpecialist()

# Create an electrician
e: Visitor = Electrician()

# Create a house
home: House = ConcreteHouse()

# Lets the house accept the HVAC specialist and work on the house by invoking the visit() method
home.accept(hv)

# Lets the house accept the electrician specialist and work on the house by invoking the visit() method
home.accept(e)
