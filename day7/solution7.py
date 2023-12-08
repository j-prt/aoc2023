# Advent of code, day 7

# Puzzle 1

with open('example.txt') as f:
    example = f.read()

with open('input7.txt') as f:
    inputs = f.read()

def parse_inputs(inputs):
    hands, bids = [], []
    for round in inputs.rstrip().split('\n'):
        hand, bid = round.split()
        hands.append(list(hand))
        bids.append(int(bid))

    return zip(hands, bids)

VALUE_MAP = dict(zip(list('AKQJT98765432'), range(14, 1, -1)))

def five_oak(hand):
    return len(set(hand)) == 1

def four_oak(hand):
    hand = sorted(hand)
    return (len(set(hand[:-1])) == 1) or (len(set(hand[1:])) == 1)

def full_house(hand):
    return len(set(hand)) == 2

def three_oak(hand):
    hand = sorted(hand)
    return ((len(set(hand[1:4])) == 1)
            or (len(set(hand[:3])) == 1)
            or (len(set(hand[2:])) == 1))

def two_pair(hand):
    return len(set(hand)) == 3

def one_pair(hand):
    return len(set(hand)) == 4

def score(hand):
    if five_oak(hand):
        points = 7**7
    elif four_oak(hand):
        points = 7**6
    elif full_house(hand):
        points = 7**5
    elif three_oak(hand):
        points = 7**4
    elif two_pair(hand):
        points = 7**3
    elif one_pair(hand):
        points = 7**2
    else:
        points = 7

    positions = [14**5, 14**4, 14**3, 14**2, 14]
    n = sum(map(lambda x: VALUE_MAP[x[1]] * x[0], zip(positions, hand)))
    return points * n

def solve(inputs):
    rounds = parse_inputs(inputs)
    rounds = sorted(rounds, key=lambda x: score(x[0]), reverse=True)
    total = 0
    for (_, bid), rank in zip(rounds, range(len(rounds), 0, -1)):
        total += bid * rank

    print(total)

# Test
solve(example)

# Solve
solve(inputs)


# Puzzle 2

VALUE_MAP = dict(zip(list('AKQT98765432J'), range(14, 1, -1)))

def pre_score(hand):
    if five_oak(hand):
        return 7**7
    elif four_oak(hand):
        return 7**6
    elif full_house(hand):
        return 7**5
    elif three_oak(hand):
        return 7**4
    elif two_pair(hand):
        return 7**3
    elif one_pair(hand):
        return 7**2
    else:
        return 7

def score(hand):
    if not (j_count := hand.count('J')):
        points = pre_score(hand)
    else:
        j_less = [card for card in hand if card != 'J']
        no_j = len(set(j_less))

        match j_count, no_j:
            case _, 1|0:
                points = 7**7 # Five of a kind
            case 2|3, 2:
                points = 7**6 # Four of a kind
            case 1|2, 3:
                points = 7**4 # Three of a kind
            case 1, 2:
                points = 7**6 if three_oak(j_less + ['F']) else 7**5 # 4OAK/FH
            case 1, 4:
                points = 7**2 # One pair

    positions = [14**5, 14**4, 14**3, 14**2, 14]
    n = sum(map(lambda x: VALUE_MAP[x[1]] * x[0], zip(positions, hand)))
    return points * n

# Test
solve(example)

# Solve
solve(inputs)
