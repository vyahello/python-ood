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
