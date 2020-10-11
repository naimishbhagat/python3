# Class: blueprint for creating new objects
# Object: instance of a class

#Class: Human
# objects: John, Mary, Jack
class Point:
    # class attribute which shared across all instances of class
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    # magic method
    def __str__(self):
        return f" ({self.x},{self.y}) "

    # compare objects
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # compare objects
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    # arithmetic operator objects
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # intance method
    def draw(self):
        print(f"Point ({self.x},{self.y}) ")


Point.default_color = "yello"
# class level method
#point = Point.zero()
point = Point(1, 2)
print(point)
print(str(point))
other = Point(1, 2)
print(point == other)
another = Point(3, 4)
print(print > another)
#point.z = 10
# point.draw()
# print(point.x)
# class attribute
print(Point.default_color)
print(point.default_color)
# instance attribute
point = Point(3, 4)
print(type(point))  # <class '__main__.Point'>
print(isinstance(point, Point))
point.draw()
# constructor
