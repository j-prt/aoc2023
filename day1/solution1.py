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


# Puzzle 2


digits_mapping = {
    'one': '1ne',
    'two': '2wo',
    'three': '3hree',
    'four': '4our',
    'five': '5ive',
    'six': '6ix',
    'seven': '7even',
    'eight': '8ight',
    'nine': '9ine',
}


answers_list = []
for line in puzzle_inputs:
    digits_list = []
    line = line.strip()
    candidates = [digit for digit in digits_mapping.keys() if digit in line]
    candidates = sorted(candidates, key=lambda x: line.find(x))
    while candidates:
        candidate = candidates[0]
        if candidate in line:
            line = line.replace(candidate, digits_mapping[candidate])
        candidates = [digit for digit in digits_mapping.keys() if digit in line]
        candidates = sorted(candidates, key=lambda x: line.find(x))
    for char in line:
        if char.isdigit():
            digits_list.append(char)
    number = int(digits_list[0]+digits_list[-1])
    answers_list.append(number)


# Second Solution
print(sum(answers_list))
