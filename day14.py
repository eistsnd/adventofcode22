from operator import attrgetter
from point import Point
from util import sign


if __name__ == '__main__':
    with open('day14_input.txt') as file:
        rock_paths = [
            [
                Point(*list(map(int, vertex.split(',')))) for vertex in line.rstrip().replace(' ', '').split('->')
            ]
            for line in file
        ]

    rocks = set()

    for rock_path in rock_paths:
        for i in range(len(rock_path)-1):
            start = rock_path[i]
            end = rock_path[i+1]

            direction = Point(sign(end.x - start.x), sign(end.y - start.y))

            next_rock = start
            while next_rock != end:
                rocks.add(next_rock)
                next_rock += direction
            rocks.add(end)

    # part 1
    rock_bottom = max(rocks, key=attrgetter('y')).y
    sands = set()
    ami_hitting_rock_bottom = False

    D = Point(0,1)
    DL = Point(-1,1)
    DR = Point(1,1)
    directions = [D,DL, DR]

    while True:
        sand = Point(500, 0)

        while True:
            for direction in directions:
                new_sand = sand + direction
                if new_sand not in rocks and new_sand not in sands:
                    sand = new_sand
                    break
            else:
                sands.add(sand)
                break

            if rock_bottom < sand.y:
                break

        if rock_bottom < sand.y:
            break

    print(len(sands))

    # part 2
    rock_bottom = max(rocks, key=attrgetter('y')).y + 2
    sands = set()
    ami_hitting_rock_bottom = False

    D = Point(0, 1)
    DL = Point(-1, 1)
    DR = Point(1, 1)
    directions = [D, DL, DR]

    while True:
        sand = Point(500, 0)

        while True:
            for direction in directions:
                new_sand = sand + direction
                if new_sand not in rocks and new_sand not in sands and new_sand.y < rock_bottom:
                    sand = new_sand
                    break
            else:
                sands.add(sand)
                break

            if sand == Point(500,0):
                break

        if sand == Point(500,0):
            break

    print(len(sands))
    # hat a faszom h ketszer kell ugyanugy kibreakelni :S:S
