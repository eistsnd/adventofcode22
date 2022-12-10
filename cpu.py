class CPU:
    def __init__(self):
        self.X = 1
        self.clock = 0
        self.thread = []
        self.running_process = None

    def tick(self):
        if not self.running_process:
            if len(self.thread):
                self.running_process = self.thread.pop(0)

        if self.running_process:
            if self.running_process.tick():
                self.running_process = None

    def add_x(self, value):
        self.X += value

    def add_instruction(self, instruction):
        new_process = self.build_process_from_instruction(instruction)
        self.thread.append(new_process)

    def build_process_from_instruction(self, line):
        if line == 'noop':
            return noop_instruction()
        else:
            value = int(line.split()[1])
            return add_x_instruction(self, value)


class Process:
    def __init__(self, cb, ticks_to_finish):
        self.clock = 0
        self.cb = cb
        self.ticks_to_finish = ticks_to_finish

    def tick(self):
        self.clock += 1
        if self.clock == self.ticks_to_finish:
            self.cb()
            return True

        return False


def noop_instruction():
    def noop():
        pass
    return Process(noop, 1)


def add_x_instruction(cpu, value):
    def add():
        def inner():
            cpu.add_x(value)
        return inner
    return Process(add(), 2)
