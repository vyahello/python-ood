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
