# Advent of code, day 5

# Puzzle 1

with open('example.txt') as f:
    example = f.read()

def split_sections(inputs):
    split = inputs.split('\n\n')

    seeds = split[0].split(':')[1].split()
    seeds = [int(seed) for seed in seeds]

    mappings = [mapping.split(':')[1].strip().split('\n')
                for mapping in split[1:]]
    clean_mappings = []
    for mapping in mappings:
        maps = []
        for map_triplet in mapping:
            map_triplet = [int(val) for val in map_triplet.split()]
            maps.append(map_triplet)
        clean_mappings.append(maps)

    return seeds, clean_mappings

def map_resolver(seed, mapping):
    for map_ in mapping:
        if map_[1] <= seed < map_[1] + map_[2]:
            diff = map_[0] - map_[1]
            return seed + diff
    # If the seed falls outside the range, return itself
    return seed

def solve(inputs):
    min_seed = float('inf')
    seeds, mappings = split_sections(inputs)
    for seed in seeds:
        for mapping in mappings:
            seed = map_resolver(seed, mapping)
        min_seed = seed if seed < min_seed else min_seed

    print(min_seed)

# Test
solve(example)

with open('input5.txt') as f:
    inputs = f.read()

# Solution
solve(inputs)
