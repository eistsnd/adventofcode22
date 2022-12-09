from enum import Enum


class Outcomes(Enum):
    WIN = 6
    DRAW = 3
    LOSS = 0


class Choices(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __lt__(self, other):
        if self == Choices.ROCK and other == Choices.PAPER:
            return True

        if self == Choices.PAPER and other == Choices.SCISSORS:
            return True

        if self == Choices.SCISSORS and other == Choices.ROCK:
            return True

        return False

    def versus(self, opponent):
        if self > opponent:
            return Outcomes.WIN
        if self == opponent:
            return Outcomes.DRAW
        if self < opponent:
            return Outcomes.LOSS

    def match_outcome(self, outcome):
        if outcome == Outcomes.DRAW:
            return self

        if outcome == Outcomes.WIN:
            # this is da way
            return [choice for choice in Choices if choice > self][0]

        if outcome == Outcomes.LOSS:
            # this is da way
            return [choice for choice in Choices if choice < self][0]


def calculate_score(outcome, choice):
    return outcome.value + choice.value
