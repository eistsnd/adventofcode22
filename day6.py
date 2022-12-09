def find_first_n_distinct_characters(stream, n):
    for i in range(n-1, len(stream)+1):
        if len(set(stream[i-n:i])) == n:
            return i


if __name__ == '__main__':
    with open('day6_input.txt') as file:
        stream = file.readline().rstrip()

    # part 1
    print(find_first_n_distinct_characters(stream, 4))

    # part 2
    print(find_first_n_distinct_characters(stream, 14))


