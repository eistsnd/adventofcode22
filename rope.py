from point import Point
from util import build_matrix, draw_matrix, get_enclosing_coos, sign


class Rope:
    def __init__(self, length):
        # head: 0 tail: size-1
        self.rope = [Point(0, 0) for _ in range(length)]
        self.length = length
        self.orig = Point(0, 0)

    @property
    def head(self):
        return self.rope[0]

    @head.setter
    def head(self, value):
        self.rope[0] = value

    @property
    def tail(self):
        return self.rope[self.length-1]

    def move(self, step):
        self.head += step

        head = self.head

        for i in range(1, self.length):
            tail = self.rope[i]

            new_tail = self.find_tail(head, tail)

            if new_tail != tail:
                self.rope[i] = new_tail
                head = new_tail
            else:
                break

    @classmethod
    def find_tail(cls, head, tail):
        new_tail = tail
        diff_x = head.x - tail.x
        diff_y = head.y - tail.y

        # diagonal
        if abs(diff_x) == 2 or abs(diff_y) == 2:
            new_tail = tail + Point(sign(diff_x), sign(diff_y))

        return new_tail

    def draw_rope(self):
        rope_and_start = self.rope + [self.orig]
        x_min, y_min, x_max, y_max = get_enclosing_coos(rope_and_start)

        terrain = build_matrix(x_max-x_min+1, y_max-y_min+1, '.')

        orig_conv = self.orig.convert_to_array_notation(x_min, y_min, y_max)
        terrain[orig_conv.x][orig_conv.y] = 's'

        for i, point in enumerate(self.rope):
            conv = point.convert_to_array_notation(x_min, y_min, y_max)
            terrain[conv.x][conv.y] = str(i)

        draw_matrix(terrain)

    @staticmethod
    def draw_visited(visited):
        x_min, y_min, x_max, y_max = get_enclosing_coos(visited)

        terrain = build_matrix(x_max - x_min + 1, y_max - y_min + 1, '.')

        for point in visited:
            conv = point.convert_to_array_notation(x_min, y_min, y_max)
            terrain[conv.x][conv.y] = str('#')

        draw_matrix(terrain)





