class Dice:
    def __init__(self, max_num=100):
        self.num = 0
        self.max_num = max_num

    def roll(self):
        result = 0
        for _ in range(3):
            result += self.num
            self.num = (self.num + 1) % self.max_num
        return result + 3


def get_dice_rolls():
    result = {}
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                result[i + j + k] = result.get(i + j + k, 0) + 1
    return result


def move(player, score, dice, max_pos):
    player = (player + dice) % max_pos
    score += player + 1
    return player, score


def next_move(p1, p2, s1, s2, turn, repetitions, dice, acc):
    if s1 > 20 or s2 > 20:
        acc[turn % 2 - 1] += repetitions
        return
    if turn % 2 == 0:
        for roll in dice:
            player1 = (p1 + roll) % 10
            next_move(player1, p2, s1 + player1 + 1, s2,
                      (turn + 1) % 2, repetitions * dice[roll], dice, acc)
    else:
        for roll in dice:
            player2 = (p2 + roll) % 10
            next_move(p1, player2, s1, s2 + player2 + 1,
                      (turn + 1) % 2, repetitions * dice[roll], dice, acc)


def basic(p1, p2, max_pos=10):
    dice = Dice()
    score1, score2 = 0, 0
    turn = 0
    while score1 < 1000 and score2 < 1000:
        if turn % 2 == 0:
            p1, score1 = move(p1, score1, dice.roll(), max_pos)
        else:
            p2, score2 = move(p2, score2, dice.roll(), max_pos)
        turn += 1
    loser = score1 if score1 < 1000 else score2
    return loser * turn * 3


def advanced(p1, p2):
    acc = [0, 0]
    next_move(p1, p2, 0, 0, 0, 1, get_dice_rolls(), acc)
    return max(acc)


if __name__ == "__main__":
    position1 = 7 - 1
    position2 = 2 - 1

    part1 = basic(position1, position2)
    print("First part:", part1)

    part2 = advanced(position1, position2)
    print("Second part:", part2)
