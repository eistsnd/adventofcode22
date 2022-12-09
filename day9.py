from point import UP, DOWN, LEFT, RIGHT
from util import flat_map
from rope import Rope


def get_direction(letter):
    table = {
        'U': UP,
        'D': DOWN,
        'L': LEFT,
        'R': RIGHT
    }
    return table[letter]


def build_steps(steps):
    direction, nr = steps.split()
    return [get_direction(direction)] * int(nr)


if __name__ == '__main__':
    with open('day9_input.txt') as file:
        steps = flat_map([build_steps(line.rstrip()) for line in file])

    # part 1
    rope = Rope(2)
    visited_by_tail = set()

    for step in steps:
        rope.move(step)
        visited_by_tail.add(rope.tail)

    nr_of_visited_points = len(visited_by_tail)

    # 6367
    print(nr_of_visited_points)

    # part 2
    rope = Rope(10)
    visited_by_tail = set()

    for step in steps:
        rope.move(step)
        visited_by_tail.add(rope.tail)

    rope.draw_visited(list(visited_by_tail))

    nr_of_visited_points = len(visited_by_tail)
    # 2536
    print(nr_of_visited_points)
