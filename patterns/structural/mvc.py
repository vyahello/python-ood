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
    def show_item_information(
        self, item_type: str, item_name: str, item_info: List[str]
    ) -> None:
        """
        Will look for item information by iterating over
        key,value pairs yielded by item_info.items().
        """
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
        except KeyError as error:
            raise KeyError(
                str(error) + " not in the model's item list."
            ) from error


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

    def show_item_information(
        self, item_type: str, item_name: str, item_info: Dict[str, int]
    ) -> None:
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
