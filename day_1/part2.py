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


if __name__ == '__main__':
    print(part2_solution())
