from scanner import Scanner

if __name__ == '__main__':
    with open('day8_input.txt') as file:
        terrain = [[int(digit) for digit in line.rstrip()] for line in file]

    scanner = Scanner(terrain)

    # part 1
    scanner.scan_visibility()
    visible_tree_count = scanner.count_visible()
    print(visible_tree_count)

    # part 2
    scanner.scan_scenic_view()
    best_scenic_view_score = scanner.get_best_scenic_view()
    print(best_scenic_view_score)