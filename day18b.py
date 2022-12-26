from point import Point3d
from operator import attrgetter


def find_enclosing(points):
    x_min = min(points, key=attrgetter('x')).x - 1
    x_max = max(points, key=attrgetter('x')).x + 1
    y_min = min(points, key=attrgetter('y')).y - 1
    y_max = max(points, key=attrgetter('y')).y + 1
    z_min = min(points, key=attrgetter('z')).z - 1
    z_max = max(points, key=attrgetter('z')).z + 1

    neighbors = [
        Point3d(-1, 0, 0), Point3d(1, 0, 0), Point3d(0, -1, 0),
        Point3d(0, 1, 0), Point3d(0, 0, -1), Point3d(0, 0, 1)
    ]

    visited = set()
    stack = [Point3d(x_min, y_min, z_min)]

    while stack:
        curr = stack.pop()
        visited.add(curr)

        for neighbor in neighbors:
            next_point = curr + neighbor

            if x_min <= next_point.x <= x_max and y_min <= next_point.y <= y_max and z_min <= next_point.z <= z_max and \
                    next_point not in visited and next_point not in points:
                stack.append(next_point)

    return visited


if __name__ == '__main__':
    neighbors = [
        Point3d(-1, 0, 0), Point3d(1, 0, 0), Point3d(0, -1, 0),
        Point3d(0, 1, 0), Point3d(0, 0, -1), Point3d(0, 0, 1)
    ]

    with open('day18_input.txt') as file:
        points = [Point3d(*[int(coo) for coo in line.rstrip().split(',')]) for line in file]

    enclosing = find_enclosing(points)

    all = 0
    outer = 0
    for point in points:
        for neighbor in neighbors:
            if (point + neighbor) not in points:
                all += 1
            if (point + neighbor) in enclosing:
                outer += 1

    print(all)
    print(outer)
