import math

FILENAME = "inputs/day18.txt"


def parse_input(string):
    result = []
    d = 0
    for s in string:
        if s == "[":
            d += 1
        elif s == "]":
            d -= 1
        elif s.isnumeric():
            result.append((int(s), d))
    return result


def explode(snailfish):
    for i in range(len(snailfish) - 1):
        left = snailfish[i]
        right = snailfish[i + 1]
        if 5 <= left[1] == right[1]:
            if i > 0:
                snailfish[i - 1] = (left[0] + snailfish[i - 1][0], snailfish[i - 1][1])
            if i < len(snailfish) - 2:
                snailfish[i + 2] = (right[0] + snailfish[i + 2][0], snailfish[i + 2][1])
            snailfish[i] = (0, left[1] - 1)
            del snailfish[i + 1]
            return True, snailfish
    return False, ""


def split(snailfish):
    for i, pair in enumerate(snailfish):
        if pair[0] >= 10:
            del snailfish[i]
            snailfish[i:i] = [
                (math.floor(pair[0] / 2), pair[1] + 1),
                (math.ceil(pair[0] / 2), pair[1] + 1),
            ]

            return True, snailfish

    return False, ""


def add(s1, s2):
    string = s1 + s2
    string = [(elem[0], elem[1] + 1) for elem in string]
    while True:
        ex, s = explode(string)
        if ex:
            string = s
        else:
            sp, s = split(string)
            if sp:
                string = s
            else:
                break
    return string


def magnitude(result):
    while len(result) > 1:
        for i in range(len(result) - 1):
            left = result[i]
            right = result[i + 1]
            if left[1] == right[1]:
                result[i] = (3 * left[0] + 2 * right[0], left[1] - 1)
                del result[i + 1]
                break
    return result[0][0]


def basic(input):
    result = parse_input(input[0])
    for i in input[1:]:
        result = add(result, parse_input(i))
    return magnitude(result)


def advanced(input):
    max_magnitude = 0
    for line1 in [parse_input(i) for i in input]:
        for line2 in [parse_input(i) for i in input]:
            if line1 != line2:
                max_magnitude = max(max_magnitude, magnitude(add(line1, line2)))
    return max_magnitude


if __name__ == "__main__":
    with open(FILENAME) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]

    part1 = basic(lines)
    print("First part:", part1)

    part2 = advanced(lines)
    print("Second part:", part2)
