import re


class State:
    def __init__(self, steps_left, total, valves_bitmap):
        self.steps_left = steps_left
        self.total = total
        self.valves_bitmap = valves_bitmap

    def add_total(self, total):
        return State(self.steps_left, self.total + total, self.valves_bitmap)

    def set_steps_left(self, steps_left):
        return State(steps_left, self.total, self.valves_bitmap)

    def open_valve(self, pos):
        return State(self.steps_left, self.total, self.valves_bitmap | pos)


class Propagator:
    def __init__(self, valves, distance_map):
        self.valves = valves
        self.distance_map = distance_map
        self.stack = None
        self.visited_max = None

    def run(self, starting_pos, max_step_nr):
        self.stack = self._generate_starting_opens(starting_pos, max_step_nr)
        self.visited_max = {}
        while self.stack:
            next_op = self.stack.pop()
            next_op.next(self)

    def get_total_max(self):
        return max(self.visited_max.values())

    def _generate_starting_opens(self, starting_pos, max_step_nr):
        stack = []
        for next_valve in self.valves:
            steps_left = max_step_nr - self.distance_map.get((starting_pos, next_valve.id)) - 1
            open = Open(next_valve, State(steps_left, 0, 0))
            stack.append(open)

        return stack


class Open:
    def __init__(self, valve, state):
        self.valve = valve
        self.state = state

    def next(self, propagator):
        state = self.state\
            .add_total(self.state.steps_left * self.valve.flow_rate)\
            .open_valve(self.valve.pos)
        propagator.visited_max[state.valves_bitmap] = max(
            propagator.visited_max.get(state.valves_bitmap, 0),
            state.total)

        for next_valve in propagator.valves:
            new_steps_left = state.steps_left - propagator.distance_map.get((self.valve.id, next_valve.id)) - 1
            if next_valve.pos & state.valves_bitmap or new_steps_left <= 0:
                continue

            propagator.stack.append(Open(next_valve, state.set_steps_left(new_steps_left)))

    def __repr__(self):
        return 'OPEN: @' + self.valve.id + ' #' + str(self.steps_left)


class Valve:
    def __init__(self, id, flow_rate, neighbors):
        self.id = id
        self.flow_rate = flow_rate
        self.neighbors = neighbors
        self.pos = None

    def set_pos(self, pos):
        self.pos = pos

    def __repr__(self):
        return 'id: {} pos:{}'.format(self.id, self.pos)


def build_valve_distance_map(start_config, valve_ids):
    distances = dict(start_config.items())

    for inter in valve_ids:
        for left in valve_ids:
            for right in valve_ids:
                curr_valves = (left, right)
                distance = min(
                    [
                        distances.get((left, right)),
                        distances.get((left, inter)) + distances.get((inter, right))
                    ]
                )
                distances[curr_valves] = distance

    return distances


def build_starting_distance_map(valves):
    valve_ids = [valve.id for valve in valves]
    distances = dict()
    for left in valve_ids:
        for right in valve_ids:
            distance = float('inf')

            if left == right:
                distance = 0

            distances[(left, right)] = distance

    for valve in valves:
        for neighbor in valve.neighbors:
            distances[(valve.id, neighbor)] = 1

    return distances


if __name__ == '__main__':
    valves = []

    with open('day16_input.txt') as file:
        for i, line in enumerate(file):
            flow_rate = int(re.findall(r'-?\d+', line)[0])
            all_valve = re.findall(r'[A-Z][A-Z]', line)
            valve_id = all_valve[0]
            neighbors = all_valve[1:]

            valves.append(Valve(valve_id, flow_rate, neighbors))

    starting_distance_map = build_starting_distance_map(valves)
    distance_map = build_valve_distance_map(starting_distance_map, [valve.id for valve in valves])

    non_zero_flow_valves = [valve for valve in valves if valve.flow_rate != 0]

    for i, valve in enumerate(non_zero_flow_valves):
        valve.set_pos(1 << i)
    # part 1
    propagator = Propagator(non_zero_flow_valves, distance_map)
    propagator.run('AA', 30)
    # 1873
    print(propagator.get_total_max())

    # part 2
    propagator = Propagator(non_zero_flow_valves, distance_map)
    propagator.run('AA', 40)
    combined_total = max(
        total_1 + total_2
        for state_1, total_1 in propagator.visited_max.items()
        for state_2, total_2 in propagator.visited_max.items()
        if not state_1 & state_2
    )

    # 2425
    print(combined_total)


