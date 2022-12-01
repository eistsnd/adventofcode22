import functools
import operator


class Bag:
    def __init__(self):
        self._bag = []

    def add(self, food):
        self._bag.append(food)

    def get_total_calories(self):
        return functools.reduce(operator.add, [food.calories for food in self._bag])


class Food:
    def __init__(self, calories: int):
        self.calories = calories
