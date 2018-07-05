class Singleton(object):
    """Make all instances the same object."""

    def __new__(cls) -> 'Singleton':
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance


class Singleton1(object):
    __instance = None
    def __new__(cls, val=None):
        if not Singleton1.__instance:
            Singleton1.__instance = object.__new__(cls)
        Singleton1.__instance.val = val
        return Singleton1.__instance


class Foo(object):
    """Fancy object."""
    pass


def foo_singleton_factory(_singleton = Foo()) -> Foo:
    """A singleton factory."""
    return _singleton


def singleton(cls):
    """Singleton decorator."""

    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@singleton
class Bar(object):
    """Fancy object."""
    pass


# Instantiate the same singleton object
s_one = Singleton()
s_two = Singleton()

print(id(s_one))
print(id(s_two))
print(s_one is s_two)

# Use singleton factory
a = foo_singleton_factory()
b = foo_singleton_factory()
print(a is b)

# Use singleton decorator
f = Bar()
d = Bar()
print(f is d)