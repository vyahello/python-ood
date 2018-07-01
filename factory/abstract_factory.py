from abc import ABC, abstractmethod


class Pet(ABC):
    """Abstraction of a pet."""

    @abstractmethod
    def speak(self) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class PetFood(ABC):
    """Abstraction of a pet food."""

    @abstractmethod
    def get(self) -> str:
        pass


class PetFactory(ABC):
    """Abstraction of a pet factory."""

    @abstractmethod
    def pet(self) -> Pet:
        pass

    @abstractmethod
    def food(self) -> PetFood:
        pass


class PetStore(ABC):
    """Abstraction of a pet."""

    @abstractmethod
    def show_pet(self) -> str:
        pass


class Dog(Pet):
    """A simple dog class."""

    def __init__(self, name: str) -> None:
        self._name: str = name

    def speak(self) -> str:
        return f'{self._name} says Woof!'

    def __str__(self) -> str:
        return 'Dog'


class DogFood(PetFood):
    """Dog food object."""

    def get(self) -> str:
        return 'Dog food'


class DogFactory(PetFactory):
    """Dog factory."""

    def __init__(self) -> None:
        self._dog: Pet = Dog('Spike')
        self._food: PetFood = DogFood()

    def pet(self) -> Pet:
        """Return dog object."""

        return self._dog

    def food(self) -> PetFood:
        """Return dog food object."""

        return self._food


class Cat(Pet):
    """A simple cat class."""

    def __init__(self, name: str) -> None:
        self._name: str = name

    def speak(self) -> str:
        return f'{self._name} says Moew!'

    def __str__(self) -> str:
        return 'Cat'


class CatFood(PetFood):
    """Cat food object."""

    def get(self) -> str:
        return 'Cat food'


class CatFactory(PetFactory):
    """Dog factory."""

    def __init__(self) -> None:
        self._cat: Pet = Cat('Hope')
        self._food: PetFood = CatFood()

    def pet(self) -> Pet:
        """Return cat object."""

        return self._cat

    def food(self) -> PetFood:
        """Return cat food object."""

        return self._food


class FluffyStore(PetStore):
    """Houses our Abstract Factory."""

    def __init__(self, pet_factory: PetFactory) -> None:
        """pet_factory is our Abstract factory."""

        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the details of the objects returned by the DogFactory."""

        pet: Pet = self._pet_factory.pet()
        pet_food: PetFood = self._pet_factory.food()

        print(f"Our pet is {pet}")
        print(f"Our pet says hello by {pet.speak()}")
        print(f"Its food is {pet_food.get()}")


# Create a Concrete Factory
factory = CatFactory()

# Create a pet store housing our Abstract Factory
shop = FluffyStore(factory)

# Invoke the utility method to show the details of our oet
shop.show_pet()
