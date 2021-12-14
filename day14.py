from collections import Counter

FILENAME = "inputs/day14.txt"


def parse_input_sequence(lines):
    sequence = lines[0].strip()
    rules = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in lines[2:]}
    return sequence, rules


def parse_input_pairs(lines):
    pairs = Counter(
        [lines[0][i] + lines[0][i + 1] for i in range(len(lines[0].strip()) - 1)]
    )
    rules = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in lines[2:]}
    return pairs, rules


def insert_sequence(seq, rules):
    new_seq = seq[0]
    for i in range(len(seq) - 1):
        new = rules[seq[i] + seq[i + 1]]
        new_seq += new + seq[i + 1]
    return new_seq


def insert_pairs(pairs, count, rules):
    new_pairs = {}
    for pair in pairs:
        a, b = pair
        new = rules[pair]
        new_pairs[a + new] = new_pairs.get(a + new, 0) + pairs[a + b]
        new_pairs[new + b] = new_pairs.get(new + b, 0) + pairs[a + b]
        count[new] = count.get(new, 0) + pairs[a + b]
    return new_pairs, count


def basic(input, iterations=10):
    sequence, rules = parse_input_sequence(input)
    for _ in range(iterations):
        sequence = insert_sequence(sequence, rules)
    sorted_count = sorted(Counter(sequence).values())
    return sorted_count[-1] - sorted_count[0]


def advanced(input, iterations=40):
    pairs, rules = parse_input_pairs(input)
    count = {}
    for i in input[0]:
        count[i] = count.get(i, 0) + 1
    for _ in range(iterations):
        pairs, count = insert_pairs(pairs, count, rules)
    sorted_count = sorted(count.values())
    return sorted_count[-1] - sorted_count[0]


if __name__ == "__main__":
    with open(FILENAME) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]

    part1 = basic(lines)
    print("First part:", part1)

    part2 = advanced(lines)
    print("Second part:", part2)
