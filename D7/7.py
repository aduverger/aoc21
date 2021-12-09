import numpy as np

for line in open("7.in"):
    X = [int(x) for x in line.split(",")]

med = int(np.round(np.median(X)))
moy = int(np.mean(np.array(X)))
fuels1 = 0
fuels2 = 0
for pos in X:
    fuels1 += abs(pos - med)
    for i in range(1, abs(pos - moy) + 1):
        fuels2 += i

print(f"P1: {fuels1}")
print(f"P2: {fuels2}")
