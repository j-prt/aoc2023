# Advent of code, day 14

# Puzzle 1
import re
from itertools import zip_longest

with open('example.txt') as f:
    example = f.read()

with open('input14.txt') as f:
    inputs = f.read()

def columnize(path):
    width = path.find('\n') + 1
    height = (len(path)+1) //  (width)
    columns = []
    for col in range(width-1):
        curr = ''
        for row in range(height):
            curr += path[col + row * width]
        columns.append(curr)

    return columns

def roll(column):
    # Record the hash sizes
    hashes = re.findall('[#]+', column)

    # Split on hashes, convert to lists, and sort
    col_sections = column.split('#')
    sorted_sections = []
    for section in col_sections:
        if section:
            sorted_sections.append(sorted(list(section), reverse=True))

    # Rebuilding with original hash sizes
    column = '' if not column.startswith('#') else hashes.pop(0)
    for hash, section in zip_longest(hashes, sorted_sections, fillvalue=''):
        column += ''.join(section) + hash

    return column

def solve(inputs):
    columns = columnize(inputs)
    rolled_columns = []
    for column in columns:
        rolled_columns.append(roll(column))

    total = 0
    for column in rolled_columns:
        subtotal = 0
        for idx, char in enumerate(column):
            subtotal += (len(column) - idx) * (char == 'O')
        total += subtotal

    print(total)

# Test
solve(example)

# Solve
solve(inputs)
