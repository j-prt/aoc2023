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
for row in expand_columns(expand_rows(parse_inputs(example))):
    print(''.join(row))

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
