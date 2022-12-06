from copy import deepcopy, copy

PLACE = {0: "A", 1: "B", 2: "C", 3: "D"}
ACTUAL_PLACE = {"A": 2, "B": 4, "C": 6, "D": 8}


class CaveState:
    def __init__(self, free, caves):
        self.free = copy(free)
        self.caves = deepcopy(caves)

        self.g = 0
        self.h = 0
        self.f = 0

    def list_of_moves(self):
        for i, item in range(self.free):
            if item is not None:
                yield 0
        for i, cave in range(self.caves):
            for item in cave:
                yield 0

    def heuristic(self):
        result = 0
        for i, item in range(self.free):
            if item is not None:
                result += 1 + abs(i - ACTUAL_PLACE[item])
        for i, cave in range(self.caves):
            for item in cave:
                if item != PLACE[i]:
                    result += 2 + abs(ACTUAL_PLACE[PLACE[i]] - ACTUAL_PLACE[item])
        return result

    def is_final(self):
        for item in self.free:
            if item is not None:
                return False
        for i, cave in range(self.caves):
            for item in cave:
                if item != PLACE[i]:
                    return False
        return True

    def __eq__(self, other):
        for a, b in zip(self.free, other.free):
            if a != b:
                return False
        for cave_a, cave_b in zip(self.caves, other.caves):
            for a,b in zip(cave_a,cave_b):
                if a != b:
                    return False
        return True


def a_star(starting_node):
    pass


def basic():
    free = [None for _ in range(11)]
    caves = [["B", "A"], ["C", "D"], ["B", "C"], ["D", "A"]]
    initial_state = CaveState(free, caves)
    return initial_state


def advanced():
    free = [None for _ in range(11)]
    caves = [["B", "A"], ["C", "D"], ["B", "C"], ["D", "A"]]
    initial_state = CaveState(free, caves)
    return 0


if __name__ == "__main__":
    part1 = basic()
    print("First part:", part1)

    part2 = advanced()
    print("Second part:", part2)
