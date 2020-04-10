![Screenshot](logo.png)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with pylint](https://img.shields.io/badge/pylint-checked-blue)](https://www.pylint.org)
[![Build Status](https://api.travis-ci.org/vyahello/python-ood.svg?branch=master)](https://travis-ci.org/vyahello/python-ood)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/python-ood/badge.svg?branch=master)](https://coveralls.io/github/vyahello/python-ood?branch=master)
[![Stars](https://img.shields.io/github/stars/vyahello/python-ood)](https://github.com/vyahello/python-ood/stargazers)
[![Issues](https://img.shields.io/github/issues/vyahello/python-ood)](https://github.com/vyahello/python-ood/issues)
[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![Hits-of-Code](https://hitsofcode.com/github/vyahello/python-ood)](https://hitsofcode.com/view/github/vyahello/python-ood)
[![CodeFactor](https://www.codefactor.io/repository/github/vyahello/python-ood/badge)](https://www.codefactor.io/repository/github/vyahello/python-ood)

# Python OOD
> Describes most useful python object oriented design patterns.

**Tools**
- `python 3.6+` basis
- `pylint` code analyser
- `black` code formatter
- `travis CI`

Source code is fully type annotated ⭐

## Table of contents
- [Creational](#creational)
  - [Factory method](#factory-method)
  - [Abstract factory](#abstract-factory)
  - [Singleton](#singleton)
  - [Builder](#builder)
  - [Prototype](#prototype)
- [Structural](#structural)
  - [Decorator](#decorator)
  - [Proxy](#proxy)
  - [Adapter](#adapter)
  - [Composite](#composite)
  - [Bridge](#bridge)
  - [Facade](#facade)
- [Behavioral](#behavioral)
  - [MVC](#mvc)
  - [Observer](#observer)
  - [Visitor](#visitor)
  - [Iterator](#iterator)
  - [Strategy](#strategy)
  - [Chain of responsibility](#chain-of-responsibility)
- [Other qualities](#other-qualities)
- [Development notes](#development-notes)
  - [Code analysis](#code-analysis)
  - [Release notes](#release-notes)
  - [Meta](#meta)
  - [Contributing](#contributing)

## Creational
Creational types of patterns used to create objects in a systematic way. Supports flexibility and different subtypes of objects from the same class at runtime. 
Here **polymorphism** is often used.

### Factory method
Factory method defines an interface for creating an object but defers object instantiation to run time.
```python
from abc import ABC, abstractmethod


class Shape(ABC):
    """Defines a shape interface."""

    @abstractmethod
    def draw(self) -> str:
        pass


class ShapeError(Exception):
    """Represents shape error message."""

    pass


class Circle(Shape):
    """A shape subclass."""

    def draw(self) -> str:
        return "Circle.draw"


class Square(Shape):
    """A shape subclass."""

    def draw(self) -> str:
        return "Square.draw"


class ShapeFactory:
    """A shape factory."""

    def __init__(self, shape: str) -> None:
        self._shape: str = shape

    def get_shape(self) -> Shape:
        if self._shape == "circle":
            return Circle()
        if self._shape == "square":
            return Square()
        raise ShapeError(f'Could not find "{self._shape}" shape!')


# circle shape
factory: ShapeFactory = ShapeFactory(shape="circle")
circle: Shape = factory.get_shape()
print(circle.__class__.__name__)
print(circle.draw())

# square shape
factory: ShapeFactory = ShapeFactory(shape="square")
square: Shape = factory.get_shape()
print(square.__class__.__name__)
print(square.draw())
```
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
        """Interface for a pet to speak."""
        pass


class Dog(Pet):
    """A simple dog class."""

    def __init__(self, name: str) -> None:
        self._dog_name: str = name

    def speak(self) -> str:
        return f"{self._dog_name} says Woof!"


class Cat(Pet):
    """A simple cat class."""

    def __init__(self, name: str) -> None:
        self._cat_name: str = name

    def speak(self) -> str:
        return f"{self._cat_name} says Meow!"


def get_pet(pet: str) -> Pet:
    """The factory method."""
    return {"dog": Dog("Hope"), "cat": Cat("Faith")}[pet]


# returns Cat class object
get_pet("cat")
```
**[⬆ back to top](#table-of-contents)**

### Abstract factory
In abstract factory a client expects to receive family related objects. But don't have to know which family it is until run time. Abstract factory is related to factory method and concrete product are singletons.
- Implementation idea:
  - Abstract factory: pet factory
  - Concrete factory: dog factory and cat factory
  - Abstract product
  - Concrete product: dog and dog food, cat and cat food
- Exercise:
  - We have a Pet factory (which includes Dog and Cat factory and both factories produced related products such as Dog and Cat food and we have a PetFactory which gets Cat or Dog factory).

```python
from abc import ABC, abstractmethod
from typing import Generator


class Pet(ABC):
    """Abstract interface of a pet."""

    @abstractmethod
    def speak(self) -> str:
        pass

    @abstractmethod
    def type(self) -> str:
        pass


class Food(ABC):
    """Abstract interface of a food."""

    @abstractmethod
    def show(self) -> str:
        pass


class PetFactory(ABC):
    """Abstract interface of a pet factory."""

    @abstractmethod
    def pet(self) -> Pet:
        pass

    @abstractmethod
    def food(self) -> Food:
        pass


class PetStore(ABC):
    """Abstract interface of a pet store."""

    @abstractmethod
    def show_pet(self) -> str:
        pass


class Dog(Pet):
    """A dog pet."""

    def __init__(self, name: str, type_: str) -> None:
        self._name: str = name
        self._type: str = type_

    def speak(self) -> str:
        return f'"{self._name}" says Woof!'

    def type(self) -> str:
        return f"{self._type} dog"


class DogFood(Food):
    """A dog food."""

    def show(self) -> str:
        return "Pedigree"


class DogFactory(PetFactory):
    """A dog factory."""

    def __init__(self) -> None:
        self._dog: Pet = Dog(name="Spike", type_="bulldog")
        self._food: Food = DogFood()

    def pet(self) -> Pet:
        return self._dog

    def food(self) -> Food:
        return self._food


class Cat(Pet):
    """A cat pet."""

    def __init__(self, name: str, type_: str) -> None:
        self._name: str = name
        self._type: str = type_

    def speak(self) -> str:
        return f'"{self._name}" says Moew!'

    def type(self) -> str:
        return f"{self._type} cat"


class CatFood(Food):
    """A cat food."""

    def show(self) -> str:
        return "Whiskas"


class CatFactory(PetFactory):
    """A dog factory."""

    def __init__(self) -> None:
        self._cat: Pet = Cat(name="Hope", type_="persian")
        self._food: Food = CatFood()

    def pet(self) -> Pet:
        return self._cat

    def food(self) -> Food:
        return self._food


class FluffyStore(PetStore):
    """Houses our abstract pet factory."""

    def __init__(self, pet_factory: PetFactory) -> None:
        self._pet: Pet = pet_factory.pet()
        self._pet_food: Food = pet_factory.food()

    def show_pet(self) -> Generator[str, None, None]:
        yield f"Our pet is {self._pet.type()}"
        yield f"{self._pet.type()} {self._pet.speak()}"
        yield f"It eats {self._pet_food.show()} food"



# cat factory
cat_factory: PetFactory = CatFactory()
store: PetStore = FluffyStore(cat_factory)
print(tuple(store.show_pet()))

# dog factory
dog_factory: PetFactory = DogFactory()
store: PetStore = FluffyStore(dog_factory)
print(tuple(store.show_pet()))
```
**[⬆ back to top](#table-of-contents)**

### Singleton
Python has global variables and modules which are **_singletons_**. Singleton allows only one object to be instantiated from a class template.
Useful if you want to share cached information to multiple objects.

**Classic singleton**
```python
from typing import Any, Dict


class Singleton:
    """Makes all instances as the same object."""

    def __new__(cls) -> "Singleton":
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance


def singleton(cls: Any) -> Any:
    """A singleton decorator."""
    instances: Dict[Any, Any] = {}

    def get_instance() -> Any:
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instance


@singleton
class Bar:
    """A fancy object."""

    pass


singleton_one: Singleton = Singleton()
singleton_two: Singleton = Singleton()

print(id(singleton_one))
print(id(singleton_two))
print(singleton_one is singleton_two)

bar_one: Bar = Bar()
bar_two: Bar = Bar()
print(id(bar_one))
print(id(bar_two))
print(bar_one is bar_two)
```

**Borg singleton**
```python
from typing import Dict, Any


class Borg:
    """Borg class making class attributes global.
    Safe the same state of all instances but instances are all different."""

    _shared_state: Dict[Any, Any] = {}

    def __init__(self) -> None:
        self.__dict__ = self._shared_state


class BorgSingleton(Borg):
    """This class shares all its attribute among its instances. Store the same state."""

    def __init__(self, **kwargs: Any) -> None:
        Borg.__init__(self)
        self._shared_state.update(kwargs)

    def __str__(self) -> str:
        return str(self._shared_state)


# Create a singleton object and add out first acronym
x: Borg = BorgSingleton(HTTP="Hyper Text Transfer Protocol")
print(x)

# Create another singleton which will add to the existent dict attribute
y: Borg = BorgSingleton(SNMP="Simple Network Management Protocol")
print(y)
```
**[⬆ back to top](#table-of-contents)**

### Builder
Builder reduces complexity of building objects.
- Participants:
  - Director
  - Abstract Builder: interfaces
  - Concrete Builder: implements the interfaces
  - Product: object being built
- Exercise:
  - Build a car object
```python
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
        return "Car details: {} | {} | {}".format(self.model, self.tires, self.engine)


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
```
**[⬆ back to top](#table-of-contents)**

### Prototype
Prototype patterns are related to abstract factory pattern.
- Ideas:
  - Clone objects according to prototypical instance.
  - Creating many identical objects individually.
  - Clone individual objects
  - Create a prototypical instance first
- Exercise:
  - Use the same car if car has same color or options, you can clone objects instead of creating individual objects

```python
import copy
from abc import ABC, abstractmethod
from typing import Dict, Any


class Machine(ABC):
    """Abstract machine interface."""

    @abstractmethod
    def summary(self) -> str:
        pass


class Car(Machine):
    """A car object."""

    def __init__(self) -> None:
        self._name: str = "Skylar"
        self._color: str = "Red"
        self._options: str = "Ex"

    def summary(self) -> str:
        return "Car details: {} | {} | {}".format(self._name, self._color, self._options)


class Prototype:
    """A prototype object."""

    def __init__(self) -> None:
        self._elements: Dict[Any, Any] = {}

    def register_object(self, name: str, machine: Machine) -> None:
        self._elements[name] = machine

    def unregister_object(self, name: str) -> None:
        del self._elements[name]

    def clone(self, name: str, **attr: Any) -> Car:
        obj: Any = copy.deepcopy(self._elements[name])
        obj.__dict__.update(attr)
        return obj


# prototypical car object to be cloned
primary_car: Machine = Car()
print(primary_car.summary())
prototype: Prototype = Prototype()
prototype.register_object("skylark", primary_car)

# clone a car object
cloned_car: Machine = prototype.clone("skylark")
print(cloned_car.summary())
```
**[⬆ back to top](#table-of-contents)**

## Structural
Structural type of patterns establish useful relationships between software components. Here **_inheritance_** is often used.
- Ideas:
  - Route maps the user request to a `Controller` which...
  - Uses the `Model` to retrieve all of the necessary data, organizes it and send it off to the...
  - View, which then uses that data to render the web page

**[⬆ back to top](#table-of-contents)**

### MVC
MVC (Model-View-Controller) is a UI pattern intended to separate internal representation of data from ways it is presented to/from the user.

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Iterator, Any


class Model(ABC):
    """Abstract model defines interfaces."""

    @abstractmethod
    def __iter__(self) -> Iterator[str]:
        pass

    @abstractmethod
    def get(self, item: str) -> Dict[str, int]:
        """Returns an object with a .items() call method
        that iterates over key,value pairs of its information."""
        pass

    @property
    @abstractmethod
    def item_type(self) -> str:
        pass


class View(ABC):
    """Abstract view defines interfaces."""

    @abstractmethod
    def show_item_list(self, item_type: str, item_list: List[str]) -> None:
        pass

    @abstractmethod
    def show_item_information(self, item_type: str, item_name: str, item_info: List[str]) -> None:
        """Will look for item information by iterating over key,value pairs yielded by item_info.items()."""
        pass

    @abstractmethod
    def item_not_found(self, item_type: str, item_name: str) -> None:
        pass


class Controller(ABC):
    """Abstract controller defines interfaces."""

    @abstractmethod
    def show_items(self):
        pass

    @abstractmethod
    def show_item_information(self, item_name: str) -> None:
        pass


class ProductModel(Model):
    """Concrete product model."""

    class Price(float):
        """A polymorphic way to pass a float with a particular
        __str__ functionality."""

        def __str__(self) -> str:
            first_digits_str: str = str(round(self, 2))
            try:
                dot_location: int = first_digits_str.index(".")
            except ValueError:
                return f"{first_digits_str}.00"
            return f"{first_digits_str}{'0' * (3 + dot_location - len(first_digits_str))}"

    products: Dict[str, Dict[str, Any]] = {
        "milk": {"price": Price(1.50), "quantity": 10},
        "eggs": {"price": Price(0.20), "quantity": 100},
        "cheese": {"price": Price(2.00), "quantity": 10},
    }

    @property
    def item_type(self) -> str:
        return "product"

    def __iter__(self) -> Iterator[str]:
        for item in self.products:  # type: str
            yield item

    def get(self, item: str) -> Dict[str, int]:
        try:
            return self.products[item]
        except KeyError as e:
            raise KeyError(str(e) + " not in the model's item list.")


class ConsoleView(View):
    """Concrete console view."""

    def show_item_list(self, item_type: str, item_list: Dict[str, Any]) -> None:
        print("{} LIST:".format(item_type.upper()))
        for item in item_list:
            print(item)
        print("\n")

    @staticmethod
    def capitalizer(string: str) -> str:
        return f"{string[0].upper()}{ string[1:].lower()}"

    def show_item_information(self, item_type: str, item_name: str, item_info: Dict[str, int]) -> None:
        print(f"{item_type.upper()} INFORMATION:")
        printout: str = f"Name: {item_name}"
        for key, value in item_info.items():
            printout += ", " + self.capitalizer(str(key)) + ": " + str(value)
        printout += "\n"
        print(printout)

    def item_not_found(self, item_type: str, item_name: str) -> None:
        print(f'That "{item_type}" "{item_name}" does not exist in the records')


class ItemController(Controller):
    """Concrete item controller."""

    def __init__(self, item_model: Model, item_view: View) -> None:
        self._model = item_model
        self._view = item_view

    def show_items(self) -> None:
        items: List = list(self._model)
        item_type: str = self._model.item_type
        self._view.show_item_list(item_type, items)

    def show_item_information(self, item_name: str) -> None:
        try:
            item_info: Dict[str, Any] = self._model.get(item_name)
        except KeyError:
            item_type: str = self._model.item_type
            self._view.item_not_found(item_type, item_name)
        else:
            item_type: str = self._model.item_type
            self._view.show_item_information(item_type, item_name, item_info)


if __name__ == "__main__":
    model: Model = ProductModel()
    view: View = ConsoleView()
    controller: ItemController = ItemController(model, view)
    controller.show_items()
    controller.show_item_information("cheese")
    controller.show_item_information("eggs")
    controller.show_item_information("milk")
    controller.show_item_information("arepas")


# OUTPUT #
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
**[⬆ back to top](#table-of-contents)**

### Decorator
Decorator type of patterns add new feature to an existing object. Supports dynamic changes.
- Exercise:
  - Add additional message to an existing function

**Decorator function**
```python
from functools import wraps
from typing import Callable


def make_blink(function: Callable[[str], str]) -> Callable[..., str]:
    """Defines the decorator function."""

    @wraps(function)
    def decorator(*args, **kwargs) -> str:
        result: str = function(*args, **kwargs)
        return f"<blink>{result}</blink>"

    return decorator


@make_blink
def hello_world(name: str) -> str:
    """Original function."""
    return f'Hello World said "{name}"!'


print(hello_world(name="James"))
print(hello_world.__name__)
print(hello_world.__doc__)
```

**Decorator class**
```python
from abc import ABC, abstractmethod


class Number(ABC):
    """Abstraction of a number object."""

    @abstractmethod
    def value(self) -> int:
        pass


class Integer(Number):
    """A subclass of a number."""

    def __init__(self, value: int) -> None:
        self._value = value

    def value(self) -> int:
        return self._value


class Float(Number):
    """Decorator object converts `int` datatype into `float` datatype."""

    def __init__(self, number: Number) -> None:
        self._number: Number = number

    def value(self) -> float:
        return float(self._number.value())


class SumOfFloat(Number):
    """Sum of two `float` numbers."""

    def __init__(self, one: Number, two: Number) -> None:
        self._one: Float = Float(one)
        self._two: Float = Float(two)

    def value(self) -> float:
        return self._one.value() + self._two.value()


integer_one: Number = Integer(value=5)
integer_two: Number = Integer(value=6)
sum_float: Number = SumOfFloat(integer_one, integer_two)
print(sum_float.value())
```
**[⬆ back to top](#table-of-contents)**

### Proxy
Proxy patterns postpones object creation unless it is necessary. Object is too expensive (resource intensive) to create that's why we have to create it once it is needed.
- Participants:
  - Producer
  - Artist
  - Guest
- Clients interact with a Proxy. Proxy is responsible for creating the resource intensive objects

```python
import time


class Producer:
    """Defines the resource-intensive object to instantiate."""

    def produce(self) -> None:
        print("Producer is working hard!")

    def meet(self) -> None:
        print("Producer has time to meet you now")


class Proxy:
    """Defines the less resource-intensive object to instantiate as a middleman."""

    def __init__(self):
        self._occupied: bool = False

    @property
    def occupied(self) -> bool:
        return self._occupied

    @occupied.setter
    def occupied(self, state: bool) -> None:
        if not isinstance(state, bool):
            raise ValueError(f'"{state}" value should be a boolean data type!')
        self._occupied = state

    def produce(self) -> None:
        print("Artist checking if producer is available ...")
        if not self.occupied:
            producer: Producer = Producer()
            time.sleep(2)
            producer.meet()
        else:
            time.sleep(2)
            print("Producer is busy!")


proxy: Proxy = Proxy()
proxy.produce()
proxy.occupied = True
proxy.produce()
```
**[⬆ back to top](#table-of-contents)**

### Adapter
Adapter patterns converts interface of a class into another one a client is expecting.
- Exercise:
  - Korean language: `speak_korean()`
  - British language: `speak_english()`
  - Client has to have uniform interface - `speak method`
- Solution:
  - Use an adapter pattern that translates method name between client and the server code

```python
from abc import ABC, abstractmethod
from typing import Any


class Speaker(ABC):
    """Abstract interface for some speaker."""

    @abstractmethod
    def type(self) -> str:
        pass


class Korean(Speaker):
    """Korean speaker."""

    def __init__(self) -> None:
        self._type: str = "Korean"

    def type(self) -> str:
        return self._type

    def speak_korean(self) -> str:
        return "An-neyong?"


class British(Speaker):
    """English speaker."""

    def __init__(self):
        self._type: str = "British"

    def type(self) -> str:
        return self._type

    def speak_english(self) -> str:
        return "Hello"


class Adapter:
    """Changes the generic method name to individualized method names."""

    def __init__(self, obj: Any, **adapted_method: Any) -> None:
        self._object = obj
        self.__dict__.update(adapted_method)

    def __getattr__(self, item: Any) -> Any:
        return getattr(self._object, item)


speakers: list = []
korean = Korean()
british = British()
speakers.append(Adapter(korean, speak=korean.speak_korean))
speakers.append(Adapter(british, speak=british.speak_english))

for speaker in speakers:
    print(f"{speaker.type()} says '{speaker.speak()}'")
```
**[⬆ back to top](#table-of-contents)**

### Composite
- Exercise:
  - Build recursive tree data structure. (Menu > submenu > sub-submenu > ...)
- Participants:
  - Component - abstract 'class'
  - Child - inherits from Component 'class'
  - Composite - inherits from component 'class'. Maintain child objects by adding.removing them

```python
from abc import ABC, abstractmethod
from typing import Sequence, List


class Component(ABC):
    """Abstract interface of some component."""

    @abstractmethod
    def function(self) -> None:
        pass


class Child(Component):
    """Concrete child component."""

    def __init__(self, *args: str) -> None:
        self._args: Sequence[str] = args

    def name(self) -> str:
        return self._args[0]

    def function(self) -> None:
        print(f'"{self.name()}" component')


class Composite(Component):
    """Concrete class maintains the tree recursive structure."""

    def __init__(self, *args: str) -> None:
        self._args: Sequence[str] = args
        self._children: List[Component] = []

    def name(self) -> str:
        return self._args[0]

    def append_child(self, child: Component) -> None:
        self._children.append(child)

    def remove_child(self, child: Component) -> None:
        self._children.remove(child)

    def function(self) -> None:
        print(f'"{self.name()}" component')
        for child in self._children:  # type: Component
            child.function()


top_menu = Composite("top_menu")

submenu_one = Composite("submenu one")
child_submenu_one = Child("sub_submenu one")
child_submenu_two = Child("sub_submenu two")
submenu_one.append_child(child_submenu_one)
submenu_one.append_child(child_submenu_two)

submenu_two = Child("submenu two")
top_menu.append_child(submenu_one)
top_menu.append_child(submenu_two)
top_menu.function()
```
**[⬆ back to top](#table-of-contents)**

### Bridge
Bridge pattern separates the abstraction into different class hierarchies. 
Abstract factory and adapter patterns are related to Bridge design pattern.

```python
from abc import ABC, abstractmethod


class DrawApi(ABC):
    """Provides draw interface."""

    @abstractmethod
    def draw_circle(self, x: int, y: int, radius: int) -> None:
        pass


class Circle(ABC):
    """Provides circle shape interface."""

    @abstractmethod
    def draw(self) -> None:
        pass

    @abstractmethod
    def scale(self, percentage: int) -> None:
        pass


class DrawApiOne(DrawApi):
    """Implementation-specific abstraction: concrete class one."""

    def draw_circle(self, x: int, y: int, radius: int) -> None:
        print(f"API 1 drawing a circle at ({x}, {y} with radius {radius}!)")


class DrawApiTwo(DrawApi):
    """Implementation-specific abstraction: concrete class two."""

    def draw_circle(self, x: int, y: int, radius: int) -> None:
        print(f"API 2 drawing a circle at ({x}, {y} with radius {radius}!)")


class DrawCircle(Circle):
    """Implementation-independent abstraction: e.g there could be a rectangle class!."""

    def __init__(self, x: int, y: int, radius: int, draw_api: DrawApi) -> None:
        self._x: int = x
        self._y: int = y
        self._radius: int = radius
        self._draw_api: DrawApi = draw_api

    def draw(self) -> None:
        self._draw_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percentage: int) -> None:
        if not isinstance(percentage, int):
            raise ValueError(f'"{percentage}" value should be an integer data type!')
        self._radius *= percentage


circle_one: Circle = DrawCircle(1, 2, 3, DrawApiOne())
circle_one.draw()
circle_two: Circle = DrawCircle(3, 4, 6, DrawApiTwo())
circle_two.draw()
```
**[⬆ back to top](#table-of-contents)**

### Facade
The Facade pattern is a way to provide a simpler unified interface to a more complex system. 
It provides an easier way to access functions of the underlying system by providing a single entry point.

```python
from abc import ABC, abstractmethod
import time
from typing import List, Tuple, Iterator, Type

_sleep: float = 0.2


class TestCase(ABC):
    """Abstract test case interface."""

    @abstractmethod
    def run(self) -> None:
        pass


class TestCaseOne(TestCase):
    """Concrete test case one."""

    def __init__(self, name: str) -> None:
        self._name: str = name

    def run(self) -> None:
        print("{:#^20}".format(self._name))
        time.sleep(_sleep)
        print("Setting up testcase one")
        time.sleep(_sleep)
        print("Running test")
        time.sleep(_sleep)
        print("Tearing down")
        time.sleep(_sleep)
        print("Test Finished\n")


class TestCaseTwo(TestCase):
    """Concrete test case two."""

    def __init__(self, name: str) -> None:
        self._name: str = name

    def run(self) -> None:
        print("{:#^20}".format(self._name))
        time.sleep(_sleep)
        print("Setting up testcase two")
        time.sleep(_sleep)
        print("Running test")
        time.sleep(_sleep)
        print("Tearing down")
        time.sleep(_sleep)
        print("Test Finished\n")


class TestCaseThree(TestCase):
    """Concrete test case three."""

    def __init__(self, name: str) -> None:
        self._name: str = name

    def run(self) -> None:
        print("{:#^20}".format(self._name))
        time.sleep(_sleep)
        print("Setting up testcase three")
        time.sleep(_sleep)
        print("Running test")
        time.sleep(_sleep)
        print("Tearing down")
        time.sleep(_sleep)
        print("Test Finished\n")


class TestSuite:
    """Represents simpler unified interface to run all test cases.

    A facade class itself.
    """

    def __init__(self, testcases: List[TestCase]) -> None:
        self._testcases = testcases

    def run(self) -> None:
        for testcase in self._testcases:  # type: TestCase
            testcase.run()


test_cases: List[TestCase] = [TestCaseOne("TC1"), TestCaseTwo("TC2"), TestCaseThree("TC3")]
test_suite = TestSuite(test_cases)
test_suite.run()


class Interface(ABC):
    """Abstract interface."""

    @abstractmethod
    def run(self) -> str:
        pass


class A(Interface):
    """Implement interface."""

    def run(self) -> str:
        return "A.run()"


class B(Interface):
    """Implement interface."""

    def run(self) -> str:
        return "B.run()"


class C(Interface):
    """Implement interface."""

    def run(self) -> str:
        return "C.run()"


class Facade(Interface):
    """Facade object."""

    def __init__(self):
        self._all: Tuple[Type[Interface], ...] = (A, B, C)

    def run(self) -> Iterator[Interface]:
        for obj in self._all:  # type: Type[Interface]
            yield obj


if __name__ == "__main__":
    print(*(cls().run() for cls in Facade().run()))
```
**[⬆ back to top](#table-of-contents)**

## Behavioral
Behavioral patterns provide best practices of objects interaction. Methods and signatures are often used.

### Observer
Observer pattern establishes one to many relationship between subject and multiple observers. Singleton is related to observer design pattern.
- Exercise:
  - Subjects need to be monitored
  - Observers need to be notified
- Participants:
  - Subject: abstract class
    - Attach
    - Detach
    - Notify
  - Concrete Subjects

```python
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
```
**[⬆ back to top](#table-of-contents)**

### Visitor
Visitor pattern adds new features to existing hierarchy without changing it. Add new operations to existing classes dynamically.
Exercise:
  - House class:
    - HVAC specialist: Visitor type 1
    - Electrician: Visitor type 2

```python
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
```
**[⬆ back to top](#table-of-contents)**

### Iterator
Composite pattern is related to iterator pattern.
- Exercise:
  - Our custom iterator based on a build-in python iterator: `zip()`
  - Will iterate over a certain point based on client input

**Iterator function**
```python
from typing import Iterator, Tuple, List


def count_to(count: int) -> Iterator[Tuple[int, str]]:
    """Our iterator implementation."""
    numbers_in_german: List[str] = ["einn", "zwei", "drei", "veir", "funf"]
    iterator: Iterator[Tuple[int, str]] = zip(range(1, count + 1), numbers_in_german)
    for position, number in iterator:  # type: int, str
        yield position, number


for number_ in count_to(3):  # type: Tuple[int]
    print("{} in german is {}".format(*number_))


class IteratorSequence:
    """Represent iterator sequence object."""

    def __init__(self, capacity: int) -> None:
        self._range: Iterator[int] = iter(range(capacity))

    def __next__(self) -> int:
        return next(self._range)

    def __iter__(self) -> Iterator[int]:
        return self


iterator_: IteratorSequence = IteratorSequence(capacity=10)
for _ in range(10):  # type: int
    print(next(iterator_))
```
**[⬆ back to top](#table-of-contents)**

### Strategy
Strategy patterns used to dynamically change the behavior of an object. Add dynamically objects with `types` module.
- Participants:
  - Abstract strategy class with default set of behaviors
  - Concrete strategy class with new behaviors

```python
import types
from typing import Callable, Any


class Strategy:
    """A strategy pattern class."""

    def __init__(self, func: Callable[["Strategy"], Any] = None) -> None:
        self._name: str = "Default strategy"
        if func:
            self.execute = types.MethodType(func, self)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise ValueError(f'"{name}" value should be a string data type!')
        self._name = name

    def execute(self):
        print(f"{self._name} is used")


def strategy_function_one(strategy: Strategy) -> None:
    print(f"{strategy.name} is used to execute method one")


def strategy_function_two(strategy: Strategy) -> None:
    print(f"{strategy.name} is used to execute method two")


default_strategy = Strategy()
default_strategy.execute()

first_strategy = Strategy(func=strategy_function_one)
first_strategy.name = "Strategy one"
first_strategy.execute()

second_strategy = Strategy(func=strategy_function_two)
second_strategy.name = "Strategy two"
second_strategy.execute()
```
**[⬆ back to top](#table-of-contents)**

### Chain of responsibility
Thiss type of pattern decouples responsibility. Composite is related to this design pattern.
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


class Handler:
    """Abstract handler."""

    def __init__(self, successor: "Handler") -> None:
        self._successor: Handler = successor

    def handler(self, request: int) -> None:
        if not self.handle(request):
            self._successor.handler(request)

    @abstractmethod
    def handle(self, request: int) -> bool:
        pass


class ConcreteHandler1(Handler):
    """Concrete handler 1."""

    def handle(self, request: int) -> bool:
        if 0 < request <= 10:
            print(f"Request {request} handled in handler 1")
            return True
        return False


class DefaultHandler(Handler):
    """Default handler."""

    def handle(self, request: int) -> bool:
        """If there is no handler available."""
        print(f"End of chain, no handler for {request}")
        return True


class Client:
    """Using handlers."""

    def __init__(self) -> None:
        self._handler: Handler = ConcreteHandler1(DefaultHandler(None))

    def delegate(self, request: List[int]) -> None:
        for next_request in request:
            self._handler.handler(next_request)


# Create a client
client: Client = Client()

# Create requests
requests: List[int] = [2, 5, 30]

# Send the request
client.delegate(requests)
```
**[⬆ back to top](#table-of-contents)**

## Other qualities
**Completeness** depends on how much the software solution meets its requirements.

**Correctness** make the software without errors.

**Coupling** how much different elements of a software are related. If there is strong coupling changes in one element affects another. Less coupling is desirable.

**Cohesion** refers to how independent the software component is. More cohesion is better.

**[⬆ back to top](#table-of-contents)**

## Development notes

### Code analysis
From the root directory of your shell please run following command to start static code assessment (it will check code with linter rules and unit testing):

```bash
~ ./run-code-analysis.sh 
```

### Release notes

* 0.2.0
    * Add tests coverage 
* 0.1.1
    * Polish documentation
* 0.1.0
    * Distribute first version of a project

### Meta
Author – Volodymyr Yahello vyahello@gmail.com

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
