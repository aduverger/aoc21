import numpy as np
from itertools import product

R = []
C = []
RC = []
folds = []
for line in open("13.in"):
    line = line.strip()
    if line != "" and line[0] != "f":
        R.append(int(line.split(",")[1]))
        C.append(int(line.split(",")[0]))
    elif line != "" and line[0] == "f":
        if line[11] == "x":
            folds.append(("x", int(line[13:])))
        else:
            folds.append(("y", int(line[13:])))

G = np.zeros((max(R) + 1, max(C) + 1))
G[R, C] = 1
print(G.shape)


def fold_it(G, folds):
    Gx = np.copy(G)
    p1 = False
    for fold in folds:
        print(fold[0], fold[1])
        if fold[0] == "y":
            y = fold[1]
            for r, c in product(range(y + 1), range(Gx.shape[1])):
                if Gx[r, c] != 1:
                    Gx[r, c] = Gx[-r - 1][c]
            Gx = Gx[:y]
        elif fold[0] == "x":
            x = fold[1]
            for r, c in product(range(Gx.shape[0]), range(x + 1)):
                if Gx[r, c] != 1:
                    Gx[r, c] = Gx[r, -c - 1]
            Gx = Gx[:, :x]
        if not p1:
            p1 = True
            print(np.count_nonzero(Gx))

    return Gx


G2 = fold_it(G, folds)
for r in range(G2.shape[0]):
    for c in range(G2.shape[1]):
        print("#" if G2[r, c] == 1 else " ", end="")
    print()
