# Advent of code, day 10

# Puzzle 1

with open('example.txt') as f:
    example = f.read()

with open('input10.txt') as f:
    inputs = f.read()

def parse_inputs(inputs):
    rows = inputs.rstrip().split('\n')
    return [list(row) for row in rows]

def get_start_location(pipe_grid):
    for row_count in range(len(pipe_grid)):
        if 'S' in (row := pipe_grid[row_count]):
            start = row.index('S')
            break
    return row_count, start

def get_first_step(start_loc, pipe_grid):
    y, x = start_loc
    try:
        if pipe_grid[y+1][x] in '|LJ':
            return (y+1, x)
    except IndexError:
        pass
    try:
        if pipe_grid[y-1][x] in '|F7':
            return (y-1, x)
    except IndexError:
        pass
    try:
        if pipe_grid[y][x-1] in '-FL':
            return (y, x-1)
    except IndexError:
        pass
    raise ValueError

def get_connections(loc, pipe_grid):
    y, x = loc
    current = pipe_grid[y][x]
    match current:
        case '|': # North-South
            return (y-1, x), (y+1, x)
        case '-': # East-West
            return (y, x+1), (y, x-1)
        case 'L': # North-East
            return (y-1, x), (y, x+1)
        case 'J': # North-West
            return (y-1, x), (y, x-1)
        case '7': # South-West
            return (y+1, x), (y, x-1)
        case 'F': # South-East
            return (y+1, x), (y, x+1)
        case _:
            raise ValueError

def solve(inputs):
    pipe_grid = parse_inputs(inputs)
    start = get_start_location(pipe_grid)
    current = get_first_step(start, pipe_grid)

    steps = 1
    prev = start
    while pipe_grid[current[0]][current[1]] != 'S':
        conn1, conn2 = get_connections(current, pipe_grid)
        if conn1 == prev:
            prev, current = current, conn2
        else:
            prev, current = current, conn1
        steps +=1

    print(steps//2)

# Test
solve(example)

# Solve
solve(inputs)
