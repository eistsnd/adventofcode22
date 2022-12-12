from operator import add, mul
from monkey_business import Monkey, MonkeyBusiness


def starting_items(text):
    items = text.removeprefix('  Starting items: ').split(', ')
    return [int(item) for item in items]


def last_number(text):
    return int(text.split(' ')[-1])


def operation(text):
    op, arg = text.removeprefix('  Operation: new = old ').split(' ')
    op_map = {'+': add, '*': mul}

    def do_op(old):
        nonlocal arg
        if arg == 'old':
            right = old
        else:
            right = int(arg)
        return op_map[op](old, right)

    return do_op


def toss(new_level, test, passed, failed):
    def get_next(item):
        new_item = (new_level(item) // 3)
        return new_item, (failed, passed)[new_item % test == 0]

    return get_next


def toss2(lcm , new_level, test, passed, failed):
    def get_next(item):
        new_item = new_level(item) % lcm
        return new_item, (failed, passed)[new_item % test == 0]

    return get_next


if __name__ == '__main__':
    with open('day11_input.txt') as file:
        lines = [line.rstrip() for line in file]

    # part 1
    monkeys = []

    for i in range(0, len(lines), 7):
        items = starting_items(lines[i+1])
        toss_cb = toss(
            operation(lines[i+2]),
            last_number(lines[i+3]),
            last_number(lines[i+4]),
            last_number(lines[i+5])
        )

        monkeys.append(Monkey(items, toss_cb))

    monkey_business = MonkeyBusiness(monkeys)

    for _ in range(20):
        monkey_business.play_round()

    # 61005
    print(mul(*sorted([monkey.inspected_items for monkey in monkey_business.monkeys])[-2:]))

    # part 2
    monkeys = []
    lcm = 1
    for i in range(0, len(lines), 7):
        lcm *= last_number(lines[i + 3])

    for i in range(0, len(lines), 7):
        items = starting_items(lines[i + 1])
        toss_cb = toss2(
            lcm,
            operation(lines[i + 2]),
            last_number(lines[i + 3]),
            last_number(lines[i + 4]),
            last_number(lines[i + 5])
        )

        monkeys.append(Monkey(items, toss_cb))

    monkey_business = MonkeyBusiness(monkeys)

    for _ in range(10000):
        monkey_business.play_round()

    print(mul(*sorted([monkey.inspected_items for monkey in monkey_business.monkeys])[-2:]))
