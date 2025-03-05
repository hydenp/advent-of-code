import sys


def part1_solution():
    max_elf_calories = 0
    with open('input.txt', 'r') as file:
        current_elf_calories = 0
        for line in file:
            if line == '\n':
                if current_elf_calories > max_elf_calories:
                    max_elf_calories = current_elf_calories
                current_elf_calories = 0
            else:
                current_elf_calories += int(line.strip('\n'))

    return max_elf_calories


def part1_recursive_solution(max_elf_cals, current_elf_cals, lines, line_index):
    if line_index == len(lines):
        return max_elf_cals
    if lines[line_index] == '\n':
        if current_elf_cals > max_elf_cals:
            return part1_recursive_solution(current_elf_cals, 0, lines, line_index+1)
        else:
            return part1_recursive_solution(max_elf_cals, 0, lines, line_index+1)
    else:
        return part1_recursive_solution(max_elf_cals, current_elf_cals+int(lines[line_index].strip('\n')), lines, line_index+1)


if __name__ == '__main__':
    print(part1_solution())

    sys.setrecursionlimit(2_500)
    input_lines = open("input.txt").readlines()
    print(part1_recursive_solution(0, 0, input_lines, 0))
