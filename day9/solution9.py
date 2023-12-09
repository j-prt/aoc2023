# Advent of code, day 9

# Puzzle 1

with open('example.txt') as f:
    example = f.read()

with open('input9.txt') as f:
    inputs = f.read()

def parse_inputs(inputs):
    histories = inputs.rstrip().split('\n')
    histories = [[int(dp) for dp in hist.split()] for hist in histories]
    return histories

def diff(array):
    array = array[:]
    differ = [0] + array[:-1]
    for i in range(1, len(differ)):
        array[i] -= differ[i]
    return array[1:]

def solve(inputs):
    histories = parse_inputs(inputs)
    total = 0
    for hist in histories:
        diffed = [hist]
        while sum(hist) != 0:
            hist = diff(hist)
            diffed.append(hist)
        extra = sum(hist[-1] for hist in diffed)
        total += extra

    print(total)

# Test
solve(example)

# Solve
solve(inputs)
