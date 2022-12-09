from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])


def add(self, other):
    return Point(self.x + other.x, self.y + other.y)


def sub(self, other):
    return Point(self.x - other.x, self.y - other.y)


def convert_to_array_notation(self, x_min, y_min, y_max):
    translated_to_new_orig = self - Point(x_min, y_min)
    magic = Point(-translated_to_new_orig.y + y_max-y_min, translated_to_new_orig.x)
    return magic


Point.__add__ = add
Point.__sub__ = sub
Point.convert_to_array_notation = convert_to_array_notation


UP = Point(0, 1)
DOWN = Point(0, -1)
LEFT = Point(-1, 0)
RIGHT = Point(1, 0)

directions = [UP, DOWN, LEFT, RIGHT]

