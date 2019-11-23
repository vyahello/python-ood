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
