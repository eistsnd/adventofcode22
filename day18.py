from point import Point3d
from operator import attrgetter


def scan_surface(points, s1, s2, s3):
    s1_min = attrgetter(s1)(min(points, key=attrgetter(s1)))
    s1_max = attrgetter(s1)(max(points, key=attrgetter(s1)))
    s2_min = attrgetter(s2)(min(points, key=attrgetter(s2)))
    s2_max = attrgetter(s2)(max(points, key=attrgetter(s2)))

    counter = 0

    for s1_running in range(s1_min, s1_max + 1):
        for s2_running in range(s2_min, s2_max + 1):
            points_in_line = sorted(
                filter(
                    lambda point: attrgetter(s1)(point) == s1_running and attrgetter(s2)(point) == s2_running,
                    points
                ),
                key=attrgetter(s3)
            )

            inner_counter = 0

            if len(points_in_line):
                inner_counter = 2
            if 1 < len(points_in_line):
                for i in range(len(points_in_line) - 1):
                    if attrgetter(s3)(points_in_line[i + 1]) - attrgetter(s3)(points_in_line[i]) != 1:
                        inner_counter += 2

            print(inner_counter)
            counter += inner_counter

    print('counter', counter)
    return counter


if __name__ == '__main__':
    with open('day18_input.txt') as file:
        points = [Point3d(*[int(coo) for coo in line.rstrip().split(',')]) for line in file]

    min(points, key=attrgetter('x'))
    surfaces = [('x', 'y', 'z'), ('x', 'z', 'y'), ('y', 'z', 'x')]

    total_surface = sum([scan_surface(points, *surface) for surface in surfaces])
    print(total_surface)
