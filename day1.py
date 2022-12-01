import elf_goodies


if __name__ == '__main__':
    elf_bags = []

    with open('day1.txt', 'r') as f:
        bag = elf_goodies.Bag()
        liter = (l.rstrip("\r\n") for l in f)
        # should there be more consecutive blank lines i might be royally fucked but im to lazy to figure this shit out
        # so just yolo
        for line in liter:
            if len(line) > 0:
                bag.add(elf_goodies.Food(int(line)))
            else:
                elf_bags.append(bag)
                bag = elf_goodies.Bag()

    # part1
    and_the_most_calories_gathered____is = max((bag.get_total_calories() for bag in elf_bags))
    print(and_the_most_calories_gathered____is)

    # part2
    and_the_three_most_calories_gathered____are = sorted((bag.get_total_calories() for bag in elf_bags))
    print(sum(and_the_three_most_calories_gathered____are[-3:]))


