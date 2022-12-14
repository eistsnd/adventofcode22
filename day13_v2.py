import json


def char_gen(packet):
    pointer = 0
    while pointer < len(packet):
        char = packet[pointer]
        if char in ['[', ']']:
            yield packet[pointer]
            pointer += 1
        elif char == ',':
            pointer += 1
        else:
            num_pointer = pointer
            while packet[num_pointer].isnumeric():
                num_pointer += 1
            char = yield int(packet[pointer: num_pointer])
            if char:
                packet = packet[:num_pointer] + char + packet[num_pointer:]
                yield int(packet[pointer: num_pointer])
            else:
                pointer = num_pointer


def process(left, right):
    left_g = char_gen(left)
    right_g = char_gen(right)

    while True:
        left_item = next(left_g)
        right_item = next(right_g)

        if left_item == ']' and type(right_item) == int:
            return -1
        if type(left_item) == int and right_item == ']':
            return 1
        if left_item == '[' and type(right_item) == int:
            right_g.send(']')
            right_g.send(']')
            right_g.send(']')
        if type(left_item) == int and right_item == '[':
            left_g.send(']')
        if type(left_item) == int and type(right_item) == int:
            if left_item != right_item:
                return (1, -1)[left_item < right_item]
        if left_item == '[' and right_item == ']':
            return 5
        if left_item == ']' and right_item == '[':
            return 6


if __name__ == '__main__':
    with open('day13_input_test.txt') as file:
        packets = [line for line in file.read().splitlines() if line]

    # part 1
    pairs_in_order = [
        (process(packets[j], packets[j + 1]), (i + 1))
        for i, j in enumerate(range(0, len(packets), 2))
    ]
    print(pairs_in_order)
    sum_of_indices_of_pairs_in_order = sum([pair[1] for pair in pairs_in_order if pair[0] == -1])
    print(sum_of_indices_of_pairs_in_order)

