FILENAME = "inputs/day02.txt"


def basic(input):
    horizontal = 0
    depth = 0
    for command in input:
        direction, value = command.split(" ")
        value = int(value)
        if direction == "forward":
            horizontal += value
        elif direction == "down":
            depth += value
        elif direction == "up":
            depth -= value
    return horizontal * depth


def advanced(input):
    position, aim, depth = 0, 0, 0
    for command in input:
        direction, value = command.split(" ")
        value = int(value)
        if direction == "forward":
            position += value
            depth += aim * value
        elif direction == "down":
            aim += value
        elif direction == "up":
            aim -= value
    return position * depth


if __name__ == "__main__":
    with open(FILENAME) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]

    part1 = basic(lines)
    print("First part:", part1)

    part2 = advanced(lines)
    print("Second part:", part2)
