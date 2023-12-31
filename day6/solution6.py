# Advent of code, day 6

# Puzzle 1

with open('example.txt') as f:
    example = f.read()

with open('input6.txt') as f:
    inputs = f.read()


print(example)
print('\n\n\n\n\n')
print(inputs)

def parse_inputs(raw_inputs):
    times = raw_inputs.split('\n')[0].split(':')[1].split()
    distances = raw_inputs.split('\n')[1].split(':')[1].split()

    times = [int(time) for time in times]
    distances = [int(dist) for dist in distances]

    return zip(times, distances)


def calculate_min_distance(time, dist):
    n = x = 0

    while n <= dist:
        x += 1
        n = x * (time - x)

    return x


def solve(inputs):
    from math import ceil

    inputs = parse_inputs(inputs)
    margin = 1

    for time, dist in inputs:
        min_ = calculate_min_distance(time, dist)
        ways = 2 * (ceil(time / 2) - min_)
        if time % 2 == 0:
            ways += 1
        margin *= ways

    print(margin)

# Test
solve(example)

# Solve
solve(inputs)


# Puzzle 2

def parse_inputs_2(raw_inputs):
    times = raw_inputs.split('\n')[0].split(':')[1].split()
    distances = raw_inputs.split('\n')[1].split(':')[1].split()

    return int(''.join(times)), int(''.join(distances))

def solve_2(inputs):
    from math import ceil

    time, distance = parse_inputs_2(inputs)

    # These functions use variables from the enclosing scope
    def f(t):
        return t * (time - t)

    def bisect(l, r):
        if r - l == 1:
            return r
        mid = (l+r) // 2
        diff =  f(mid) - distance
        if diff > 0:
            return bisect(l, mid)
        else:
            return bisect(mid, r)

    # Find the min and get the answer
    min_ = bisect(0, time//2)
    ways = 2 * (ceil(time / 2) - min_)
    if time % 2 == 0:
        ways += 1

    print(ways)

# Test
solve_2(example)

# Solve
solve_2(inputs)
