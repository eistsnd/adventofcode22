from rps_game import Choices, Outcomes, calculate_score


opponent_choice = {
    'A': Choices.ROCK,
    'B': Choices.PAPER,
    'C': Choices.SCISSORS,
}

my_choice = {
    'X': Choices.ROCK,
    'Y': Choices.PAPER,
    'Z': Choices.SCISSORS,
}

desired_outcome = {
    'X': Outcomes.LOSS,
    'Y': Outcomes.DRAW,
    'Z': Outcomes.WIN,
}


if __name__ == '__main__':

    with open('day2_input.txt', 'r') as file:
        games = [line.rstrip().split() for line in file]

    # part 1
    total_score_1 = sum(
        (
            calculate_score(
                my_choice[game[1]].versus(opponent_choice[game[0]]),
                my_choice[game[1]]
            )
            for game in games
        )
    )

    print(total_score_1)

    # part 2
    total_score_2 = sum(
        (
            calculate_score(
                desired_outcome[game[1]],
                opponent_choice[game[0]].match_outcome(desired_outcome[game[1]])
            )
            for game in games
        )
    )

    print(total_score_2)
