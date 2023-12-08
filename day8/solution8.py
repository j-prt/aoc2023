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
