numbers = None
boards = []
for line in open("4.in"):
    line = line.strip()
    if numbers == None:
        numbers = line.split(",")
    elif line == "":
        boards.append([])
    else:
        boards[-1].append(line.split())

won_boards = []
for _ in boards:
    won_boards.append([[False for _ in range(5)] for _ in range(5)])

n_wins = 0
WON = [False for _ in range(len(boards))]

for number in numbers:
    for i in range(len(boards)):
        for r in range(5):
            for c in range(5):
                if boards[i][r][c] == number:
                    won_boards[i][r][c] = int(number)

        won = False
        for r in range(5):
            won_r = True
            for c in range(5):
                if not won_boards[i][r][c]:
                    won_r = False
            if won_r:
                won = True
        for c in range(5):
            won_c = True
            for r in range(5):
                if not won_boards[i][r][c]:
                    won_c = False
            if won_c:
                won = True

        if won and not WON[i]:
            WON[i] = True
            n_wins += 1
            score = 0
            for r in range(5):
                for c in range(5):
                    if not won_boards[i][r][c]:
                        score += int(boards[i][r][c])
            score *= int(number)
            if n_wins == 1 or n_wins == len(boards) - 1:
                print(score)
