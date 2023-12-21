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


# Puzzle 2

def HASHMAP(instr):
    if '-' in instr:
        code, length = instr.split('-')
        add = False
    else:
        code, length = instr.split('=')
        add = True

    box_no = HASH(code)
    if not boxes.get(box_no):
        boxes[box_no] = {}

    if add:
        boxes[box_no][code] = length
    else:
        boxes[box_no].pop(code, None)

def solve_2(inputs):
    instructions = parse_inputs(inputs)

    for instr in instructions:
        HASHMAP(instr)

    total = 0
    for box in boxes:
        num = box + 1
        subtotal = 0
        for idx, val in enumerate(boxes[box].values(), start=1):
            subtotal += num * idx * int(val)
        total += subtotal

    print(total)

boxes = {}

# Test
solve_2(example)

boxes = {}

# Solve
solve_2(inputs)
