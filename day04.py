FILENAME = "inputs/day04.txt"


class Board:
    def __init__(self, data):
        self.data = [list(map(int, line.split())) for line in data.split("\n")]
        self.columns = zip(*self.data)
        self.size = len(self.data)
        self.winning_number = 0
        self.bingo = [[False for _ in range(self.size)] for _ in range(self.size)]

    def solve(self, numbers):
        self.bingo = [[False for _ in range(self.size)] for _ in range(self.size)]
        for length, n in enumerate(numbers):
            i, j = self.get_indices(n)
            if i is not None:
                self.bingo[i][j] = True
                if self.check_matrix():
                    self.winning_number = n
                    break
        return length

    def get_score(self):
        total = 0
        for i in range(self.size):
            for j in range(self.size):
                if not self.bingo[i][j]:
                    total += self.data[i][j]
        return total * self.winning_number

    def get_indices(self, number):
        for i in range(self.size):
            for j in range(self.size):
                if self.data[i][j] == number:
                    return i, j
        return None, None

    def check_matrix(self):
        for row in self.bingo:
            if all(row):
                return True
        self.columns = zip(*self.bingo)
        for row in self.columns:
            if all(row):
                return True
        return False

    def __repr__(self):
        return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.data])


def basic(boards, numbers):
    results = [(board, board.solve(numbers)) for board in boards]
    winner, _ = min(results, key=lambda x: x[1])
    return winner.get_score()


def advanced(boards, numbers):
    results = [(board, board.solve(numbers)) for board in boards]
    winner, _ = max(results, key=lambda x: x[1])
    return winner.get_score()


if __name__ == "__main__":
    with open(FILENAME) as f:
        lines = f.read()
    drawn_numbers = list(map(int, lines.split("\n")[0].split(",")))
    boards = lines.split("\n\n")[1:]
    boards = [Board(data) for data in boards]

    part1 = basic(boards, drawn_numbers)
    print("First part:", part1)

    part2 = advanced(boards, drawn_numbers)
    print("Second part:", part2)
