from abc import ABC, abstractmethod


class Machine(ABC):
    """Abstract machine product."""

    @abstractmethod
    def model(self) -> str:
        pass

    @abstractmethod
    def tires(self) -> str:
        pass

    @abstractmethod
    def engine(self) -> str:
        pass


class Builder(ABC):
    """Abstract builder."""

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
        self._model = None
        self._tires = None
        self._engine = None

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, model: str) -> None:
        self._model = model

    @property
    def tires(self) -> str:
        return self._tires

    @tires.setter
    def tires(self, tires: str) -> None:
        self._tires = tires

    @property
    def engine(self) -> str:
        return self._engine

    @engine.setter
    def engine(self, engine: str) -> None:
        self._engine = engine

    def __str__(self):
        return '{} | {} | {}'.format(self.model, self.tires, self.engine)


class SkyLarkBuilder(Builder):
    """Concrete Builder --> provides parts and tools to work on the parts."""

    def __init__(self) -> None:
        self._car: Machine = Car()

    def add_model(self) -> None:
        self._car.model = 'SkyBuilder model'

    def add_tires(self) -> None:
        self._car.tires = 'Motosport tires'

    def add_engine(self) -> None:
        self._car.engine = 'GM Motors engine'

    def machine(self) -> Machine:
        return self._car


class Director(object):
    """Director. Responsible for `Car` assembling."""

    def __init__(self, builder: Builder):
        self._builder = builder

    def construct_machine(self) -> None:
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_machine(self) -> Machine:
        return self._builder.machine()


builder: Builder = SkyLarkBuilder()
director: Director = Director(builder)
director.construct_machine()
car: Machine = director.get_machine()
print(car)
