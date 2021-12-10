from statistics import median


FILENAME = "inputs/day10.txt"


def get_first_incorrect_character(line):
    match = {")": "(", "]": "[", "}": "{", ">": "<"}
    stack = []
    for c in line:
        if c in "<([{":
            stack.append(c)
        elif match[c] != stack.pop():
            return c
    return None


def closing_sequence(line):
    match = {"(": ")", "[": "]", "{": "}", "<": ">"}
    stack = []
    for c in line:
        if c in "<([{":
            stack.append(c)
        elif c != match[stack.pop()]:
            return []
    closing = []
    for s in stack[::-1]:
        closing.append(match[s])
    return closing


def get_score(s):
    score = 0
    values = {")": 1, "]": 2, "}": 3, ">": 4}
    for c in s:
        score *= 5
        score += values[c]
    return score


def basic(input):
    total = 0
    values = {")": 3, "]": 57, "}": 1197, ">": 25137}
    for line in input:
        c = get_first_incorrect_character(line)
        if c is not None:
            total += values[c]
    return total


def advanced(input):
    seq = [closing_sequence(line) for line in input]
    seq = [s for s in seq if len(s) > 0]
    scores = [get_score(s) for s in seq]
    return int(median(scores))


if __name__ == "__main__":
    with open(FILENAME) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]

    part1 = basic(lines)
    print("First part:", part1)

    part2 = advanced(lines)
    print("Second part:", part2)
