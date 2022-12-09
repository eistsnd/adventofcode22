class Assignment:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def does_superseed(self, other_assignment):
        if self.start <= other_assignment.start and other_assignment.end <= self.end:
            return True

        return False

    def does_overlap(self, other_assignment):
        return self.is_within(other_assignment.start) or self.is_within(other_assignment.end) or \
            other_assignment.is_within(self.start) or other_assignment.is_within(self.end)

    def is_within(self, point):
        return self.start <= point <= self.end


class WorkGroup:
    def __init__(self, assignment_1, assignment_2):
        self.assignment_1 = assignment_1
        self.assignment_2 = assignment_2

    def does_one_contain_the_other(self):
        return self.assignment_1.does_superseed(self.assignment_2) or \
            self.assignment_2.does_superseed(self.assignment_1)

    def does_overlap(self):
        return self.assignment_1.does_overlap(self.assignment_2)


if __name__ == '__main__':
    with open('day4_input.txt') as file:
        work_pairs = [[interval.split('-') for interval in line.rstrip().split(',')] for line in file]

    # part 1
    total_part_1 = sum(
        [
            int(
                WorkGroup(
                    *[Assignment(*list(map(int, assignment))) for assignment in pair]
                ).does_one_contain_the_other()
            )
            for pair in work_pairs
        ]
    )

    print(total_part_1)

    # part 2
    total_part_2 = sum(
        [
            int(
                WorkGroup(
                    *[Assignment(*list(map(int, assignment))) for assignment in pair]
                ).does_overlap()
            )
            for pair in work_pairs
        ]
    )

    print(total_part_2)