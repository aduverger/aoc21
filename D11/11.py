from itertools import product

grid = []
for line in open("11.in"):
    grid.append([int(x) for x in line.strip()])
depth = len(grid)
width = len(grid[0])
n_flashes = 0
rc_flashed = []  # coordinates of octopuses that flashed at each step
step = 0

# while all octopuses didn't flash at the same step:
while len(rc_flashed) != depth * width:
    step += 1
    for r, c in product(range(depth), range(width)):
        grid[r][c] += 1
    cur_flashes = -1
    rc_flashed = []
    while cur_flashes != n_flashes:  # while there is at least one flash per step
        cur_flashes = n_flashes
        for r, c in product(range(depth), range(width)):
            if grid[r][c] > 9 and (r, c) not in rc_flashed:
                rc_flashed.append((r, c))
                n_flashes += 1
                for dr, dc in product([-1, 0, 1], [-1, 0, 1]):
                    r_adj = r + dr
                    c_adj = c + dc
                    if 0 <= r_adj < depth and 0 <= c_adj < width:
                        grid[r_adj][c_adj] += 1
    for (r, c) in rc_flashed:  # all octopuses that flashed at this step reset to 0
        grid[r][c] = 0
    if step == 100:
        print(f"P1: {n_flashes}")

print(f"P2: {step}")
