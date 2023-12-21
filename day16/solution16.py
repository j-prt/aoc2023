# Advent of code, day 16

# Puzzle 1

from dataclasses import dataclass, field
from enum import Enum
from typing import ClassVar

with open('example.txt') as f:
    example = f.read()

with open('input16.txt') as f:
    inputs = f.read()


class Compass(Enum):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3

@dataclass
class Beam:
    x: int = 0
    y: int = 0
    direction: Compass = Compass.EAST

    # Bit of a hack here: all instances of Beam share a
    # single set for their history attribute. This is why
    # Beam.history has to be reset after each run of solve.
    history: ClassVar[set[tuple[int, int, Compass]]] = set()


    def step(self):
        if self.direction == Compass.EAST:
            self.x += 1
        if self.direction == Compass.SOUTH:
            self.y += 1
        if self.direction == Compass.WEST:
            if self.x == 0:
                raise IndexError
            self.x -= 1
        if self.direction == Compass.NORTH:
            if self.y == 0:
                raise IndexError
            self.y -= 1



    def split(self, symbol):
        if symbol == '|':
            self.direction = Compass.NORTH
            return self, Beam(x=self.x, y=self.y,
                              direction=Compass.SOUTH)
        else:
            self.direction = Compass.EAST
            return self, Beam(x=self.x, y=self.y,
                              direction=Compass.WEST)

    def look(self, symbol):
        pos = (self.x, self.y, self.direction)
        if pos in self.history:
            raise IndexError

        self.history.add(pos)

        if symbol == '\\':
            if self.direction == Compass.EAST:
                self.direction = Compass.SOUTH
            elif self.direction == Compass.SOUTH:
                self.direction = Compass.EAST
            elif self.direction == Compass.WEST:
                self.direction = Compass.NORTH
            elif self.direction == Compass.NORTH:
                self.direction = Compass.WEST
        if symbol == '/':
            if self.direction == Compass.EAST:
                self.direction = Compass.NORTH
            elif self.direction == Compass.SOUTH:
                self.direction = Compass.WEST
            elif self.direction == Compass.WEST:
                self.direction = Compass.SOUTH
            elif self.direction == Compass.NORTH:
                self.direction = Compass.EAST
        if symbol == '|':
            if self.direction == Compass.EAST or \
                self.direction == Compass.WEST:
                return self.split(symbol)
        if symbol == '-':
            if self.direction == Compass.SOUTH or \
                self.direction == Compass.NORTH:
                return self.split(symbol)
        return self, None


def parse_inputs(inputs):
    inputs = inputs.rstrip().split('\n')
    list_of_lists = [list(row) for row in inputs]
    return list_of_lists

def solve(inputs):
    contraption = parse_inputs(inputs)

    beams = [Beam()]
    finished = []
    while beams:
        beam = beams.pop()

        while True:
            try:
                try:
                    symbol = contraption[beam.y][beam.x]
                except:
                    raise IndexError
                beam, other = beam.look(symbol)
                if other:
                    beams.append(other)
                beam.step()
            except IndexError:

                finished.append(beam)
                break

    locations = set()
    for beam in finished:
        hist = [(h[0], h[1]) for h in beam.history]
        locations.update(hist)
    print(len(locations))
    Beam.history = set()

# Test
solve(example)

# Solve
solve(inputs)


# Puzzle 2

# Brute force works here too
def score(x, y, dir, contraption):
    beams = [Beam(x=x, y=y, direction=dir)]
    finished = []
    while beams:
        beam = beams.pop()

        while True:
            try:
                try:
                    symbol = contraption[beam.y][beam.x]
                except:
                    raise IndexError
                beam, other = beam.look(symbol)
                if other:
                    beams.append(other)
                beam.step()
            except IndexError:

                finished.append(beam)
                break

    locations = set()
    for beam in finished:
        hist = [(h[0], h[1]) for h in beam.history]
        locations.update(hist)
    Beam.history = set()
    return len(locations)

def solve_2(inputs):
    contraption = parse_inputs(inputs)
    x_limit = len(contraption[0])
    y_limit = len(contraption)
    max_val = 0

    # HORIZONTAL
    for y in range(y_limit):
        val = max(score(0, y, Compass.EAST, contraption),
                    score(x_limit-1, y, Compass.WEST, contraption))
        if val > max_val:
            max_val = val

    # VERTICAL
    for x in range(x_limit):
        val = max(score(x, 0, Compass.SOUTH, contraption),
                    score(x, y_limit-1, Compass.NORTH, contraption))
        if val > max_val:
            max_val = val

    print(max_val)

# Test
solve_2(example)

# Solve
solve_2(inputs)
