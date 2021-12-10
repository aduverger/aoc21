grid = []
for line in open("9.in"):
    grid.append([int(x) for x in line.strip()])

min_coord = []
for r in range(len(grid)):
    for c in range(len(grid[0])):
        is_min = True
        if r > 0:
            is_min *= grid[r][c] < grid[r - 1][c]
        if r < len(grid) - 1:
            is_min *= grid[r][c] < grid[r + 1][c]
        if c > 0:
            is_min *= grid[r][c] < grid[r][c - 1]
        if c < len(grid[0]) - 1:
            is_min *= grid[r][c] < grid[r][c + 1]
        if is_min:
            min_coord.append((r, c))

risk = 0
for coord in min_coord:
    risk += grid[coord[0]][coord[1]] + 1

print(f"P1: {risk}")


def create_basin(coord):
    basin_coords = []
    r = coord[0]
    c = coord[1]
    if grid[r][c] != 9:
        basin_coords.append(coord)
    if r > 0 and grid[r][c] < grid[r - 1][c]:
        next_coords = create_basin((r - 1, c))
        for next_coord in next_coords:
            basin_coords.append(next_coord)
    if r < len(grid) - 1 and grid[r][c] < grid[r + 1][c]:
        next_coords = create_basin((r + 1, c))
        for next_coord in next_coords:
            basin_coords.append(next_coord)
    if c > 0 and grid[r][c] < grid[r][c - 1]:
        next_coords = create_basin((r, c - 1))
        for next_coord in next_coords:
            basin_coords.append(next_coord)
    if c < len(grid[0]) - 1 and grid[r][c] < grid[r][c + 1]:
        next_coords = create_basin((r, c + 1))
        for next_coord in next_coords:
            basin_coords.append(next_coord)

    return basin_coords


sizes = []
for coord in min_coord:
    basin = set(create_basin(coord))
    sizes.append(len(basin))

sizes = sorted(sizes)

print(f"P2: {sizes[-1] * sizes[-2] * sizes[-3]}")
