import json
from functools import cmp_to_key
from operator import mul


def process(left, right):
    next_to_process = [(left, right, 0)]

    while next_to_process:
        left, right, pos = next_to_process.pop()
        left_size = len(left)
        right_size = len(right)

        while True:
            if left_size == pos and right_size == pos:
                break
            if left_size == pos or right_size == pos:
                return (1, -1)[left_size < right_size]

            left_item = left[pos]
            right_item = right[pos]

            if type(left_item).__name__ == 'list' and type(right_item).__name__ == 'list':
                next_to_process.append((left, right, pos+1))
                next_to_process.append((left_item, right_item, 0))
                break

            if type(left_item).__name__ != 'list' and type(right_item).__name__ != 'list':
                if left_item == right_item:
                    pos += 1
                else:
                    return (1, -1)[left_item < right_item]

            if type(left_item).__name__ != 'list' and type(right_item).__name__ == 'list':
                left_item = [left_item]
                next_to_process.append((left, right, pos + 1))
                next_to_process.append((left_item, right_item, 0))
                break

            if type(left_item).__name__ == 'list' and type(right_item).__name__ != 'list':
                right_item = [right_item]
                next_to_process.append((left, right, pos + 1))
                next_to_process.append((left_item, right_item, 0))
                break


if __name__ == '__main__':
    with open('day13_input.txt') as file:
        packets = [json.loads(line) for line in file.read().splitlines() if line]

    # part 1
    pairs_in_order = [
        (process(packets[j], packets[j + 1]), (i + 1))
        for i, j in enumerate(range(0, len(packets), 2))
    ]
    sum_of_indices_of_pairs_in_order = sum([pair[1] for pair in pairs_in_order if pair[0] == -1])
    print(sum_of_indices_of_pairs_in_order)

    # part 2
    dividers = [[[2]], [[6]]]
    packets_with_dividers = packets + dividers
    packets_with_dividers.sort(key=cmp_to_key(process))
    decoder_key = mul(*[packets_with_dividers.index(divider) + 1 for divider in dividers])
    print(decoder_key)













