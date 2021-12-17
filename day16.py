import math

FILENAME = "inputs/day16.txt"


def sum_version_numbers(content, total=0):
    initial_total = total
    if content["type"] == 4:
        return content["version"]
    else:
        for elem in content["content"]:
            total += sum_version_numbers(elem, initial_total)
        return content["version"] + total


def calculate_operation(content):
    if content["type"] == 0:
        return sum([calculate_operation(c) for c in content["content"]])
    elif content["type"] == 1:
        return math.prod([calculate_operation(c) for c in content["content"]])
    elif content["type"] == 2:
        return min([calculate_operation(c) for c in content["content"]])
    elif content["type"] == 3:
        return max([calculate_operation(c) for c in content["content"]])
    elif content["type"] == 4:
        return content["content"]
    elif content["type"] == 5:
        return calculate_operation(content["content"][0]) > calculate_operation(content["content"][1])
    elif content["type"] == 6:
        return calculate_operation(content["content"][0]) < calculate_operation(content["content"][1])
    elif content["type"] == 7:
        return calculate_operation(content["content"][0]) == calculate_operation(content["content"][1])


def parse_packet(binary_string):
    first_bit = 0
    version = int(binary_string[first_bit : first_bit + 3], 2)
    packet_type = int(binary_string[first_bit + 3 : first_bit + 6], 2)
    first_bit += 6
    if packet_type == 4:
        number = ""
        while True:
            number += binary_string[first_bit + 1 : first_bit + 5]
            if binary_string[first_bit] == "0":
                break
            first_bit += 5
        first_bit += 5
        content = int(number, 2)
        binary_string = binary_string[first_bit:]
    else:
        length_type = binary_string[first_bit]
        first_bit += 1
        if length_type == "0":
            length = int(binary_string[first_bit : first_bit + 15], 2)
            first_bit += 15
            binary_string = binary_string[first_bit:]
            sub_string = binary_string[0:length]
            content = []
            while len(sub_string):
                c, sub_string = parse_packet(sub_string)
                content.append(c)
            binary_string = binary_string[length:]
        else:
            num_packets = int(binary_string[first_bit : first_bit + 11], 2)
            first_bit += 11
            binary_string = binary_string[first_bit:]
            content = []
            for _ in range(num_packets):
                c, binary_string = parse_packet(binary_string)
                content.append(c)

    return {"version": version, "type": packet_type, "content": content}, binary_string


def basic(input):
    binary_string = str(bin(int(input, 16)))[2:]
    pad = "0" * ((4 - len(binary_string)) % 4)
    binary_string = pad + binary_string
    content, _ = parse_packet(binary_string)
    return sum_version_numbers(content)


def advanced(input):
    binary_string = str(bin(int(input, 16)))[2:]
    pad = "0" * ((4 - len(binary_string)) % 4)
    binary_string = pad + binary_string
    content, _ = parse_packet(binary_string)
    return calculate_operation(content)


if __name__ == "__main__":
    with open(FILENAME) as f:
        lines = f.read()

    part1 = basic(lines)
    print("First part:", part1)

    part2 = advanced(lines)
    print("Second part:", part2)
