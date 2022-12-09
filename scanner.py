from util import flat_map, g_step
from point import directions
HIDDEN = 0
VISIBLE = 1


class Scanner:
    def __init__(self, terrain):
        self.terrain = terrain

        self.cols = len(terrain[0])
        self.rows = len(terrain)
        # 0 means not visible 1 means visible

        self.visibility_map = [[HIDDEN] * self.cols for _ in range(self.rows)]
        self.scenic_view_map = [[HIDDEN] * self.cols for _ in range(self.rows)]

    def scan_visibility(self):
        for i in range(self.cols):
            for j in range(self.rows):
                tree_height = self.terrain[i][j]

                for direction in directions:
                    if self.visibility_map[i][j] == HIDDEN:
                        step = g_step(self.terrain, i, j, *direction)
                        for next_tree_height in step:
                            if tree_height <= next_tree_height:
                                break
                        else:
                            self.visibility_map[i][j] = VISIBLE

    def count_visible(self):
        return sum(flat_map(self.visibility_map))

    def scan_scenic_view(self):
        for i in range(self.cols):
            for j in range(self.rows):
                total_score = 1
                tree_height = self.terrain[i][j]

                for direction in directions:
                    score_in_direction = 0
                    step = g_step(self.terrain, i, j, *direction)

                    for next_tree_height in step:
                        score_in_direction += 1
                        if tree_height <= next_tree_height:
                            break

                    total_score *= score_in_direction

                self.scenic_view_map[i][j] = total_score

    def get_best_scenic_view(self):
        return max(flat_map(self.scenic_view_map))

    def print_visibility_map(self):
        for row in self.visibility_map:
            print(''.join([str(i) for i in row]))

