# Python OOD
Describes most useful python design patterns.

## Table of contents
- [Creational](#creational)
  - [Factory](#factory)
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
  - [Adapter](#adapter)
  - [Composite](#composite)
  - [Bridge](#bridge)
  - [Facade](#facade)
- [Behavioral](#behavioral)
  - [Observer](#observer)
  - [Visitor](#visitor)
  - [Iterator](#iterator)
  - [Strategy](#strategy)
  - [Chain of responsibility](#chain-of-responsibility)
- [Other qualities](#other-qualities)
  - [Completeness](#completeness)
  - [Correctness](#correctness)
  - [Coupling](#)
  - [Cohesion](#)
## Creational
Used to create objects in a systematic way. Supports flexibility and different subtypes of objects from the same class at runtime. Here polymorphism is often used.
### Factory
Define an interface for creating an object but defer object instantiation to run time.
```python
class ShapeInterface(object):
    """Interface that defines the method."""

    def draw(self) -> None:
        raise NotImplementedError


class ShapeError(Exception):
    """Represent shape error message."""
    
    pass


class Circle(ShapeInterface):
    """Concrete shape subclass."""
    
    def draw(self):
        print('Circle.draw')


class Square(ShapeInterface):
    """Concrete shape subclass."""
    
    def draw(self):
        print('Square.draw')


class ShapeFactory(object):
    """Concrete shape factory."""

    def __init__(self, shape: str) -> None:
        self._shape: str = shape

    def get_shape(self):
        if self._shape == 'circle':
            return Circle()
        elif self._shape == 'square':
            return Square()
        raise ShapeError('Could not find shape {shape}')


factory = ShapeFactory(shape='circle')
factory.get_shape().draw()
```
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


class Foo(object):
    """Fancy object."""
    pass


def foo_singleton_factory(_singleton = Foo()) -> Foo:
    """A singleton factory."""
    return _singleton


def singleton(cls):
    """Singleton decorator."""

    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@singleton
class Bar(object):
    """Fancy object."""
    pass


# Instantiate the same singleton object
s_one = Singleton()
s_two = Singleton()

print(id(s_one))
print(id(s_two))
print(s_one is s_two)

# Use singleton factory
a = foo_singleton_factory()
b = foo_singleton_factory()
print(a is b)

# Use singleton decorator
f = Bar()
d = Bar()
print(f is d)
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
- Route maps the user request to a `Controller` which...
- Uses the `Model` to retrieve all of the necessary data, organizes it and send it off to the...
- View, which then uses that data to render the webpage.
### MVC
UI pattern intended to separate internal representation of data from ways it is presented to/accepted from the user.
```python
from abc import ABC, abstractmethod


class Model(ABC):
    """Abstract model defines interfaces."""

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def get(self, item):
        """Returns an object with a .items() call method
        that iterates over key,value pairs of its information."""
        pass

    @abstractmethod
    def item_type(self):
        pass


class View(ABC):
    """Abstract view defines interfaces."""

    @abstractmethod
    def show_item_list(self, item_type, item_list):
        pass

    @abstractmethod
    def show_item_information(self, item_type, item_name, item_info):
        """Will look for item information by iterating over key,value pairs
        yielded by item_info.items()"""
        pass

    @abstractmethod
    def item_not_found(self, item_type, item_name):
        pass


class Controller(ABC):
    """Abstract controller defines interfaces."""

    @abstractmethod
    def show_items(self):
        pass

    @abstractmethod
    def show_item_information(self, item_name):
        pass


class ProductModel(Model):
    """Concrete product model."""

    class Price(float):
        """A polymorphic way to pass a float with a particular
        __str__ functionality."""

        def __str__(self):
            first_digits_str = str(round(self, 2))
            try:
                dot_location = first_digits_str.index('.')
            except ValueError:
                return '{}.00'.format(first_digits_str)
            return '{}{}'.format(first_digits_str, '0' * (3 + dot_location - len(first_digits_str)))

    products = {
        'milk': {'price': Price(1.50), 'quantity': 10},
        'eggs': {'price': Price(0.20), 'quantity': 100},
        'cheese': {'price': Price(2.00), 'quantity': 10}
    }

    @property
    def item_type(self):
        return 'product'

    def __iter__(self):
        for item in self.products:
            yield item

    def get(self, product):
        try:
            return self.products[product]
        except KeyError as e:
            raise KeyError(str(e) + " not in the model's item list.")



class ConsoleView(View):
    """Concrete console view."""

    def show_item_list(self, item_type, item_list):
        print("{} LIST:".format(item_type.upper()))
        for item in item_list:
            print(item)
        print('\n')

    @staticmethod
    def capitalizer(string):
        return '{}{}'.format(string[0].upper(), string[1:].lower())

    def show_item_information(self, item_type, item_name, item_info):
        print('{} INFORMATION:'.format(item_type.upper()))
        printout = 'Name: {}'.format(item_name)
        for key, value in item_info.items():
            printout += ', ' + self.capitalizer(str(key)) + ': ' + str(value)
        printout += '\n'
        print(printout)

    def item_not_found(self, item_type, item_name):
        print('That {} "{}" does not exist in the records'.format(item_type, item_name))


class ItemController(Controller):
    """Concrete item controller."""

    def __init__(self, model, view):
        self._model = model
        self._view = view

    def show_items(self):
        items = list(self._model)
        item_type = self._model.item_type
        self._view.show_item_list(item_type, items)

    def show_item_information(self, item_name):
        try:
            item_info = self._model.get(item_name)
        except KeyError:
            item_type = self._model.item_type
            self._view.item_not_found(item_type, item_name)
        else:
            item_type = self._model.item_type
            self._view.show_item_information(item_type, item_name, item_info)


if __name__ == '__main__':
    model = ProductModel()
    view = ConsoleView()
    controller = ItemController(model, view)
    controller.show_items()
    controller.show_item_information('cheese')
    controller.show_item_information('eggs')
    controller.show_item_information('milk')
    controller.show_item_information('arepas')


### OUTPUT ###
# PRODUCT LIST:
# cheese
# eggs
# milk
#
# PRODUCT INFORMATION:
# Name: Cheese, Price: 2.00, Quantity: 10
#
# PRODUCT INFORMATION:
# Name: Eggs, Price: 0.20, Quantity: 100
#
# PRODUCT INFORMATION:
# Name: Milk, Price: 1.50, Quantity: 10
#
# That product "arepas" does not exist in the records
```
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
### Adapter
Converts interface of a class into another one a client is expecting.
- Exercise:
  - Korean language: speak_korean()
  - British language: speak_english()
  - Client has to have uniform interface - speak method()
- Solution:
  - Use an adapter pattern that translates method name between client and the server code.
```python
class Korean(object):
    """Korean speaker."""

    def __init__(self) -> None:
        self._name: str = 'Korean'

    def name(self) -> str:
        return self._name

    def speak_korean(self) -> str:
        return 'An-neyong?'


class British(object):
    """English speaker"""

    def __init__(self):
        self._name: str = 'British'

    def name(self) -> str:
        return self._name

    # Note the difference method name here!
    def speak_english(self) -> str:
        return 'Hello'


class Adapter(object):
    """Change the generic method name to individualized method names."""

    def __init__(self, obj, **adapted_method) -> None:
        """Change the name of method."""
        self._object = obj

        # Add a new dictionary item that establishes the mapping between the generic method name: speak() and the concrete method
        # For example, speak() will be translated to speak_korean() is the mapping says so

        self.__dict__.update(adapted_method)

    def __getattr__(self, item):
        """Return the rest of attributes!"""

        return getattr(self._object, item)


# List to store speaker objects
objects: list = []

# Create a Korean object
korean = Korean()

# Create a British object
british = British()

# Append the object to the objects list, dynamically
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for o in objects:
    print(f"{o.name()} says '{o.speak()}'\n")

```
### Composite
- Exercise:
  - Build recursive tree data structure. (Menu > submenu > sub-submenu > ...)
- Participants:
  - Component - abstract 'class'
  - Child - inherits from Component 'class'
  - Composite - inherits from component 'class'. Maintain child objects by adding.removing them.
```python
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """Abstract class"""

    @abstractmethod
    def component_function(self):
        pass


class Child(Component):
    """Concrete class."""

    def __init__(self, *args: str) -> None:

        # We store the name of your chile item.
        self._args: str = args

    def name(self) -> str:
        return self._args[0]

    def component_function(self) -> None:
        # Print the name of your chile item here!
        print('{}'.format(self.name()))


class Composite(Component):
    """Concrete class and maintains the tree recursive structure."""

    def __init__(self, *args: str):

        # Name of the composite object
        self._args: str = args

        # Keep our child items
        self.children: List[...] = []

    def name(self) -> str:
        return self._args[0]

    def append_child(self, child: Component) -> None:
        """Method to add a new child item."""
        self.children.append(child)

    def remove_child(self, child: Component) -> None:
        """Method to remove a child item."""
        self.children.remove(child)

    def component_function(self) -> None:
        # Print name of the composite object
        print('{}'.format(self.name()))

        # Iterate through the child objects and invoke their component function printing their names
        for child in self.children:
            child.component_function()


# Build a composite submenu 1
sub1 = Composite('submenu1')

# Create a new child submenu 11
sub11 = Child('sub_submenu 11')

# Create a new child submenu 12
sub12 = Child('sub_submenu 12')

# Add the sub_submenu 11 to submenu 1
sub1.append_child(sub11)

# Add the sub_submenu 12 to submenu 1
sub1.append_child(sub12)

# Build a top-level composite menu
top = Composite('top_menu')

# Build a submenu 2 that is not a composite
sub2 = Child('submenu2')

# Add the composite submenu 1 to the top-level composite menu
top.append_child(sub1)

# Add the plain submenu 2 to the top-level composite menu
top.append_child(sub2)

# Lets's test is our Composite pattern works!
top.component_function()

```
### Bridge
Separates the abstraction into different class hierarchies. Abstract factory and adapter patterns are related to this Bridge design pattern.
```python
from abc import ABC, abstractmethod


class DrawAPI(ABC):
    """Provide `draw_circle()` interface for child objects."""

    @abstractmethod
    def draw_circle(self, x: int, y: int, radius: int) -> None:
        pass


class Circle(ABC):
    """Provide two interfaces `draw()` and `scale` interfaces for child objects."""

    @abstractmethod
    def draw(self) -> None:
        pass

    @abstractmethod
    def scale(self, percent: int) -> None:
        pass


class DrawAPIOne(DrawAPI):
    """Implementation-specific abstraction: concrete class one."""

    def draw_circle(self, x: int, y: int, radius: int) -> None:
        print("API 1 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))


class DrawAPITwo(DrawAPI):
    """Implementation-specific abstraction: concrete class two."""

    def draw_circle(self,  x: int, y: int, radius: int) -> None:
        print("API 2 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))


class DrawCircle(object):
    """Implementation-independent abstraction: e.g there could be a rectangle class!."""

    def __init__(self, x: int, y: int, radius: int, draw_api: DrawAPI) -> None:
        """Initialize the necessary attributes."""
        self._x: int = x
        self._y: int = y
        self._radius: int = radius
        self._draw_api: DrawAPI = draw_api


    def draw(self) -> None:
        """Implementation-specific abstraction taken care of another class: DrawAPI."""

        self._draw_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent: int) -> None:
        """Implementation-independent."""

        self._radius *= percent


# Build the first Circle object using API One
circle1: Circle = DrawCircle(1, 2, 3, DrawAPIOne())

# Draw a circle
circle1.draw()

# Build the second Circle object sing APi Two
circle2: Circle = DrawCircle(3, 4, 6, DrawAPITwo())

# Draw a circle
circle2.draw()

```
### Facade
The Facade pattern is a way to provide a simpler unified interface to a more complex system. It provides an easier way to access functions of the underlying system by providing a single entry point.
```python
from abc import ABC, abstractmethod
import time
from typing import Iterator, Tuple

_sleep: float = 0.2


class TestCase(ABC):
    """Abstraction provides `run()` interface."""

    @abstractmethod
    def run(self) -> None:
        """Abstract interface that has to be reused by child objects."""
        pass


# Complex Parts
class TestCase1(TestCase):
    """Concrete test case."""

    def __init__(self, name: str) -> None:
        self._name: str = name

    def run(self) -> None:
        print('{:#^20}'.format(self._name))
        time.sleep(_sleep)
        print("Setting up")
        time.sleep(_sleep)
        print("Running test")
        time.sleep(_sleep)
        print("Tearing down")
        time.sleep(_sleep)
        print("Test Finished\n")


class TestCase2(TestCase):
    """Concrete test case."""

    def __init__(self, name: str) -> None:
        self._name: str = name

    def run(self) -> None:
        print('{:#^20}'.format(self._name))
        time.sleep(_sleep)
        print("Setting up")
        time.sleep(_sleep)
        print("Running test")
        time.sleep(_sleep)
        print("Tearing down")
        time.sleep(_sleep)
        print("Test Finished\n")


class TestCase3(TestCase):
    """Concrete test case."""

    def __init__(self, name: str) -> None:
        self._name: str = name

    def run(self) -> None:
        print('{:#^20}'.format(self._name))
        time.sleep(_sleep)
        print("Setting up")
        time.sleep(_sleep)
        print("Running test")
        time.sleep(_sleep)
        print("Tearing down")
        time.sleep(_sleep)
        print("Test Finished\n")


# Facade
class TestRunner(object):
    """Represent simpler unified interface to run all test cases."""

    def __init__(self) -> None:
        self._tcs: Tuple[TestCase] = (TestCase1('Test Case 1'),
                                      TestCase2('Test Case 2'),
                                      TestCase3('Test Case 3'))

    def _tests(self) -> Iterator[TestCase]:
        yield from self._tcs

    def run(self) -> None:
        c = 0
        tests = self._tests()
        while c < len(self._tcs):
            next(tests).run()
            c += 1


# Client
class Client(object):
    """Client runner."""

    def __init__(self) -> None:
        self._runner: TestRunner = TestRunner()

    def run(self) -> None:
        self._runner.run()


if __name__ ==  '__main__':
    client: Client = Client()
    client.run()

```
```python
from typing import Tuple, Iterator
import abc


class Interface(abc.ABC):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def run(self) -> str:
        pass


class A(Interface):
    """Implement interface."""

    def run(self) -> str:
        return 'A.run()'


class B(Interface):
    """Implement interface."""

    def run(self) -> str:
        return 'B.run()'


class C(Interface):
    """Implement interface."""

    def run(self) -> str:
        return 'C.run()'


class Facade(Interface):
    """Facade object."""

    def __init__(self):
        self._all: Tuple[Interface] = (A, B, C)

    def run(self) -> Iterator[Interface]:
        for obj in self._all:
            yield obj


if __name__ == '__main__':
    lst = [cls().run() for cls in Facade().run()]
    print(*lst)
```
## Behavioral
Best practices of objects interaction. Methods and signatures are often used.
### Observer
Establishes one yo many relationship between subject and multiple observers. Singleton is related to observer design pattern.
- Exercise:
  - Subjects need to be monitored.
  - Observers need to be notified.
- Participants:
  - Subject: abstract class
    - Attach
    - Detach
    - Notify
  - Concrete Subjects
```python
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
```
### Visitor
Add new features to existing hierarchy without changing it. Add new operations to existing classes dynamically.
Exercise:
  - House class:
    - HVAC specialist: Visitor type 1
    - Electrician: Visitor type 2
```python
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

```
### Iterator
Composite pattern is related to iterator pattern.
- Exercise:
  - Our custom iterator based on a build-in python iterator: `zip()`.
  - Will iterate over a certain point baed on client input.

```python
from typing import Iterator


class IteratorSequence(object):
    """Represent iterator sequence object."""

    def __init__(self, capacity: int) -> None:
        self._rng: Iterator[int] = iter(range(capacity))

    def __next__(self) -> int:
        return next(self._rng)

    def __iter__(self) -> Iterator[int]:
        return self


iterator = IteratorSequence(capacity=10)

for _ in range(10):
    print(next(iterator))
```

```python
from typing import Iterator, Tuple


def count_to(count: int) -> Iterator[Tuple[int, str]]:
    """Our iterator implementation."""

    # Our list
    number_in_german = ['einn', 'zwei', 'drei', 'veir', 'funf']

    # Our built-in iterator
    # Creates a tuple as (1, 'eins')
    iterator = zip(range(1, count + 1), number_in_german)

    # Iterate through our iterable list
    # Extract the German numbers
    # Out them in a generator called number
    for position, number in iterator:

        # Return a 'generator' containing numbers in German
        yield position, number


# Let's test the generator returned by our iterator
for num in count_to(3):
    print("{} in german is {}".format(*num))

```
### Strategy
Dynamically changing the behavior of an object. Add dynamically objects with `types` module.
- Participants:
  - Abstract strategy class with default set of behaviors
  - Concrete strategy class with new behaviors
```python
import types
from typing import Callable, Any


class Strategy(object):
    """The strategy pattern class."""

    def __init__(self, func: Callable[['Strategy'], Any] = None) -> None:
        self._name = "Default strategy"

        # If a reference to a function is provided, replace the execute() method with the given function
        if func:
            self.execute = types.MethodType(func, self)  # dynamically add a new method to a class

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    def execute(self):  # gets replace by another version if another strategy is provided.
        print("{} is used".format(self._name))


# Replacement method 1
def strategy_one(strategy: Strategy) -> None:
    print("{} is used to execute method 1".format(strategy.name))

# Replacement method 2
def strategy_two(strategy: Strategy) -> None:
    print("{} is used to execute method 2".format(strategy.name))


# Default strategy
s0 = Strategy()

# Execute our default strategy
s0.execute()

# Let'screate the first variation of our default strategy by providing a new behavior
s1 = Strategy(func=strategy_one)

# Set it's name
s1.name = 'Strategy one'

# Execute the strategy
s1.execute()

s2 = Strategy(func=strategy_two)
s2.name = 'Strategy two'
s2.execute()
```
### Chain of responsibility
Decouple responsibility. Composite is related to this design pattern.
- Exercise:
  - Integer value
  - Handlers
    - Find out its range
- Participants:
  - Abstract handler
    - Successor
  - Concrete Handler
    - Checks if it can handle the request
```python
from abc import abstractmethod
from typing import List


class Handler(object):
    """Abstract handler."""

    def __init__(self, successor: 'Handler') -> None:
        # Define who is the next handler
        self._successor: Handler = successor

    def handler(self, request: int) -> None:
        # If handled, stop here otherwise, keep going

        if not self.handle(request):
            self._successor.handler(request)

    @abstractmethod
    def handle(self, request: int) -> None:
        pass


class ConcreteHandler1(Handler):
    """Concrete handler 1."""

    def handle(self, request: int) -> bool:
        if 0 < request <= 10:
            print("Request {} handled in handler 1".format(request))
            return True  # Indicated that request has been handled


class DefaultHandler(Handler):
    """Default handler."""

    def handle(self, request: int) -> bool:
        """If there is no handler available."""
        # No condition as this is a default handler
        print("End of chain, no handler for {}".format(request))
        return True # Indicated that request has been handled


class Client(object):
    """Using handlers."""

    def __init__(self) -> None:
        self._handler: Handler = ConcreteHandler1(DefaultHandler(None))

        # Create handlers and use them in a sequence you want
        # Note that the default handler has no successor

    def delegate(self, requests: List[int]) -> None:  # Send a request one at a time for handlers to handle
        for request in requests:
            self._handler.handler(request)


# Create a client
c = Client()

# Create requests
requests = [2, 5, 30]

# Send the request
c.delegate(requests)
```
## Other qualities
### Completeness
Depends on how much the software solution meets its requirements.
### Correctness
Make the software without errors.
### Coupling
How much different elements of a software are related. If there is strong coupling changes in one element affects another. Less coupling is desirable.
### Cohesion
Refers to how independent the software component is. More cohesion is better.
## Contributing

### Setup
- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `python3.6` is required to run the code
