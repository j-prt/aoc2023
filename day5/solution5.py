# Advent of code, day 5

# Puzzle 1

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
# with open('example.txt') as f:
#     example = f.read()
# solve(example)

# Solution
# with open('input5.txt') as f:
#     inputs = f.read()
# solve(inputs)


# Puzzle 2
#
# AKA
#
# 'Waiting is Eaiser Than Thinking'
#               or
# 'Multiprocessing isn't THAT Hard'

from multiprocessing import Process, SimpleQueue, cpu_count

def worker(jobs, results):
    while data := jobs.get():
        seed_range, mappings = data
        min_seed = float('inf')
        for seed in seed_range:
            for mapping in mappings:
                seed = map_resolver(seed, mapping)
            min_seed = seed if seed < min_seed else min_seed
        print('Worker finished one')
        results.put(min_seed)
    results.put(0)

def start_jobs(seeds, mappings, procs, jobs, results):
    for seed_range in seeds:
        jobs.put((seed_range, mappings))
    for _ in range(procs):
        proc = Process(target=worker, args=(jobs, results))
        proc.start()
        jobs.put(0)

def report(procs, results):
    procs_done = 0
    min_val = float('inf')
    while procs_done < procs:
        val = results.get()
        if val == 0:
            procs_done += 1
        else:
            print('report val:', val)
            if val < min_val:
                min_val = val
    return min_val

def solve_mp(inputs):
    procs = cpu_count()
    jobs = SimpleQueue()
    results = SimpleQueue()

    seeds, mappings = split_sections(inputs)
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_range = range(seeds[i], seeds[i]+seeds[i+1])
        seed_ranges.append(seed_range)

    start_jobs(seed_ranges, mappings, procs, jobs, results)

    val = report(procs, results)
    print(val)

if __name__ == '__main__':
    with open('input5.txt') as f:
        inputs = f.read()
    solve_mp(inputs)
