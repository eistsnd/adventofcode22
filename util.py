import operator


def g_step(board, sx, sy, dx, dy):
    px, py = sx, sy

    def inner():
        nonlocal px, py

        while True:
            px += dx
            py += dy
            if px < 0 or py < 0:
                return
            try:
                yield board[px][py]
            except IndexError:
                return

    return inner()


def flat_map(da_list):
    return [item for _ in da_list for item in _]


def build_matrix(cols, rows, filler):
    return [[filler] * cols for _ in range(rows)]


def draw_matrix(matrix):
    for row in matrix:
        print(''.join([str(item) for item in row]))


def get_enclosing_coos(points):
    x_min, y_min, x_max, y_max = \
        [op([operator.attrgetter(attr)(item) for item in points]) for op in [min, max] for attr in ['x', 'y']]

    return x_min, y_min, x_max, y_max


