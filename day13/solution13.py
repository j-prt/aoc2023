# Advent of code, day 13

# Puzzle 1

with open('example.txt') as f:
    example = f.read()

with open('input13.txt') as f:
    inputs = f.read()

def parse_inputs(inputs):
    paths = inputs.rstrip().split('\n\n')
    return paths

def get_columns(path):
    width = path.find('\n') + 1
    height = (len(path)+1) //  (width)
    columns = []
    for col in range(width-1):
        curr = ''
        for row in range(height):
            curr += path[col + row * width]
        columns.append(curr)

    return columns

def get_rows(path):
    return path.split('\n')

def find_mirror(split_path):
    # Find possible centres
    locations = []
    for idx, path in enumerate(split_path[1:], 1):
        if path == split_path[idx-1]:
            locations.append(idx-1)

    # Measure the lines of reflections, if any
    max_reflect = candidate = 0
    for loc in locations:
        left = loc
        right = loc + 1
        reflect = 0

        # Avoiding index errors
        while (left >= 0 and right < len(split_path)):
            if split_path[left] != split_path[right]:
                reflect = 0
                break
            reflect += 1
            left -= 1
            right += 1
        if reflect > max_reflect:
            max_reflect = reflect
            candidate = loc

    return max_reflect, candidate

def solve(inputs):
    total = 0
    all_paths = parse_inputs(inputs)
    for path in all_paths:
        columns = get_columns(path)
        rows = get_rows(path)
        col_reflect = find_mirror(columns)
        row_reflect = find_mirror(rows)

        if col_reflect[0] > row_reflect[0]:
            total += col_reflect[1] + 1
        else:
            total += 100 * (row_reflect[1] + 1)

    print(total)

# Test
solve(example)

# Solve
solve(inputs)
