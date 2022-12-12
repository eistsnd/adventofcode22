class Monkey:
    def __init__(self, items, toss):
        self.items = items
        self.toss = toss
        self.inspected_items = 0


class MonkeyBusiness:
    def __init__(self, monkeys):
        self.monkeys = monkeys

    def play_round(self):
        for monkey in self.monkeys:
            for _ in range(len(monkey.items)):
                new_item, new_owner = monkey.toss(monkey.items.pop(0))
                monkey.inspected_items += 1
                self.monkeys[new_owner].items.append(new_item)
