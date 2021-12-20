FILENAME = "inputs/day20.txt"


def neighbors(x, y):
    return [(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2)]


def get_number(x, y, image):
    string = ""
    for n in neighbors(x, y):
        if n in image:
            string += "1"
        else:
            string += "0"
    return int(string, 2)


def transform_image(image, algorithm, filter_border):
    new_image = set()
    for i in range(-55, 200):
        for j in range(-55, 200):
            if algorithm[get_number(i, j, image)] == "#":
                new_image.add((i, j))
    if filter_border:
        new_image = {
            i
            for i in new_image
            if i[0] != 199 and i[1] != 199 and i[0] != -55 and i[1] != -55
        }
    return new_image


def solve(input, transformations=2):
    algorithm = input[0]
    image = set()
    for i, line in enumerate(input[2:]):
        for j, elem in enumerate(line):
            if elem == "#":
                image.add((i, j))

    for i in range(transformations):
        image = transform_image(image, algorithm, i % 2)

    return len(image)


if __name__ == "__main__":
    with open(FILENAME) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]

    part1 = solve(lines, 2)
    print("First part:", part1)

    part2 = solve(lines, 50)
    print("Second part:", part2)
