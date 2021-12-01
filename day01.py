FILENAME = "inputs/day01.txt"


def basic(input):
    counter = 0
    for i in range(len(input) - 1):
        if input[i] < input[i + 1]:
            counter += 1
    return counter


def advanced(input):
    counter = 0
    for i in range(len(input) - 3):
        if sum(input[i : i + 3]) < sum(input[i + 1 : i + 4]):
            counter += 1
    return counter


if __name__ == "__main__":
    with open(FILENAME) as f:
        lines = f.readlines()
    lines = [int(x.strip()) for x in lines]

    part1 = basic(lines)
    print("First part:", part1)

    part2 = advanced(lines)
    print("Second part:", part2)
