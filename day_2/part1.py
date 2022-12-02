# all outcomes pre-determined so build a model for each combination

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
        score += SCORE_MODEL[line.strip()]
print(score)

