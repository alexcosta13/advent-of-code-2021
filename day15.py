import math
from heapdict import heapdict

FILENAME = "inputs/day15.txt"


def get_minimum_path(x, y, max, matrix, results):
    if (x, y) in results:
        return results[(x, y)]

    if x > max or y > max or x < 0 or y < 0:
        return math.inf

    if x == max and y == max:
        return matrix[max][max]

    value = matrix[x][y] + min(
        get_minimum_path(x + 1, y, max, matrix, results),
        get_minimum_path(x, y + 1, max, matrix, results),
    )
    results[(x, y)] = value

    return value


def create_full_map(matrix):
    new_matrix = [[0 for _ in range(len(matrix) * 5)] for _ in range(len(matrix) * 5)]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(5):
                new_matrix[i][j + k * len(matrix)] = ((matrix[i][j] + k - 1) % 9) + 1

    for i in range(len(matrix)):
        for j in range(len(new_matrix)):
            for k in range(5):
                new_matrix[i + k * len(matrix)][j] = (
                    (new_matrix[i][j] + k - 1) % 9
                ) + 1
    return new_matrix


def get_neighbors(x, y, maximum):
    return [
        (x + i, y + j)
        for i in range(-1, 2)
        for j in range(-1, 2)
        if 0 <= x + i < maximum
        and 0 <= y + j < maximum
        and (i == 0 or j == 0)
        and (i != 0 or j != 0)
    ]


def dijkstra_algorithm(matrix):
    shortest_path = {(0, 0): 0}
    visited = {(0, 0)}
    queue = heapdict()
    queue[(0, 0)] = 0
    while len(queue) > 0:
        spot, _ = queue.popitem()
        visited.add(spot)
        neighbors = get_neighbors(*spot, len(matrix))
        for neighbor in neighbors:
            if neighbor not in visited:
                new_distance = shortest_path[spot] + matrix[neighbor[0]][neighbor[1]]
                current_distance = shortest_path.get(neighbor, math.inf)
                if new_distance < current_distance:
                    queue[neighbor] = new_distance
                    shortest_path[neighbor] = new_distance

    return shortest_path[len(matrix) - 1, len(matrix) - 1]


def basic(input):
    return get_minimum_path(0, 0, len(input) - 1, input, {}) - input[0][0]


def advanced(input):
    matrix = create_full_map(input)
    return dijkstra_algorithm(matrix)


if __name__ == "__main__":
    with open(FILENAME) as f:
        lines = f.readlines()
    lines = [list(map(int, (line.strip()))) for line in lines]

    part1 = basic(lines)
    print("First part:", part1)

    part2 = advanced(lines)
    print("Second part:", part2)
