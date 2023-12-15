# Advent of code, day 12

# Puzzle 1
from re import findall, sub
from itertools import combinations

with open('example.txt') as f:
    example = f.read()

with open('input12.txt') as f:
    inputs = f.read()

def parse_inputs(inputs):
    lines = inputs.rstrip().split('\n')[:10]
    records, templates = [], []
    for record in lines:
        gears, sizes = record.split()
        template = ['#' * int(size) for size in sizes.split(',')]
        record = sub(r'[.]+', '-', gears)

        records.append(record)
        templates.append(template)

    return zip(records, templates)

def get_perms(record, template):
    exc_count = 0
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
        if exc_count % 10_000_000 == 0:
            print(exc_count, combo)
        exc_count += 1
    return count

def solve(inputs):
    data = parse_inputs(inputs)
    total = 0
    for record, template in data:
        total += get_perms(record, template)
    print(total)

# Test
# solve(example)

# Solve
# solve(inputs)


# Puzzle 2

# ohgod

def parse_inputs_2(inputs):
    lines = inputs.rstrip().split('\n')[:10]
    records, templates = [], []
    for record in lines:
        gears, sizes = record.split()
        template = ['#' * int(size) for size in sizes.split(',')]
        template = template * 2
        gears = gears +'?'+ gears
        record = sub(r'[.]+', '-', gears)

        records.append(record)
        templates.append(template)

    print(records[0], templates[0])
    return zip(records, templates)


# First (failed) attempt at solving part 2. The idea was that there
# would be a constant multiplicative relationship between original
# inputs and N expansions. This assumption held true on the example
# set - by computing the 2x factor, I could extrapolate to 5x.
# This unfortunately did not hold true for the actual inputs.

def solve_2(inputs):
    totally_total = 0
    data1 = parse_inputs(inputs)
    data2 = parse_inputs_2(inputs)
    total1 = []
    total2 = []
    for record, template in data1:
        num_perms = get_perms(record, template)
        total1.append(num_perms)
    for record, template in data2:
        num_perms = get_perms(record, template)
        total2.append(num_perms)
    for one, two in zip(total1, total2):
        rel = two / one
        totally_total += one * rel**4
        print(one, two, rel)
    print(totally_total)

# Test
solve_2(example)

# Solve
solve_2(inputs)
