def probe_reaches_target(x0, y0, target):
    x, y = x0, y0
    (x_min, x_max), (y_min, y_max) = target

    while x <= x_max and y >= y_min:
        if x_min <= x and y_max >= y:
            return True
        x0 = max(x0 - 1, 0)
        y0 -= 1
        x += x0
        y += y0

    return False


def max_height(y):
    total = 0
    while y > 0:
        total += y
        y -= 1
    return total


def basic(target):
    max_h = 0
    (x_min, x_max), (y_min, y_max) = target
    for y in range(y_min, -y_min):
        for x in range(1, x_max + 1):
            if probe_reaches_target(x, y, target):
                max_h = max_height(y)
    return max_h


def advanced(target):
    total = 0
    (x_min, x_max), (y_min, y_max) = target
    for y in range(y_min, -y_min):
        for x in range(1, x_max + 1):
            if probe_reaches_target(x, y, target):
                total += 1
    return total


if __name__ == "__main__":
    target = (282, 314), (-80, -45)

    part1 = basic(target)
    print("First part:", part1)

    part2 = advanced(target)
    print("Second part:", part2)
