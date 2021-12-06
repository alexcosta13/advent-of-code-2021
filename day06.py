FILENAME = "inputs/day06.txt"


def basic(input, days=80):
    lantern_fish = input
    for _ in range(days):
        total = len(lantern_fish)
        for i in range(total):
            if lantern_fish[i] == 0:
                lantern_fish[i] = 6
                lantern_fish.append(8)
            else:
                lantern_fish[i] -= 1
    return len(lantern_fish)


def efficient_implementation(input, days=80):
    ages = [0 for _ in range(9)]
    for age in input:
        ages[age] += 1
    for d in range(days):
        new = ages.pop(0)
        ages.append(new)
        ages[6] += new
    return sum(ages)


if __name__ == "__main__":
    with open(FILENAME) as f:
        lines = f.read()
    lines = [int(x) for x in lines.split(",")]

    part1 = efficient_implementation(lines)
    print("First part:", part1)

    part2 = efficient_implementation(lines, 256)
    print("Second part:", part2)
