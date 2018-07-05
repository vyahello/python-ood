class ShapeInterface(object):
    """Interface that defines the method."""

    def draw(self) -> None:
        raise NotImplementedError


class Circle(ShapeInterface):
    """Concrete subclass."""
    def draw(self):
        print('Circle.draw')


class Square(ShapeInterface):
    """Concrete subclass."""
    def draw(self):
        print('Square.draw')


class ShapeFactory(object):
    @staticmethod
    def get_shape(type: str):
        if type == 'circle':
            return Circle()
        if type == 'square':
            return Square()
        assert 0, f'Could not find shape {type}'


factory = ShapeFactory()
print(factory.get_shape('circle'))
