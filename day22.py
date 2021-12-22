import re

FILENAME = "inputs/day22.txt"


class Cube:
    def __init__(self, x0, x1, y0, y1, z0, z1):
        self.x0, self.x1, self.y0, self.y1, self.z0, self.z1 = x0, x1, y0, y1, z0, z1
        self.off = []

    def get_intersection(self, other):
        x0, x1 = max(self.x0, other.x0), min(self.x1, other.x1)
        y0, y1 = max(self.y0, other.y0), min(self.y1, other.y1)
        z0, z1 = max(self.z0, other.z0), min(self.z1, other.z1)
        if x0 <= x1 and y0 <= y1 and z0 <= z1:
            return Cube(x0, x1, y0, y1, z0, z1)
        return None

    def remove(self, other):
        if c := self.get_intersection(other):
            for o in self.off:
                o.remove(other)
            self.off.append(c)

    def volume(self):
        return (self.x1 - self.x0 + 1) * (self.y1 - self.y0 + 1) * (
            self.z1 - self.z0 + 1
        ) - sum([o.volume() for o in self.off])


def parse_line(line):
    turn_on = line.split()[0] == "on"
    return turn_on, list(map(int, re.findall("-?\d+", line.split()[1])))


def get_cube(cube):
    x0, x1, y0, y1, z0, z1 = cube
    return {
        (i, j, k)
        for i in range(x0, x1 + 1)
        for j in range(y0, y1 + 1)
        for k in range(z0, z1 + 1)
    }


def basic(input):
    cube = set()
    for instruction in [parse_line(line) for line in input[:20]]:
        if instruction[0]:
            cube |= get_cube(instruction[1])
        else:
            cube -= get_cube(instruction[1])
    return len(cube)


def advanced(input):
    cubes = []
    for on, cube in [parse_line(line) for line in input]:
        cube = Cube(*cube)
        for c in cubes:
            c.remove(cube)
        if on:
            cubes.append(cube)
    return sum([c.volume() for c in cubes])


if __name__ == "__main__":
    with open(FILENAME) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]

    part1 = basic(lines)
    print("First part:", part1)

    part2 = advanced(lines)
    print("Second part:", part2)
