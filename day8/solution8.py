# Advent of code, day 8

# Puzzle 1

with open('example.txt') as f:
    example = f.read()

with open('input8.txt') as f:
    inputs = f.read()

def parse_inputs(inputs):
    instructions, nodes = inputs.split('\n\n')
    nodes = nodes.rstrip().split('\n')
    clean_nodes = []

    for node in nodes:
        name, edges = node.split('=')
        name = name.strip()
        edges = edges[2:-1].split(',')
        edges[1] = edges[1].strip()

        clean_nodes.append((name, tuple(edges)))

    return instructions, clean_nodes

def solve(inputs):
    from itertools import cycle

    instructions, nodes = parse_inputs(inputs)
    instructions = cycle(instructions)

    node_dict = {}
    for node in nodes:
        node_dict[node[0]] = node[1]

    cur_node = 'AAA'
    steps = 0
    for LR in instructions:
        steps += 1
        if LR == 'L':
            cur_node = node_dict[cur_node][0]
        if LR == 'R':
            cur_node = node_dict[cur_node][1]
        if cur_node == 'ZZZ':
            break

    print(steps)

# Test
solve(example)

# Solve
solve(inputs)


# Puzzle 2

with open('example2.txt') as f:
    example2 = f.read()

def solve_2(inputs):
    from itertools import cycle
    from math import lcm

    instructions, nodes = parse_inputs(inputs)
    instructions_cycle = cycle(instructions)

    node_dict = {}
    for node in nodes:
        node_dict[node[0]] = node[1]

    starting_nodes = [node for node in node_dict.keys() if node.endswith('A')]
    steps = []
    for node in starting_nodes:
        curr_steps = 0
        curr = node
        instructions_cycle = cycle(instructions)
        for LR in instructions_cycle:
            curr_steps += 1
            if LR == 'L':
                curr = node_dict[curr][0]
            if LR == 'R':
                curr = node_dict[curr][1]
            if curr.endswith('Z'):
                steps.append(curr_steps)
                break

    print(lcm(*steps))

# Test
solve_2(example2)

# Solve
solve_2(inputs)
