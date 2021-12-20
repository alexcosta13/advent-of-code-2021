FILENAME = "inputs/day19.txt"


def manhattan_distance(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))


def dist_point_to_points(points):
    return {
        p: {sum((x - y) ** 2 for x, y in zip(p, q)) for q in points} for p in points
    }


def rotations(scanner):
    result = [rotate_point(point) for point in scanner]
    return [list(row) for row in zip(*result)]


def rotate_point(point):
    a, b, c = point
    return [(+a, +b, +c), (+b, +c, +a), (+c, +a, +b), (+c, +b, -a), (+b, +a, -c), (+a, +c, -b),
            (+a, -b, -c), (+b, -c, -a), (+c, -a, -b), (+c, -b, +a), (+b, -a, +c), (+a, -c, +b),
            (-a, +b, -c), (-b, +c, -a), (-c, +a, -b), (-c, +b, +a), (-b, +a, +c), (-a, +c, +b),
            (-a, -b, +c), (-b, -c, +a), (-c, -a, +b), (-c, -b, -a), (-b, -a, -c), (-a, -c, -b)]


def move(scanner, offset):
    return [tuple(x - offset[i] for i, x in enumerate(point)) for point in scanner]


def scanners_overlap(scanner1, scanner2):
    scanner1 = dist_point_to_points(scanner1)
    scanner2 = dist_point_to_points(scanner2)
    for p, ps in scanner1.items():
        for q, qs in scanner2.items():
            if len(ps & qs) > 11:
                return p, q


def orient(base, scanner, points):
    p, q = points
    idx_q = scanner.index(q)
    base = move(base, p)
    moved_scanner = move(scanner, q)
    for i, rotation in enumerate(rotations(moved_scanner)):
        if len(set(base) & set(rotation)) > 11:
            return move(rotation, (-p[0], -p[1], -p[2])), (
                pi - qi for pi, qi in zip(p, rotations(scanner)[i][idx_q])
            )


def match_scanners(scanner1, scanner2):
    point = scanners_overlap(scanner1, scanner2)
    return orient(scanner1, scanner2, point)


def place_scanners(scanners, advanced=False):
    final_map = set(scanners.pop(0))
    locations = [(0, 0, 0)]
    while len(scanners) > 0:
        for scanner in scanners:
            if scanners_overlap(final_map, scanner):
                beacons, location = match_scanners(final_map, scanner)
                final_map |= set(beacons)
                scanners.remove(scanner)
                locations.append(location)

    return (
        max([manhattan_distance(a, b) for a in locations for b in locations])
        if advanced
        else len(final_map)
    )


if __name__ == "__main__":
    with open(FILENAME) as f:
        readings = f.read()

    scanners = [
        [tuple(map(int, beacon.split(","))) for beacon in scanner.split("\n")[1:]]
        for scanner in readings.split("\n\n")
    ]

    part1 = place_scanners(scanners)
    print("First part:", part1)

    scanners = [
        [tuple(map(int, beacon.split(","))) for beacon in scanner.split("\n")[1:]]
        for scanner in readings.split("\n\n")
    ]

    part2 = place_scanners(scanners, advanced=True)
    print("Second part:", part2)
