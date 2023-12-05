# Advent of code, day 3, puzzle 1

import re
from dataclasses import dataclass, field

example = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


# Simple helper classes for storing line data

@dataclass(frozen=True)
class Part:
    loc: frozenset = None
    val: str = None

@dataclass
class Line:
    nums: list[Part] = field(default_factory=list)
    symbols: list[Part] = field(default_factory=list)

    # Added this while working on part 2
    def __add__(self, other):
        sum_nums = self.nums + other.nums
        sum_symbols = self.symbols + other.symbols
        return self.__class__(sum_nums, sum_symbols)


# Functions for parsing and scoring

def build_part(match):
    loc = frozenset(range(match.start(), match.end()+1)) # Catch diagonals
    val = match.group()
    return Part(loc=loc, val=val)

def parse_line(line):
    nums = []
    symbols = []
    for match in re.finditer(r'[^\d.]', line):
        symbols.append(build_part(match))
    for match in re.finditer(r'\d+', line):
        nums.append(build_part(match))
    return Line(nums=nums, symbols=symbols)

def score(parts_list, parsed_line):
    sub_total = 0
    for num in parsed_line.nums:
        if num in parts_list:
            continue
        if any(num.loc.intersection(s.loc) for s in parsed_line.symbols):
            sub_total += int(num.val)
            parts_list.add(num)

    return sub_total

def test():
    total = 0
    parts_list = set()
    inputs = example.split()
    prev_line = parse_line(inputs[0])
    for line in inputs[1:]:
        cur_line = parse_line(line)
        prev_line.symbols.extend(cur_line.symbols)
        prev_line.nums.extend(cur_line.nums)
        total += score(parts_list, prev_line)
        prev_line = cur_line
    total += score(parts_list, prev_line)

    print(total)

# test()

def solve_part_1():
    with open('input3.txt', 'r', encoding='utf-8') as f:
        inputs = f.readlines()

    total = 0
    parts_list = set()
    prev_line = parse_line(inputs[0])
    for line in inputs[1:]:
        cur_line = parse_line(line.strip())
        prev_line.symbols.extend(cur_line.symbols)
        prev_line.nums.extend(cur_line.nums)
        total += score(parts_list, prev_line)
        prev_line = cur_line
    total += score(parts_list, prev_line)

    print(total)

# solve_part_1()


# Puzzle 2
from operator import mul
from functools import reduce

def score_gears(left, center, right):
    triplet = left + center + right
    sub_total = 0
    for part in center.symbols:
        if part.val == '*':
            neighbors = []
            for num in triplet.nums:
                if num.loc.intersection(part.loc):
                    neighbors.append(int(num.val))
            if len(neighbors) > 1:
                sub_total += reduce(mul, neighbors)

    return sub_total

def test():
    total = 0
    inputs = example.split()
    prev_one = parse_line(inputs[0])
    prev_two = Line()
    for line in inputs[1:]:
        current = parse_line(line)

        total += score_gears(prev_two, prev_one, current)
        # Prep for the next loop
        prev_two = prev_one
        prev_one = current

    current = Line()
    total += score_gears(prev_two, prev_one, current)

    print(total)

# test()

def solve_part_2():
    with open('input3.txt', 'r', encoding='utf-8') as f:
        inputs = f.readlines()

    total = 0
    prev_one = parse_line(inputs[0])
    prev_two = Line()
    for line in inputs[1:]:
        current = parse_line(line)
        total += score_gears(prev_two, prev_one, current)
        # Prep for the next loop
        prev_two = prev_one
        prev_one = current

    current = Line()
    total += score_gears(prev_two, prev_one, current)

    print(total)

solve_part_2()
