FILENAME = "inputs/day13.txt"


def fold_x(dots, x):
    result = {d for d in dots}
    for dot in dots:
        if dot[0] > x:
            result -= {dot}
            result |= {(dot[0] - 2 * (dot[0] - x), dot[1])}
    return result


def fold_y(dots, y):
    result = {d for d in dots}
    for dot in dots:
        if dot[1] > y:
            result -= {dot}
            result |= {(dot[0], dot[1] - 2 * (dot[1] - y))}
    return result


def fold(dots, instruction):
    if instruction[0] == "x":
        return fold_x(dots, instruction[1])
    else:
        return fold_y(dots, instruction[1])


def print_matrix(dots):
    string = "\n"
    min_coordinate = min(min(dots))
    dots = {(x - min_coordinate, y - min_coordinate) for x, y in dots}
    for i in range(6):
        for j in range(8 * 5):
            if j % 5 == 4:
                string += "\t\t"
            elif (j, i) in dots:
                string += "#"
            else:
                string += " "
        string += "\n"

    return string


def parse_input(lines):
    dots, instructions = lines.split("\n\n")
    dots = {(int(d.split(",")[0]), int(d.split(",")[1])) for d in dots.split("\n")}
    instructions = [
        tuple(instruction.split()[-1].split("="))
        for instruction in instructions.split("\n")
    ]
    instructions = [(a, int(b)) for a, b in instructions]
    return dots, instructions


def basic(dots, instructions):
    dots = fold(dots, instructions[0])
    return len(dots)


def advanced(dots, instructions):
    for i in instructions:
        dots = fold(dots, i)
    return print_matrix(dots)


if __name__ == "__main__":
    with open(FILENAME) as f:
        lines = f.read()

    dots, instructions = parse_input(lines)

    part1 = basic(dots, instructions)
    print("First part:", part1)

    part2 = advanced(dots, instructions)
    print("Second part:", part2)
