import time


class Producer:
    """Define the resource-intensive object to instantiate."""

    @staticmethod
    def produce():
        print('producer is working hard')

    @staticmethod
    def meet():
        print('Producer has time to meet you now')


class Proxy:
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
