import numpy as np
from itertools import product
from collections import defaultdict
import time
import datetime
import sys

G = []
DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]
s_time = time.time()

for line in open("15.txt"):
    line = line.strip()
    X = []
    for x in line:
        X.append(int(x))
    G.append(X)

depth = len(G)
width = len(G[0])


def get_next_vertice(dist, visited):
    min_ = sys.maxsize
    for r, c in product(range(depth), range(width)):
        if dist[r][c] != " " and dist[r][c] < min_ and (r, c) not in visited:
            min_ = dist[r][c]
            min_pos = (r, c)
    return min_pos


def dijkstra(start):
    dist = []
    for r in range(depth):
        dist.append([])
        for _ in range(width):
            dist[r].append(" ")

    dist[start[0]][start[1]] = 0
    visited = set()

    while (depth - 1, width - 1) not in visited:
        curr = get_next_vertice(dist, visited)
        visited.add(curr)
        for d in range(4):
            rr = curr[0] + DR[d]
            cc = curr[1] + DC[d]
            if 0 <= rr < depth and 0 <= cc < width and dist[rr][cc] == " ":
                dist[rr][cc] = dist[curr[0]][curr[1]] + G[rr][cc]
        # for r in range(len(dist)):
        #     print(dist[r])
        # print()
    print(
        f"Computing time: {str(datetime.timedelta(seconds=round(time.time()-s_time, 0)))}"
    )
    return dist[depth - 1][width - 1]


print(dijkstra((0, 0)))
