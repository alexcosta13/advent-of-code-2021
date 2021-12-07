from statistics import median, mean

FILENAME = "inputs/day07.txt"


def calculate_fuel(distance):
    return sum(range(distance + 1))


def basic(input):
    m = int(median(input))
    distance = [abs(x - m) for x in input]
    return sum(distance)


def advanced(input):
    m = int(mean(input))
    fuel1 = [calculate_fuel(abs(x - m)) for x in input]
    fuel2 = [calculate_fuel(abs(x - (m + 1))) for x in input]
    print(sum(fuel1), sum(fuel2))
    return min(sum(fuel1), sum(fuel2))


if __name__ == "__main__":
    with open(FILENAME) as f:
        lines = f.read()
    lines = [int(x) for x in lines.split(",")]

    part1 = basic(lines)
    print("First part:", part1)

    part2 = advanced(lines)
    print("Second part:", part2)
