# Python OOD
Describes most useful python design patterns.

## Table of contents
- [Creational](#creational)
  - [Factory method](#factory-method)
  - [Abstract factory](#abstract-factory)
  - [Classic singleton](#classic-singleton)
  - [Borg singleton](#borg-singleton)
  - [Builder](#builder)
  - [Prototype](#prototype)
- [Structural](#structural)
  - [Decorator function](#decorator-function)
  - [Decorator class](#decorator-class)
  - [Proxy](#proxy)
- [Behavioral](#behavioral)

## Creational
Used to create objects in a systematic way. Supports flexibility and different subtypes of objects from the same class at runtime. Here polymorphism is often used.
### Factory method
Factory encapsulates objects creation. Factory is an object that is specialized in creation of other objects. 
- Benefits:  
  - Useful when you are not sure what kind of object you will be needed eventually.
  - Application need to decide what class it has to use.
- Exercise:
  - Pet shop is selling dogs but now it sells cats too.
```python
from abc import ABC, abstractmethod


class Pet(ABC):
    """Abstraction of a pet."""

    @abstractmethod
    def speak(self) -> str:
        pass


class Dog(Pet):
    """A simple dog class."""

    def __init__(self, name: str) -> None:
        self._name: str = name

    def speak(self) -> str:
        return f'{self._name} says Woof!'


class Cat(Pet):
    """A simple cat class."""

    def __init__(self, name: str) -> None:
        self._name: str = name

    def speak(self) -> str:
        return f'{self._name} says Meow!'


def get_pet(pet: str) -> Pet:
    """The factory method."""

    return dict(dog=Dog("Hope"), cat=Cat("Faith")).get(pet)


print(get_pet('dog')) # returns Dog("Hope") object
```
### Abstract factory
Client expects to receive family related objects. But dont have to know which family it is until run time. Abstract factory is related to factory method and concrete product are singletons.
- Participants:
  - Abstract factory: pet factory.
  - Concrete factory: dog factory and cat factory.
  - Abstract product.
  - Concrete product: dog and dog food, cat and cat food.
- Exercise:
We have a Pet factory (which includes Dog and Cat factory and both factories produced related products such as Dog and Cat food and we have a PetFactory which gets Cat or Dog factory).

```python
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

        self._pet_factory: PetFactory = pet_factory

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
```
### Classic singleton
Global variable, modules - singleton. Allows only one object to be instantiated from a class template.
If you want to share cached information to multiple objects.
```python
class Singleton(object):
    """Make all instances the same object."""

    def __new__(cls) -> 'Singleton':
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance


# Instantiate the same singleton object
s_one = Singleton()
s_two = Singleton()

print(id(s_one))
print(id(s_two))
print(s_one is s_two)
```
### Borg singleton
```python
from typing import Any


class Borg(object):
    """Borg class making class attributes global.
    Safe the same state of all instances but instances are all different."""

    _shared_state: dict = {}  # Attribute dictionary

    def __init__(self) -> None:
        # Make it an attribute dictionary
        self.__dict__ = self._shared_state


class BorgSingleton(Borg):
    """This class shares all its attribute among its instances. Store the same state."""
    # Makes a singleton an object-oriented global variable

    def __init__(self, **kwargs: Any) -> None:
        Borg.__init__(self)
        # Update the attribute dictionary by inserting a new key-value pair
        self._shared_state.update(kwargs)

    def __str__(self) -> str:
        # Return the attribute dict for printing
        return str(self._shared_state)


# Create a singleton object and add out first acronym
x = BorgSingleton(HTTP='Hyper Text Transfer Protocol')
print(x)

# Create another singleton which will add to the existent dict attribute
y = BorgSingleton(SNMP='Simple Network Management Protocol')
print(y)

```
### Builder
Reduces complexity of building objects.
- Participants:
  - Director.
  - Abstract Builder: interfaces.
  - Concrete Builder: implements the interfaces.
  - Product: object being built.
- Exercise to to build a car object.
```python
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
```
### Prototype
Prototype patterns is related to abstract factory pattern.
- Ideas:
  - Clone objects according to prototypical instance. 
  - Creating many identical objects individually. 
  - Clone individual objects. 
  - Create a prototypical instance first.
- Exercise:
  - Use the same car if car has same color or options, you can clone objects instead of creating individual objects
```python
import copy
from typing import Any, Dict


class Car(object):
    """A car object."""

    def __init__(self) -> None:
        self._name: str = 'Skylar'
        self._color: str = 'Red'
        self._options: str = 'Ex'

    def __str__(self) -> str:
        return '{} | {} | {}'.format(self._name, self._color, self._options)


class Prototype(object):
    """A prototype object."""

    def __init__(self) -> None:
        self._objects: Dict[...] = {}

    def register_object(self, name: str, obj: Car) -> None:
        """Register an object."""

        self._objects[name] = obj

    def unregister_object(self, name: str) -> None:
        """Unregister an object."""

        del self._objects[name]

    def clone(self, name: str, **attr: Any) -> Car:
        """Clone a registered object and update its attributes."""

        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(attr)
        return obj


# Prototypical object to be cloned
car = Car()
prototype = Prototype()
prototype.register_object('skylark', car)

# Clone the object
car1 = prototype.clone('skylark')
print(car1)

```
## Structural
Establish useful relationships between software components. Here inheritance is often used.
### Decorator function
Add new feature to an existing object. Supports dynamic changes.
- Exercise:
  - Add additonal message to an existing function.
```python
from functools import wraps
from typing import Callable


def make_blink(function: Callable[[str], str]) -> Callable[..., str]:
    """Define the decorator."""

    # This makes the decorator transperant in terms of its name and docstring
    @wraps(function)

    # Define the inner function
    def decorator(*args, **kwargs) -> str:

        # Return value of the function being decorated
        ret = function(*args, **kwargs)

        # Add new functionality to the function being decorated
        return f"<blink>{ret}</blink>"

    return decorator

@make_blink
def hello_world(name: str) -> str:
    """Original function!"""

    return f"Hello World said {name}!"


# Decorated function
print(hello_world('James'))

# Check if the function name is still the same name of the function being decorated
print(hello_world.__name__)

# Check if the docstring is still the same name of the function being decorated
print(hello_world.__doc__)
```
### Decorator class
```python
from abc import ABC, abstractmethod


class Int(ABC):
    """Abstraction of and `int` object"""

    @abstractmethod
    def value(self) -> int:
        pass


class ToFloat(object):
    """Decorator object converts `int` datatype into `float` datatype."""

    def __init__(self, int_obj: Int) -> None:
        self._int_obj: Int = int_obj

    def value(self) -> float:
        return float(self._int_obj.value())


class IntA(Int):
    """Int object A."""

    def __init__(self, int_a: int) -> None:
        self._int_a: int = int_a

    def value(self) -> int:
        return self._int_a


class IntB(Int):
    """Int object B."""

    def __init__(self, int_b: int) -> None:
        self._int_b: int = int_b

    def value(self) -> int:
        return self._int_b


class SumFloat:
    """Sum `float` numbers."""

    def __init__(self, int_a: Int, int_b: Int) -> None:
        self._int_a: ToFloat = ToFloat(int_a)
        self._int_b: ToFloat = ToFloat(int_b)

    def value(self) -> float:
        return self._int_a.value() + self._int_b.value()


int_a: Int = IntA(5)
int_b: Int = IntB(6)

sum_f = SumFloat(int_a, int_b)
print(sum_f.value())

```
### Proxy
Postpone object creation unless it is necessary. Object is too expensive (resource intensive) to create that's why we have to create it if it is needed.
- Participants:
  - Producer
  - Artist
  - Guest
- Clients interact with a Proxy. Proxy is responsible for creating the resource intensive objects.
```python
import time


class Producer(object):
    """Define the resource-intensive object to instantiate."""

    def produce(self):
        print('producer is working hard')

    def meet(self):
        print('Producer has time to meet you now')


class Proxy(object):
    """Define the less resource-intensive object to instantiate as a middleman."""

    def __init__(self):
        self._occupied: bool = False

    @property
    def occupied(self) -> bool:
        return self._occupied

    @occupied.setter
    def occupied(self, state: bool) -> None:
        self._occupied = state

    def produce(self) -> None:
        """Check if producer is available."""

        print('Artist checking if producer is available...')

        if not self.occupied:
            # If producer is available, create a producer object!
            producer = Producer()
            time.sleep(2)

            # Make the producer meet the guest!
            producer.meet()
        else:
            # Otherwise don't instantiate a producer
            time.sleep(2)
            print('Producer is busy!')


# Instantiate a Proxy
proxy = Proxy()

# Make the proxy: Artist produce until Producer is available
proxy.produce()

# Change the state to 'occupied'
proxy.occupied = True

# Make the Producer produce
proxy.produce()

```
## Behavioral
Best practices of objects interaction. Methods and signatures are often used.
## Contributing

### Setup
- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `python3.6` is required to run the code
