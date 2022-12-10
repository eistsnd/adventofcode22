from cpu import add_x_instruction, CPU, noop_instruction
from crt import CRT


if __name__ == '__main__':
    with open('day10_input.txt') as file:
        instructions = [line.rstrip() for line in file]

    # part 1
    cpu = CPU()
    for instruction in instructions:
        cpu.add_instruction(instruction)

    signal_str_to_measure = [20, 60, 100, 140, 180, 220]
    total_signal_str = 0
    for i in range(2, 221):
        cpu.tick()
        if i in signal_str_to_measure:
            total_signal_str += (cpu.X * i)

    print(total_signal_str)

    # part 2
    cpu = CPU()
    for instruction in instructions:
        cpu.add_instruction(instruction)

    crt = CRT()

    for _ in range(240):
        crt.tick()
        cpu.tick()
        crt.set_sprite(cpu.X)

    print(crt.screen)


