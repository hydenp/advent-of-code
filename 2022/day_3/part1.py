def find_duplicate(input_line):
    """find the character that exists in both halves of the input_line"""
    first_have_characters = set(input_line[:len(input_line) // 2])
    for c in input_line[len(input_line) // 2:]:
        if c in first_have_characters:
            return c


def find_duplicate_2(input_line):
    return (set(input_line[:len(input_line)//2]) & set(input_line[len(input_line)//2:])).pop()


def character_score(character):
    """calculate score of the given character"""
    character_ascii_value = ord(character)
    # lower case
    if character_ascii_value > 90:
        return character_ascii_value - 96
    # upper case
    else:
        return character_ascii_value - 64 + 26


total_score = 0
with open('input.txt', 'r') as file:
    for line in file:
        total_score += character_score(find_duplicate_2(line))
print(total_score)


total_score = 0
with open('input.txt', 'r') as file:
    for line in file:
        total_score += character_score(find_duplicate_2(line.strip()))
print(total_score)
