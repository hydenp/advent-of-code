def find_badge(line_1, line_2, line_3):
    return (set(line_1) & set(line_2) & set(line_3)).pop()


def character_score(character):
    """calculate score of the given character"""
    character_ascii_value = ord(character)
    # lower case
    if character_ascii_value > 90:
        return character_ascii_value - 96
    # upper case
    else:
        return character_ascii_value - 64 + 26


lines = open('input.txt').readlines()
total_score = 0
for i in range(0, len(lines), 3):
    total_score += character_score(find_badge(lines[i].strip(), lines[i + 1].strip(), lines[i + 2].strip()))
print(total_score)
