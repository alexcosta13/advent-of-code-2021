FILENAME = "inputs/day03.txt"


def basic(input):
    common = [0 for _ in range(len(input[0]))]
    for line in input:
        for pos, bit in enumerate(line):
            common[pos] += int(bit)
    common = [1 if i > len(input) / 2 else 0 for i in common]
    gamma, epsilon = 0, 0
    for pos, bit in enumerate(common[::-1]):
        if bit:
            gamma += 2 ** pos
        else:
            epsilon += 2 ** pos
    return gamma * epsilon


def life_support_rating(input, criteria=1):
    value = input
    for i in range(len(input[0])):
        value_count = 0
        for line in value:
            value_count += int(line[i])
        most_common_value = criteria if value_count >= len(value) / 2 else not criteria
        value = [r for r in value if int(r[i]) == most_common_value]
        if len(value) == 1:
            break
    return value[0]


def advanced(input):
    oxygen_generator = life_support_rating(input, 1)
    CO2_scrubber = life_support_rating(input, 0)

    return int(oxygen_generator, 2) * int(CO2_scrubber, 2)


if __name__ == "__main__":
    with open(FILENAME) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]

    part1 = basic(lines)
    print("First part:", part1)

    part2 = advanced(lines)
    print("Second part:", part2)
