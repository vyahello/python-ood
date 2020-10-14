from abc import ABC, abstractmethod


class Machine(ABC):
    """Abstract machine interface."""

    @abstractmethod
    def summary(self) -> str:
        pass


class Builder(ABC):
    """Abstract builder interface."""

    @abstractmethod
    def add_model(self) -> None:
        pass

    @abstractmethod
    def add_tires(self) -> None:
        pass

    @abstractmethod
    def add_engine(self) -> None:
        pass

    @abstractmethod
    def machine(self) -> Machine:
        pass


class Car(Machine):
    """A car product."""

    def __init__(self) -> None:
        self.model: str = None
        self.tires: str = None
        self.engine: str = None

    def summary(self) -> str:
        return "Car details: {} | {} | {}".format(
            self.model, self.tires, self.engine
        )


class SkyLarkBuilder(Builder):
    """Provides parts and tools to work on the car parts."""

    def __init__(self) -> None:
        self._car: Machine = Car()

    def add_model(self) -> None:
        self._car.model = "SkyBuilder model"

    def add_tires(self) -> None:
        self._car.tires = "Motosport tires"

    def add_engine(self) -> None:
        self._car.engine = "GM Motors engine"

    def machine(self) -> Machine:
        return self._car


class Director:
    """A director. Responsible for `Car` assembling."""

    def __init__(self, builder_: Builder) -> None:
        self._builder: Builder = builder_

    def construct_machine(self) -> None:
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def release_machine(self) -> Machine:
        return self._builder.machine()


builder: Builder = SkyLarkBuilder()
director: Director = Director(builder)
director.construct_machine()
car: Machine = director.release_machine()
print(car.summary())
