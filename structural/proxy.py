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
