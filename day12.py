from contextlib import suppress
from point import directions, Point
from util import build_matrix, flat_map

if __name__ == '__main__':
    with open('day12_input.txt') as file:
        height_map = [[char for char in line.rstrip()] for line in file]

    rows = len(height_map)
    cols = len(height_map[0])

    for i in range(rows):
        for j in range(cols):
            if height_map[i][j] == 'S':
                start = Point(i, j)
                height_map[i][j] = 'a'

            if height_map[i][j] == 'E':
                end = Point(i, j)
                height_map[i][j] = 'z'

    # part 1
    path_map = build_matrix(cols, rows, '.')
    start.set_element_to(path_map, 0)

    process_queue = [start]

    while process_queue:
        x_marks_the_spot = process_queue.pop(0)

        for direction in directions:
            adjacent_spot = x_marks_the_spot + direction
            with suppress(IndexError):
                adjacent_height = adjacent_spot.get_element_from(height_map)
                x_mark_height = x_marks_the_spot.get_element_from(height_map)

                # can take step or too high terrain
                if ord(adjacent_height)-ord(x_mark_height) <= 1:
                    steps_to_get_here_if_any = adjacent_spot.get_element_from(path_map)
                    steps_to_get_here_from_x = x_marks_the_spot.get_element_from(path_map)
                    if steps_to_get_here_if_any == '.' or steps_to_get_here_from_x + 1 < steps_to_get_here_if_any:
                        adjacent_spot.set_element_to(path_map, steps_to_get_here_from_x + 1)

                        if adjacent_spot != end:
                            process_queue.append(adjacent_spot)

    # 423
    print(end.get_element_from(path_map))

    # part 2
    path_map = build_matrix(cols, rows, '.')
    end.set_element_to(path_map, 0)

    process_queue = [end]

    while process_queue:
        x_marks_the_spot = process_queue.pop(0)

        for direction in directions:
            adjacent_spot = x_marks_the_spot + direction
            with suppress(IndexError):
                adjacent_height = adjacent_spot.get_element_from(height_map)
                x_mark_height = x_marks_the_spot.get_element_from(height_map)

                # could have stepped from next pos to current
                if ord(x_mark_height) - ord(adjacent_height) <= 1:
                    steps_to_get_here_if_any = adjacent_spot.get_element_from(path_map)
                    steps_to_get_here_from_x = x_marks_the_spot.get_element_from(path_map)
                    if steps_to_get_here_if_any == '.' or steps_to_get_here_from_x + 1 < steps_to_get_here_if_any:
                        adjacent_spot.set_element_to(path_map, steps_to_get_here_from_x + 1)

                        if adjacent_spot.get_element_from(height_map) != 'a':
                            process_queue.append(adjacent_spot)

    min_steps = min([step for height, step in zip(flat_map(height_map), flat_map(path_map)) if height == 'a' and step !='.'])
    # 416
    print(min_steps)





