from abc import abstractmethod
from typing import List


class Handler:
    """Abstract handler."""

    def __init__(self, successor: "Handler") -> None:
        self._successor: Handler = successor

    def handler(self, req: int) -> None:
        if not self.handle(req):
            self._successor.handler(req)

    @abstractmethod
    def handle(self, req: int) -> bool:
        pass


class ConcreteHandler1(Handler):
    """Concrete handler 1."""

    def handle(self, req: int) -> bool:
        if 0 < req <= 10:
            print("Request {} handled in handler 1".format(req))
            return True
        return False


class DefaultHandler(Handler):
    """Default handler."""

    def handle(self, req: int) -> bool:
        """If there is no handler available."""
        print("End of chain, no handler for {}".format(req))
        return True


class Client:
    """Using handlers."""

    def __init__(self) -> None:
        self._handler: Handler = ConcreteHandler1(DefaultHandler(None))

    def delegate(self, req: List[int]) -> None:
        for r in req:
            self._handler.handler(r)


# Create a client
c = Client()

# Create requests
requests = [2, 5, 30]

# Send the request
c.delegate(requests)
