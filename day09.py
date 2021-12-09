FILENAME = "inputs/day09.txt"


def get_neighbors(i, matrix, n):
    top = int(matrix[i - n]) if i > n - 1 else 9
    bottom = int(matrix[i + n]) if i < len(matrix) - n else 9
    left = int(matrix[i - 1]) if i % n != 0 else 9
    right = int(matrix[i + 1]) if i % n != n - 1 else 9
    return top, bottom, left, right


def expand_basin(i, acc, matrix, n):
    top, bottom, left, right = get_neighbors(i, matrix, n)
    if top < 9 and i > n - 1 and i - n not in acc:
        acc.append(i - n)
        acc + expand_basin(i - n, acc, matrix, n)
    if bottom < 9 and i < len(matrix) - n and i + n not in acc:
        acc.append(i + n)
        expand_basin(i + n, acc, matrix, n)
    if left < 9 and i % n != 0 and i - 1 not in acc:
        acc.append(i - 1)
        expand_basin(i - 1, acc, matrix, n)
    if right < 9 and i % n != n - 1 and i + 1 not in acc:
        acc.append(i + 1)
        expand_basin(i + 1, acc, matrix, n)

    return acc


def get_low_points_position(matrix, n):
    positions = []
    for i in range(len(matrix)):
        point = int(matrix[i])
        top, bottom, left, right = get_neighbors(i, matrix, n)
        if point < top and point < bottom and point < left and point < right:
            positions.append(i)
    return positions


def basic(matrix, n):
    low_points = 0
    for position in get_low_points_position(matrix, n):
        low_points += int(matrix[position]) + 1

    return low_points


def advanced(matrix, n):
    low_points = get_low_points_position(matrix, n)
    basins = [expand_basin(point, [point], matrix, n) for point in low_points]
    basins = sorted(basins, key=lambda x: len(x))[-3:]
    total = 1
    for b in basins:
        total *= len(b)
    return total


if __name__ == "__main__":
    with open(FILENAME) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]

    n = len(lines[0])
    matrix = ""
    for line in lines:
        matrix += line

    part1 = basic(matrix, n)
    print("First part:", part1)

    part2 = advanced(matrix, n)
    print("Second part:", part2)
