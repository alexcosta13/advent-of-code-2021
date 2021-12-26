FILENAME = "inputs/day25.txt"


def parse_input(lines):
    east, south = set(), set()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '>':
                east.add((i, j))
            elif c == 'v':
                south.add((i, j))

    return east, south


def move_east(east, south, max_east):
    new_east = set()
    for i, j in east:
        if (i, (j+1)%max_east) in east or (i, (j+1)%max_east) in south:
            new_east.add((i, j))
        else:
            new_east.add((i, (j+1)%max_east))
    return new_east


def move_south(east, south, max_south):
    new_south = set()
    for i, j in south:
        if ((i + 1)%max_south, j) in east or ((i + 1)%max_south, j) in south:
            new_south.add((i, j))
        else:
            new_south.add(((i + 1)%max_south, j))
    return new_south


def basic(input):
    rounds = 0
    east, south = parse_input(input)
    max_east = len(input[0])
    max_south = len(input)
    while True:
        new_east = move_east(east, south, max_east)
        new_south = move_south(new_east, south, max_south)
        rounds += 1
        if new_east == east and new_south == south:
            break
        else:
            east, south = new_east, new_south
    return rounds


if __name__ == "__main__":
    with open(FILENAME) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]

    part1 = basic(lines)
    print("First part:", part1)
