from abc import ABC, abstractmethod


class Visitor(ABC):
    """Abstract visitor."""

    @abstractmethod
    def visit(self, house: "House") -> None:
        pass

    def __str__(self) -> str:
        return self.__class__.__name__


class House(ABC):
    """Abstract house."""

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

    @abstractmethod
    def work_on_hvac(self, specialist: Visitor) -> None:
        pass

    @abstractmethod
    def work_on_electricity(self, specialist: Visitor) -> None:
        pass

    def __str__(self) -> str:
        return self.__class__.__name__


class ConcreteHouse(House):
    """Represent concrete house."""

    def accept(self, visitor: Visitor) -> None:
        visitor.visit(self)

    def work_on_hvac(self, specialist: Visitor) -> None:
        print(self, "worked on by", specialist)

    def work_on_electricity(self, specialist: Visitor) -> None:
        print(self, "worked on by", specialist)


class HvacSpecialist(Visitor):
    """Concrete visitor: HVAC specialist."""

    def visit(self, house: House) -> None:
        house.work_on_hvac(self)


class Electrician(Visitor):
    """Concrete visitor: electrician."""

    def visit(self, house: House) -> None:
        house.work_on_electricity(self)


hvac: Visitor = HvacSpecialist()
electrician: Visitor = Electrician()
home: House = ConcreteHouse()
home.accept(hvac)
home.accept(electrician)
