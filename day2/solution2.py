# Advent of code, day 2, puzzle 1

example = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

MAX_VALS = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def parse_game(line):
    # print(line)
    game, contents = line.split(':')
    game_number = int(game.split()[1])

    game_data = []
    rounds = contents.split(';')
    for round in rounds:
        pulls = round.split(',')
        round_counts = [pull.split() for pull in pulls]
        round_dict = {items[1]:int(items[0]) for items in round_counts}
        game_data.append(round_dict)

    return game_number, game_data

def check_game(max_vals, game_data):
    return all(max_vals[key] >= game.get(key, 0) for key
                in max_vals for game in game_data)

# Test on example data
total = 0
for line in example.split('\n'):
    # print(parse_game(line))
    num, game_data = parse_game(line)
    if check_game(MAX_VALS, game_data):
        total += num

print('Example 1: ', total)

# Get the actual total
total = 0
with open('input2.txt', 'r') as f:
    for line in f.readlines():
        num, game_data = parse_game(line)
        if check_game(MAX_VALS, game_data):
            total += num

# Solution
print('Solution 1:', total)


# Puzzle 2


example = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


# Tweaking the previous function
def parse_game_2(line):
    _, contents = line.split(':') # Don't need the game #

    game_data = []
    rounds = contents.split(';')
    for round in rounds:
        pulls = round.split(',')
        round_counts = [pull.split() for pull in pulls]
        round_dict = {items[1]:int(items[0]) for items in round_counts}
        game_data.append(round_dict)

    return game_data

def score_game(game_data):
    from operator import mul
    from functools import reduce

    max_dict = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    for key in max_dict:
        for game in game_data:
            if (val := game.get(key, 0)) > max_dict[key]:
                max_dict[key] = val

    return reduce(mul, max_dict.values())


# Example solution
total = 0
for line in example.split('\n'):
    game_data = parse_game_2(line)
    total += score_game(game_data)
print('Example 2:', total)


# Actual solution
total = 0
with open('input2.txt', 'r') as f:
    for line in f.readlines():
        game_data = parse_game_2(line)
        total += score_game(game_data)


# Solution
print('Solution 2:', total)
