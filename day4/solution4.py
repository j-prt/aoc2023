# Advent of code, day 4


# Puzzle 1

with open('example.txt') as f:
    example = [line.strip() for line in f.readlines()]

def parse_card(line):
    card_number, card = line.split(':')
    winning, user = card.split('|')

    return int(card_number[-1]), winning.split(), user.split()

def score_card(winning, user):
    winning, user = set(winning), set(user)
    if (points := winning.intersection(user)):
        return 2 ** (len(points) - 1)
    return 0

def solve(lines):
    total = 0
    for line in lines:
        _, winning, user = parse_card(line)
        total += score_card(winning, user)
    print(total)

# Test
solve(example)

with open('input4.txt') as f:
    inputs = [line.strip() for line in f.readlines()]

# Get the answer!
solve(inputs)


# Puzzle 2

def score_card_2(winning, user):
    winning, user = set(winning), set(user)
    return len(winning.intersection(user))

def solve_2(lines):
    total = 0
    multiples = [1]*10 # Max 10 winning numbers
    for line in lines:
        multiple = multiples.pop(0)
        multiples.append(1)
        _, winning, user = parse_card(line)
        score = score_card_2(winning, user)
        for i in range(score):
            multiples[i] += multiple
        total += multiple
    print(total)

# Test
solve_2(example)

# Solution!
solve_2(inputs)
