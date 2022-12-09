class Cargo:
    # should you create a copy of the input???
    def __init__(self, stacks):
        self.stacks = stacks

    def move_one_from_to(self, orig, dest):
        self.stacks[dest].append(self.stacks[orig].pop())

    def get_top_layer(self):
        return ''.join([stack[len(stack)-1] for stack in self.stacks])


class Cargo9000(Cargo):
    def move_multiple_from_to(self, nr, orig, dest):
        for _ in range(nr):
            self.move_one_from_to(orig, dest)


class Cargo9001(Cargo):
    def move_multiple_from_to(self, nr, orig, dest):
        temp_stack = []

        for _ in range(nr):
            temp_stack.append(self.stacks[orig].pop())

        for _ in range(nr):
            self.stacks[dest].append(temp_stack.pop())
