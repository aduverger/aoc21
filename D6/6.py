import numpy as np

ages = []
for line in open("6.in"):
    line = line.split(",")
    ages = [int(x) for x in line]

X = [0 for _ in range(9)]

for age in ages:
    X[age] += 1

for d in range(256):
    Y = [0 for _ in range(9)]
    for age in range(9):
        if age == 0:
            Y[6] += X[age]
            Y[8] += X[age]
        else:
            Y[age - 1] += X[age]
    X = Y
    if d == 79:
        print(f"P1: {np.array(X).sum()}")

print(f"P2: {np.array(X).sum()}")
