class Singleton(object):
    """Make all instances the same object."""

    def __new__(cls) -> 'Singleton':
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance


# Instantiate the same singleton object
s_one = Singleton()
s_two = Singleton()

print(id(s_one))
print(id(s_two))
print(s_one is s_two)