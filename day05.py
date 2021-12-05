FILENAME = "inputs/day05.txt"


def get_points(vent, advanced=False):
    x1, y1, x2, y2 = vent
    if x1 == x2:
        return [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
    elif y1 == y2:
        return [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]
    elif x1 > x2 and y1 > y2 or x1 < x2 and y1 < y2:
        return (
            [
                (x, y)
                for x, y in zip(
                    range(min(x1, x2), max(x1, x2) + 1),
                    range(min(y1, y2), max(y1, y2) + 1),
                )
            ]
            if advanced
            else []
        )
    elif x1 > x2 and y1 < y2:
        return (
            [(x, y) for x, y in zip(range(x1, x2 - 1, -1), range(y1, y2 + 1))]
            if advanced
            else []
        )
    elif x1 < x2 and y1 > y2:
        return (
            [(x, y) for x, y in zip(range(x1, x2 + 1), range(y1, y2 - 1, -1))]
            if advanced
            else []
        )
    else:
        return []


def overlapping(vents, advanced=False):
    points = {}
    for vent in vents:
        for point in get_points(vent, advanced):
            points[point] = points.get(point, 0) + 1
    return len([key for key, value in points.items() if value > 1])


if __name__ == "__main__":
    with open(FILENAME) as f:
        lines = f.readlines()

    vents = [tuple(map(int, (line.replace(" -> ", ",").split(",")))) for line in lines]

    part1 = overlapping(vents)
    print("First part:", part1)

    part2 = overlapping(vents, advanced=True)
    print("Second part:", part2)
