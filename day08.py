FILENAME = "inputs/day08.txt"


def decode(line):
    code = {}
    for digit in line:
        if len(digit) == 2:
            code[1] = sort_string(digit)
        elif len(digit) == 4:
            code[4] = sort_string(digit)
        elif len(digit) == 3:
            code[7] = sort_string(digit)
        elif len(digit) == 7:
            code[8] = sort_string(digit)
        elif (
            len(digit) == 6
            and len([d for d in digit if d in code[1]]) == 1
            and len([d for d in digit if d in code[4]]) == 3
        ):
            code[6] = sort_string(digit)

        elif (
            len(digit) == 6
            and len([d for d in digit if d in code[1]]) == 2
            and len([d for d in digit if d in code[4]]) == 3
        ):
            code[0] = sort_string(digit)
        elif len(digit) == 6 and len([d for d in digit if d in code[4]]) == 4:
            code[9] = sort_string(digit)
        elif len(digit) == 5 and len([d for d in digit if d in code[1]]) == 2:
            code[3] = sort_string(digit)
        elif len(digit) == 5 and len([d for d in digit if d in code[6]]) == 5:
            code[5] = sort_string(digit)
        elif len(digit) == 5 and len([d for d in digit if d in code[9]]) == 4:
            code[2] = sort_string(digit)
    return {value: key for key, value in code.items()}


def translate(output, code):
    num = 0
    for d in output:
        num += code[sort_string(d)]
        num *= 10
    return int(num / 10)


def basic(input):
    total = 0
    for line in input:
        output = line.split(" | ")[1].split()
        for digit in output:
            if len(digit) in [2, 4, 3, 7]:
                total += 1

    return total


def sort_string(s):
    return "".join(sorted(s))


def advanced(input):
    total = 0
    order_dict = {2: 0, 4: 0, 3: 0, 7: 0, 6: 1, 5: 5}
    for line in input:
        a, b = [i.split() for i in line.split(" | ")]
        code = decode(sorted(a, key=lambda x: order_dict[len(x)]))
        total += translate(b, code)

    return total


if __name__ == "__main__":
    with open(FILENAME) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]

    part1 = basic(lines)
    print("First part:", part1)

    part2 = advanced(lines)
    print("Second part:", part2)
