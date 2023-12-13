# Advent of code, day 11

# Puzzle 1
from re import findall, sub
from itertools import combinations, permutations

with open('example.txt') as f:
    example = f.read()

with open('input12.txt') as f:
    inputs = f.read()

# def parse_inputs(inputs):
#     lines = inputs.rstrip().split('\n')
#     all_gears, all_sizes = [], []
#     for record in lines:
#         gear, sizes = record.split()
#         sizes = [int(size) for size in sizes.split(',')]
#         unknowns = list(finditer(r'[?]+', gear))
#         knowns = list(finditer(r'[#]+', gear))

def parse_inputs(inputs):
    lines = inputs.rstrip().split('\n')
    records, templates = [], []
    for record in lines:
        gears, sizes = record.split()
        template = ['#' * int(size) for size in sizes.split(',')]
        record = sub(r'[.]+', '-', gears)

        records.append(record)
        templates.append(template)

    return zip(records, templates)

def get_perms(record, template):
    count = 0
    base_len = sum(len(item) for item in template)
    record_len = len(record)
    base_str = ['#'] * record_len
    dash_locs = {idx for idx, val in enumerate(record) if val == '-'}
    hash_locs = {idx for idx, val in enumerate(record) if val == '#'}
    dashes_to_add = record_len - base_len - len(dash_locs)
    for loc in dash_locs:
        base_str[loc] = '-'

    # The logic: list all possible indexes that can contain damaged parts,
    # subtract the indexes with known parts or known working parts, and use
    # the remaining indexes to build all possible arrangements. Compare to
    # the template, and if the template matches, increment the counter by 1.

    possible_locs = set(range(record_len)).difference(dash_locs).difference(hash_locs)
    for combo in combinations(possible_locs, dashes_to_add):
        current = base_str[:]
        for idx in combo:
            current[idx] = '-'
        if findall('[#]+', ''.join(current)) == template:
            count += 1
    return count

def solve(inputs):
    data = parse_inputs(inputs)
    total = 0
    for record, template in data:
        total += get_perms(record, template)
    print(total)

# Test
solve(example)

# Solve
solve(inputs)
