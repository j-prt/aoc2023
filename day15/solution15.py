# Advent of code, day 15

# Puzzle 1

with open('example.txt') as f:
    example = f.read()

with open('input15.txt') as f:
    inputs = f.read()

def parse_inputs(inputs):
    return inputs.rstrip().split(',')

def HASH(instr):
    value = 0
    for char in instr:
        value = (value + ord(char)) * 17 % 256
    return value

def solve(inputs):
    instructions = parse_inputs(inputs)

    total = 0
    for instr in instructions:
        total += HASH(instr)

    print(total)

# Test
solve(example)

# Solve
solve(inputs)
