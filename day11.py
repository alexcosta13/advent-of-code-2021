FILENAME = "inputs/day11.txt"


def all_zeroes(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                return False
    return True


def count_flashes(matrix):
    flashes = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > 9:
                flashes += 1
                matrix[i][j] = 0
    return flashes


def get_neighbors(i, j, matrix):
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x != 0 or y != 0:
                try:
                    neighbor = matrix[i + x][j + y]
                    if neighbor < 10 and i + x > -1 and j + y > -1:
                        yield i + x, j + y
                except:
                    pass


def step(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] += 1

    flag = True
    while flag:
        flag = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 10:
                    matrix[i][j] += 1
                    neighbors = list(get_neighbors(i, j, matrix))
                    for x, y in neighbors:
                        matrix[x][y] += 1
                        flag = True

    return count_flashes(matrix)


def basic(input, steps=100):
    flashes = 0
    for _ in range(steps):
        flashes += step(input)
    return flashes


def advanced(input):
    counter = 0
    while not all_zeroes(input):
        step(input)
        counter += 1
    return counter


if __name__ == "__main__":
    with open(FILENAME) as f:
        lines = f.readlines()

    input1 = [list(map(int, line.strip())) for line in lines]
    input2 = [row[:] for row in input1]

    part1 = basic(input1)
    print("First part:", part1)

    part2 = advanced(input2)
    print("Second part:", part2)
