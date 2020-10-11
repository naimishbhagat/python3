class Animal(object):
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# Animal: Parent, Base
# Mammal: Child, Sub


class Mammal(Animal):
    def __init__(self):
        self.weight = 2
        # method override
        super().__init__()

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
m.walk()
print(m.age)
print(m.weight)
print(isinstance(m, object))
o = object()
# object class
print(issubclass(Mammal, object))

# good example of inheritance


class InvalidOperationExceptionError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationExceptionError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationExceptionError("Stream is already closed")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStram(Stream):
    def read(self):
        print("Reading data from a network")
