# Advent of code, day 10

# Puzzle 1

from dataclasses import dataclass
from itertools import combinations

with open('example.txt') as f:
    example = f.read()

with open('input11.txt') as f:
    inputs = f.read()

def parse_inputs(inputs):
    return [list(row) for row in inputs.rstrip().split('\n')]

# print(parse_inputs(example))

def expand_rows(star_map):
    new_map = []
    width = len(star_map[0])
    for row in star_map:
        if all(point == '.' for point in row):
            new_map.append(['.'] * width)
        new_map.append(row)
    return new_map

def expand_columns(star_map):
    length = len(star_map)
    width = len(star_map[0])
    new_map = [[] for _ in range(length)]
    for idx in range(width):
        if all(row[idx] == '.' for row in star_map):
            for new_row in new_map:
                new_row.extend(['.', '.'])
        else:
            for row_idx in range(length):
                new_map[row_idx].append(star_map[row_idx][idx])
    return new_map

# Visualize
# for row in expand_columns(expand_rows(parse_inputs(example))):
#     print(''.join(row))

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def l1_dist(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

def populate_galaxies(star_map):
    galaxies = []
    for row_idx, row in enumerate(star_map):
        for col_idx, val in enumerate(row):
            if val == '#':
                galaxies.append(Point(col_idx, row_idx))
    return galaxies

def solve(inputs):
    star_map = parse_inputs(inputs)
    star_map = expand_columns(star_map)
    star_map = expand_rows(star_map)

    galaxies = populate_galaxies(star_map)
    pairs = combinations(galaxies, 2)

    total = sum(a.l1_dist(b) for a, b in pairs)
    print(total)

# Test
solve(example)

# Solve
solve(inputs)


# Puzzle 2

# Rows must be called first
def expand_rows_2(star_map):
    new_map = []
    width = len(star_map[0])
    for row in star_map:
        if all(point == '.' for point in row):
            new_map.append(['H'] * width)
        else:
            new_map.append(row)
    return new_map

# Columns are called next
def expand_columns_2(star_map):
    length = len(star_map)
    width = len(star_map[0])
    new_map = [[] for _ in range(length)]
    for idx in range(width):
        if all(row[idx] == '.' or row[idx] == 'H' for row in star_map):
            for row_idx in range(length):
                if star_map[row_idx][idx] == '.':
                    new_map[row_idx].append('W')
                elif star_map[row_idx][idx] == 'H':
                    new_map[row_idx].append('M')
        else:
            for row_idx in range(length):
                new_map[row_idx].append(star_map[row_idx][idx])
    return new_map

# Visualize - H: 1m height, W: 1m width, M: 1m h and w.
# for row in expand_columns_2(expand_rows_2(parse_inputs(example))):
#     print(''.join(row))

def populate_galaxies_2(star_map):
    galaxies = []
    row_counter = 0
    for row in star_map:
        if row[0] in 'HM':
            row_counter += 1_000_000
            # row_counter += 10 # Test w/ example
        else:
            row_counter += 1

        col_counter = 0
        for val in row:
            if val in 'WM':
                col_counter += 1_000_000
                # col_counter += 10 # Test w/ example
            else:
                col_counter += 1

            if val == '#':
                galaxies.append(Point(col_counter, row_counter))

    return galaxies

def solve_2(inputs):
    star_map = parse_inputs(inputs)
    star_map = expand_rows_2(star_map)
    star_map = expand_columns_2(star_map)

    galaxies = populate_galaxies_2(star_map)
    pairs = combinations(galaxies, 2)

    total = sum(a.l1_dist(b) for a, b in pairs)
    print(total)

# Test
solve_2(example)

# Solve
solve_2(inputs)
