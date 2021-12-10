starts = []
ends = []
for line in open("5.in"):
    line = line.split(" -> ")
    starts.append([int(x) for x in line[0].split(",")])
    ends.append([int(x) for x in line[1].split(",")])

depth = 0
all_coords = starts + ends
for coord in all_coords:
    if coord[0] > depth:
        depth = coord[0]
    elif coord[1] > depth:
        depth = coord[1]
gridA = [[0 for _ in range(depth + 1)] for _ in range(depth + 1)]
gridB = [[0 for _ in range(depth + 1)] for _ in range(depth + 1)]

for i in range(len(starts)):
    if starts[i][0] == ends[i][0]:
        x = starts[i][0]
        y_0 = min(starts[i][1], ends[i][1])
        y_1 = max(starts[i][1], ends[i][1])
        for y in range(y_0, y_1 + 1):
            gridA[y][x] += 1
            gridB[y][x] += 1
    elif starts[i][1] == ends[i][1]:
        y = starts[i][1]
        x_0 = min(starts[i][0], ends[i][0])
        x_1 = max(starts[i][0], ends[i][0])
        for x in range(x_0, x_1 + 1):
            gridA[y][x] += 1
            gridB[y][x] += 1
    elif abs(starts[i][0] - ends[i][0]) == abs(starts[i][1] - ends[i][1]):
        x_0 = starts[i][0]
        x_1 = ends[i][0]
        y_0 = starts[i][1]
        y_1 = ends[i][1]
        dx = -1 if x_0 > x_1 else 1
        dy = -1 if y_0 > y_1 else 1
        for j in range(abs(starts[i][1] - ends[i][1]) + 1):
            gridB[y_0 + j * dy][x_0 + j * dx] += 1

nb_pointsA = 0
nb_pointsB = 0
for r in range(depth + 1):
    for c in range(depth + 1):
        if gridA[r][c] > 1:
            nb_pointsA += 1
        if gridB[r][c] > 1:
            nb_pointsB += 1

print(f"P1: {nb_pointsA}")
print(f"P2: {nb_pointsB}")
