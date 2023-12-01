# Advent of code, day 1, puzzle 1


with open('input-1.txt', 'r') as f:
    puzzle_inputs = f.readlines()

answers_list = []
for line in puzzle_inputs:
    digits_list = []
    line = line.strip()
    for char in line:
        if char.isdigit():
            digits_list.append(char)
    number = int(digits_list[0]+digits_list[-1])
    answers_list.append(number)


# First solution
print(sum(answers_list))
