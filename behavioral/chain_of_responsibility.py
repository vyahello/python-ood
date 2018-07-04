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