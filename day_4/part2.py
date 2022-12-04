score = 0
with open('input.txt', 'r') as file:
    for line in file:
        group1, group2 = line.strip().split(',')

        start_1, end_1 = group1.split('-')
        start_2, end_2 = group2.split('-')

        set_1 = set(range(int(start_1), int(end_1) + 1))
        set_2 = set(range(int(start_2), int(end_2) + 1))

        score += ((len(set_1) + len(set_2)) != len(set_1.union(set_2)))

print(score)
