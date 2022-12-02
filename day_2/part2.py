
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

# points per play
X = 1  # rock
Y = 2  # paper
Z = 3  # scissors

SCORE_MODEL = {
    'A X': DRAW + X,
    'B Y': DRAW + Y,
    'C Z': DRAW + Z,
    'A Z': LOSS + Z,
    'B X': LOSS + X,
    'C Y': LOSS + Y,
    'A Y': WIN + Y,
    'B Z': WIN + Z,
    'C X': WIN + X,
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

