from cargo import Cargo9000, Cargo9001


def convert_to_programmer_numbers(move_str):
    move_int = list(map(int, move_str.split(' ')[1::2]))
    move_int[1] -= 1
    move_int[2] -= 1

    return move_int


if __name__ == '__main__':
    with open('day5_cargo_input.txt') as file:
        raw_lines = [line[1::4] for line in file]

    with open('day5_moves_input.txt') as file:
        moves = [convert_to_programmer_numbers(line) for line in file]


    # part 2
    cargo_input = [list(''.join(i).rstrip()) for i in zip(*reversed(raw_lines))]
    cargo = Cargo9000(cargo_input)
    for move in moves:
        cargo.move_multiple_from_to(*move)

    print(cargo.get_top_layer())

    # part 2
    cargo_input = [list(''.join(i).rstrip()) for i in zip(*reversed(raw_lines))]
    cargo = Cargo9001(cargo_input)
    for move in moves:
        cargo.move_multiple_from_to(*move)

    print(cargo.get_top_layer())
