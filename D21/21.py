from itertools import product

lines = open("21.txt").read().split("\n")
pos1, pos2 = int(lines[0][-1]), int(lines[1][-1])
POS = [pos1, pos2]
DIE = list(range(1, 101))


def roll(i):
    die = 0
    for _ in range(3):
        die += DIE[i]
        i = i + 1 if (i < len(DIE) - 1) else 0
    return die, i


def roll_determ(pos1, pos2):
    i, cnt, score1, score2 = 0, 0, 0, 0
    while True:
        # PLAYER 1
        die, i = roll(i)
        cnt += 3
        pos1 = (pos1 + die) % 10 if (pos1 + die) % 10 != 0 else 10
        score1 += pos1
        if score1 >= 1_000:
            return score2 * cnt
        # PLAYER 2
        die, i = roll(i)
        cnt += 3
        pos2 = (pos2 + die) % 10 if (pos2 + die) % 10 != 0 else 10
        score2 += pos2
        if score2 >= 1_000:
            return score1 * cnt


MEMO = {}


def roll_quantum(player, POS, SCR):
    if SCR[0] >= 21:
        return (1, 0)
    elif SCR[1] >= 21:
        return (0, 1)
    if (player, str(POS), str(SCR)) in MEMO:
        return MEMO[player, str(POS), str(SCR)]
    wins = (0, 0)
    for die1, die2, die3 in product((1, 2, 3), (1, 2, 3), (1, 2, 3)):
        die = die1 + die2 + die3
        POS2 = POS.copy()
        POS2[player] = (POS[player] + die) % 10 if (POS[player] + die) % 10 != 0 else 10
        SCR2 = SCR.copy()
        SCR2[player] = SCR[player] + POS2[player]
        w1, w2 = roll_quantum(1 - player, POS2, SCR2)
        wins = (wins[0] + w1, wins[1] + w2)
    MEMO[player, str(POS), str(SCR)] = wins
    return wins


print(f"P1: {roll_determ(pos1, pos2)}")
print(f"P2: {max(roll_quantum(0, POS, [0, 0]))}")
