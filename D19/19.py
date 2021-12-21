from itertools import product, permutations
from collections import defaultdict


def diff_(c1, c2):
    return tuple(c1[i] - c2[i] for i in range(3))


def sum_(c1, c2):
    return tuple(c1[i] + c2[i] for i in range(3))


def manhattan(c1, c2):
    return sum(max(c1[i] - c2[i], c2[i] - c1[i]) for i in range(3))


def get_scnr_coord(coords1, coords2):
    """get scanner2 coordinates (`coords2`) relative to scanner1 (`coords1`)"""
    DIFF = defaultdict(int)
    for c1, c2 in product(coords1, coords2):
        DIFF[diff_(c1, c2)] += 1
    if max(DIFF.values()) > 11:
        return max(DIFF, key=DIFF.get)
    return -1


def rotate(coords, r, t):
    """rotate and/or translate the coordinates of a given scanner.
    e.g.: if (x, y ,z) -> (-x, z, -y), then r = (0, 2, 1) and t = (-1, 1, -1)"""
    r_coords = []
    for coord in coords:
        new_x = t[0] * coord[r[0]]
        new_y = t[1] * coord[r[1]]
        new_z = t[2] * coord[r[2]]
        r_coords.append((new_x, new_y, new_z))
    return r_coords


def find_those_beacons():
    D0 = D[0]  # List of beacons coordinates, relative to scanner 0
    SCNR = [(0, 0, 0)]  # List of scanners coordinates, relative to scanner 0
    scnr_to_fnd = list(range(1, len(D)))  # List of scanners to find (all except 0)
    while scnr_to_fnd:  # while there is still scanners to find
        for scnr in scnr_to_fnd:  # try to find overlapping betwen scanner 0 and scnr
            for r, t in product(
                permutations((0, 1, 2), 3), product((-1, 1), (-1, 1), (-1, 1))
            ):
                r_coords = rotate(D[scnr], r, t)
                scnr_coord = get_scnr_coord(D0, r_coords)
                if scnr_coord != -1:  # This is a match ! Between scanner 0 and scnr
                    scnr_to_fnd.remove(scnr)  # scnr is found so remove it
                    SCNR.append(scnr_coord)  # save its coordinates for part2
                    for coord in r_coords:
                        if sum_(coord, scnr_coord) not in D0:
                            # add these new beacons coordinates, relative to 0
                            D0.append(sum_(coord, scnr_coord))
                    break
    return D0, SCNR


## PARSE INPUT
D = defaultdict(list)
scnr = -1
for line in open("19.txt"):
    line = line.strip()
    if line.startswith("---"):
        scnr += 1
    elif line != "":
        x, y, z = line.split(",")
        D[scnr].append((int(x), int(y), int(z)))

D0, SCNR = find_those_beacons()
## PART 1
print(f"P1: {len(D0)}")
## PART 2
d = 0
for i, j in product(range(len(D)), range(len(D))):
    d = max(d, manhattan(SCNR[i], SCNR[j]))
print(f"P2: {d}")
