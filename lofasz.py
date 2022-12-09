from util import build_matrix, draw_matrix, get_enclosing_coos
from point import Point
matrix = build_matrix(4, 4, '.')


def convert_to_lofasz(point, y_len):
    return Point(-point.y, point.x) + Point(y_len,0)

# ..23
# .1..
# 0...
# 3,0 -> -1,-1
# 1,1 -> 0,0
# 0,2 -> 1,1


points = [Point(-1,-1), Point(0,0), Point(1,1), Point(2,1)]
x_min, y_min, x_max, y_max = get_enclosing_coos(points)

print(x_min, y_min, x_max, y_max)

translated = [point.convert_to_array_notation(x_min, y_min, y_max) for point in points]
print(translated)

for i, point in enumerate(translated):
    matrix[point.x][point.y] = str(i)

for row in matrix:
    print(''.join(row))
