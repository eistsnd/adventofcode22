def get_item_prio(letter):
    value = ord(letter)
    if value < 91:
        return value - 64 + 26
    else:
        return value - 96


if __name__ == '__main__':
    with open('day3_input.txt', 'r') as file:
        zurucksachen = [line.rstrip() for line in file]

    # part 1
    total_part_1 = sum([
        get_item_prio(
            (set(zurucksach[:len(zurucksach) // 2]) & set(zurucksach[len(zurucksach) // 2:])).pop()
        )
        for zurucksach in zurucksachen
    ])

    print(total_part_1)

    # part 2
    total_part_2 = sum([
        get_item_prio(
            (set(zurucksachen[i]) & set(zurucksachen[i+1]) & set(zurucksachen[i+2])).pop()
        )
        for i in range(0, len(zurucksachen), 3)
    ])

    print(total_part_2)





