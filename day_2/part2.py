
# Again, everything has exactly one move to respond with so simply create
# a decision model

# X - loose
# Y - draw
# Z - Win
ROCK = 'X'
PAPER = 'Y'
SCISSORS = 'Z'

MOVE_MODEL = {
    'A X': SCISSORS,  # lose against rock
    'B Y': PAPER,  # draw against paper
    'C Z': ROCK,  # win against scissors
    'A Z': PAPER,  # win against rock
    'B X': ROCK,  # lose against paper
    'C Y': SCISSORS,  # draw against scissors
    'A Y': ROCK,  # draw against rock
    'B Z': SCISSORS,  # win against paper
    'C X': PAPER,  # loose against scissors
}

# points per result
LOSS = 0
DRAW = 3
WIN = 6

# points per results
ROCK = 1  # rock
PAPER = 2  # paper
SCISSORS = 3  # scissors

SCORE_MODEL = {
    'A X': DRAW + ROCK,  # draw with rock
    'B Y': DRAW + PAPER,  # draw with paper
    'C Z': DRAW + SCISSORS,  # draw with scissors
    'A Z': LOSS + SCISSORS,  # loose to rock with scissors
    'B X': LOSS + ROCK,  # loose to paper with rock
    'C Y': LOSS + PAPER,  # loose to scissors with paper
    'A Y': WIN + PAPER,  # win with paper against rock
    'B Z': WIN + SCISSORS,  # win wih scissors against paper
    'C X': WIN + ROCK,  # win with rock against scissors
}

score = 0
with open('input.txt', 'r') as file:
    for line in file:
        clean_line = line.strip()
        move = MOVE_MODEL[clean_line]
        score += SCORE_MODEL[
            f'{clean_line[0]} {move}'
        ]
print(score)

