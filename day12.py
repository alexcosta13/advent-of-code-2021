FILENAME = "inputs/day12.txt"


def find_paths(start, path, connections, paths):
    for next_cave in connections[start]:
        if next_cave == "end":
            paths.append(path + ["end"])
        elif (next_cave in path and next_cave.islower()) or next_cave == "start":
            pass
        else:
            find_paths(next_cave, path + [next_cave], connections, paths)
    return paths


def find_paths_advanced(start, path, connections, paths, double=None):
    for next_cave in connections[start]:
        if next_cave == "end":
            paths.append(path + ["end"])
        elif next_cave == double or next_cave == "start":
            pass
        elif next_cave.islower() and double is None and next_cave in path:
            find_paths_advanced(
                next_cave, path + [next_cave], connections, paths, next_cave
            )
        elif next_cave.islower() and double is not None and next_cave in path:
            pass
        else:
            find_paths_advanced(
                next_cave, path + [next_cave], connections, paths, double
            )
    return paths


def basic(input, advanced=False):
    connections = {}
    for line in input:
        a, b = line.split("-")
        if a in connections:
            connections[a].append(b)
        else:
            connections[a] = [b]
        if b in connections:
            connections[b].append(a)
        else:
            connections[b] = [a]
    recursive_function = find_paths_advanced if advanced else find_paths
    paths = recursive_function("start", ["start"], connections, [])
    return len(paths)


if __name__ == "__main__":
    with open(FILENAME) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]

    part1 = basic(lines)
    print("First part:", part1)

    part2 = basic(lines, advanced=True)
    print("Second part:", part2)
