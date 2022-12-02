import sys


def part2_solution():
    max_elf_calories = [0, 0, 0]
    with open('input.txt', 'r') as file:
        current_elf_calories = 0
        for line in file:
            if line == '\n':
                if current_elf_calories > max_elf_calories[0]:
                    max_elf_calories[1:] = max_elf_calories[:2]
                    max_elf_calories[0] = current_elf_calories
                elif current_elf_calories > max_elf_calories[0]:
                    max_elf_calories[2] = max_elf_calories[1]
                    max_elf_calories[1] = current_elf_calories
                elif current_elf_calories > max_elf_calories[0]:
                    max_elf_calories[2] = current_elf_calories
                current_elf_calories = 0
            else:
                current_elf_calories += int(line.strip('\n'))

    return sum(max_elf_calories)


def part2_recursive_solution(max_elf_calories, current_elf_calories, lines, line_index):
    if line_index == len(lines):
        return sum(max_elf_calories)
    if lines[line_index] == '\n':
        if current_elf_calories > max_elf_calories[0]:
            return part2_recursive_solution([current_elf_calories, *max_elf_calories[:2]], 0, lines, line_index + 1)
        elif current_elf_calories > max_elf_calories[1]:
            return part2_recursive_solution([max_elf_calories[0], current_elf_calories, max_elf_calories[1]], 0,
                                            lines, line_index + 1)
        elif current_elf_calories > max_elf_calories[2]:
            return part2_recursive_solution([*max_elf_calories[:2], current_elf_calories], 0, lines, line_index + 1)
        else:
            return part2_recursive_solution(max_elf_calories, 0, lines, line_index + 1)
    else:
        return part2_recursive_solution(max_elf_calories, current_elf_calories + int(lines[line_index].strip('\n')),
                                        lines, line_index + 1)


if __name__ == '__main__':
    print(part2_solution())

    sys.setrecursionlimit(2_500)
    input_lines = open("input.txt").readlines()
    print(part2_recursive_solution([0, 0, 0], 0, input_lines, 0))
