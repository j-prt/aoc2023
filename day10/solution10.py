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


# Puzzle 2

with open('example2.txt') as f:
    example2 = f.read()

def parse_inputs_2(inputs):
    rows = inputs.rstrip().split('\n')
    expanded_rows = []
    for i in range(len(rows)*2):
        if i % 2 ==0:
            new_row = ' '
            for j in range(len(rows[0])*2):
                if j % 2 == 0:
                    new_row += rows[i//2][j//2]
                else:
                    new_row += ' '
        else:
            new_row = ' ' + ' ' * len(rows[0]*2)
        expanded_rows.append(list(new_row))
    return expanded_rows

def get_first_step_2(start_loc, pipe_grid):
    y, x = start_loc
    try:
        if pipe_grid[y+2][x] in '|LJ':
            pipe_grid[y+1][x] = '*'
            return (y+2, x)
    except IndexError:
        pass
    try:
        if pipe_grid[y-2][x] in '|F7':
            pipe_grid[y-1][x] = '*'
            return (y-2, x)
    except IndexError:
        pass
    try:
        if pipe_grid[y][x-2] in '-FL':
            pipe_grid[y][x-1] = '*'
            return (y, x-2)
    except IndexError:
        pass
    raise ValueError

def get_connections_2(loc, pipe_grid):
    y, x = loc
    current = pipe_grid[y][x]
    match current:
        case '|': # North-South
            return (y-2, x), (y+2, x), (y-1, x), (y+1, x)
        case '-': # East-West
            return (y, x+2), (y, x-2), (y, x+1), (y, x-1)
        case 'L': # North-East
            return (y-2, x), (y, x+2), (y-1, x), (y, x+1)
        case 'J': # North-West
            return (y-2, x), (y, x-2), (y-1, x), (y, x-1)
        case '7': # South-West
            return (y+2, x), (y, x-2), (y+1, x), (y, x-1)
        case 'F': # South-East
            return (y+2, x), (y, x+2), (y+1, x), (y, x+1)
        case _:
            raise ValueError

def get_path(inputs):
    pipe_grid = parse_inputs_2(inputs)
    start = get_start_location(pipe_grid)
    current = get_first_step_2(start, pipe_grid)

    steps = 1
    prev = start
    while pipe_grid[current[0]][current[1]] != 'S':
        conn1, conn2, gap1, gap2 = get_connections_2(current, pipe_grid)
        pipe_grid[current[0]][current[1]] = '*'
        if conn1 == prev:
            prev, current = current, conn2
            pipe_grid[gap2[0]][gap2[1]] = '*'
        else:
            prev, current = current, conn1
            pipe_grid[gap1[0]][gap1[1]] = '*'
        steps +=1
    pipe_grid[current[0]][current[1]] = '*'

    return pipe_grid


# Quick visualization
# for row in parse_inputs_2(example2):
#     print(''.join(row))

# print('-------------------')

# for row in get_path(example2):
#     print(''.join(row))


# Start in the upper left corner. Add each adjacent point to a queue.
# Move to the first point in the queue. Check if it's a star - if it's
# a star, don't add any neighbours, don't modify it, and move to the next
# point. If it isn't a star, add it to the 'outside' list. Add its neighbours
# to the 'to-visit' queue.

def solve_2(inputs):
    path_grid = get_path(inputs)
    start = 0, 0
    visited = set()
    symbols = []
    to_visit = [start]
    max_y = len(path_grid) - 1
    max_x = len(path_grid[0]) - 1

    while to_visit:
        y, x = to_visit.pop()
        if (sym := path_grid[y][x]) == '*':
            continue
        if (y, x) in visited:
            continue
        if sym not in '* ':
            symbols.append(sym)
        visited.add((y, x))
        if x != max_x:
            to_visit.append((y, x+1))
        if x != 0:
            to_visit.append((y, x-1))
        if y != max_y:
            to_visit.append((y+1, x))
        if y != 0:
            to_visit.append((y-1, x))
    all_symbols = []
    for row in range(len(path_grid)):
        for index in range(len(path_grid[0])):
            if (sym := path_grid[row][index]) not in '* ':
                all_symbols.append(sym)

    print(len(all_symbols) - len(symbols))


# Test
solve_2(example2)

# Solve
solve_2(inputs)
