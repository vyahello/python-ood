from abc import ABC, abstractmethod


class Component(ABC):
    """Abstract interface of some component."""

    @abstractmethod
    def function(self) -> None:
        pass


class Child(Component):
    """Concrete child component."""

    def __init__(self, *args: str) -> None:
        self._args: str = args

    def name(self) -> str:
        return self._args[0]

    def function(self) -> None:
        print(f'"{self.name()}" component')


class Composite(Component):
    """Concrete class maintains the tree recursive structure."""

    def __init__(self, *args: str):
        self._args: str = args
        self._children: list = []

    def name(self) -> str:
        return self._args[0]

    def append_child(self, child: Component) -> None:
        self._children.append(child)

    def remove_child(self, child: Component) -> None:
        self._children.remove(child)

    def function(self) -> None:
        print(f'"{self.name()}" component')
        for child in self._children:
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
