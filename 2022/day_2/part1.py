# all outcomes pre-determined so build a model for each combination

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
        score += SCORE_MODEL[line.strip()]
print(score)

