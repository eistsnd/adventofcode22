from collections import namedtuple
from functools import reduce

Point = namedtuple('Point', ['x', 'y'])


def add(self, other):
    return Point(self.x + other.x, self.y + other.y)


def sub(self, other):
    return Point(self.x - other.x, self.y - other.y)


def convert_to_array_notation(self, x_min, y_min, y_max):
    translated_to_new_orig = self - Point(x_min, y_min)
    magic = Point(-translated_to_new_orig.y + y_max-y_min, translated_to_new_orig.x)
    return magic


def get_element_from(self, matrix):
    if self.x < 0 or self.y < 0:
        raise IndexError
    return matrix[self.x][self.y]


def set_element_to(self, matrix, value):
    matrix[self.x][self.y] = value


Point.__add__ = add
Point.__sub__ = sub
Point.convert_to_array_notation = convert_to_array_notation
Point.get_element_from = get_element_from
Point.set_element_to = set_element_to


UP = Point(0, 1)
DOWN = Point(0, -1)
LEFT = Point(-1, 0)
RIGHT = Point(1, 0)

directions = [UP, DOWN, LEFT, RIGHT]

Range = namedtuple('Range', ['start', 'end'])


def union_of_ranges(ranges):
    ranges_sorted = sorted(ranges, key=lambda range: range.start)

    return reduce(
        lambda acc, coverage: acc[:-1] + [Range(acc[-1].start, max(acc[-1].end, coverage.end))]
        if coverage.start-1 <= acc[-1].end
        else acc + [coverage],
        ranges_sorted[1:],
        ranges_sorted[0:1]
    )


def trim_ranges(ranges, range):
    if ranges[0].start < range.start:
        ranges[0] = Range(range.start, ranges[0].end)
    if range.end < ranges[-1].end:
        ranges[-1] = Range(ranges[-1].start, range.end)


Point3d = namedtuple('Point3d', ['x', 'y', 'z'])


def add3d(self, point3d):
    return Point3d(self.x + point3d.x, self.y + point3d.y, self.z + point3d.z)


Point3d.__add__ = add3d
