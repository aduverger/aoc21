import numpy as np
from itertools import product


def pxl_conv(G, r, c):
    DR = [-1, 0, 1]
    DC = [-1, 0, 1]
    output = ""
    for dr, dc in product(DR, DC):
        rr = r + dr
        cc = c + dc
        if not (0 <= rr < G.shape[0] and 0 <= cc < G.shape[1]):
            rr, cc = r, c  # Deal with edges of the grid
        output += str(G[rr, cc])
    return algo[int(output, 2)]


def img_conv(G):
    G1 = np.empty((G.shape[0], G.shape[1]), dtype=int)
    for r, c in product(range(G.shape[0]), range(G.shape[1])):
        G1[r, c] = pxl_conv(G, r, c)
    return G1


## PARSE INPUT
# We change `#` for `1` and `.` for `0` to ease the binary conversion
lines = open("20.txt").read().split("\n")
algo = [int(char == "#") for char in lines[0]]
G = np.array([[int(char == "#") for char in row] for row in lines[2:]])

## PAD INPUT
steps = 50
padding = steps
G = np.pad(G, padding, mode="constant", constant_values=0)

## PARTS 1 & 2
for step in range(steps):
    G = img_conv(G)
    if step == 1:
        print(f"P1: {np.count_nonzero(G == 1)}")
print(f"P2: {np.count_nonzero(G == 1)}")
