from collections import defaultdict


def reboot(p1):
    C = defaultdict(int)
    for line in open("22.txt"):
        line = line.strip().split(" ")
        ordr = 1 if line[0] == "on" else -1
        x, y, z = line[1].split(",")
        x1, x2 = map(int, x[2:].split(".."))
        y1, y2 = map(int, y[2:].split(".."))
        z1, z2 = map(int, z[2:].split(".."))
        if p1 and any([c not in range(-50, 51) for c in (x1, x2, y1, y2, z1, z2)]):
            continue
        # Try to find intersections between previous cuboids (_p) and the current one:
        for (x1_p, x2_p, y1_p, y2_p, z1_p, z2_p), ordr_p in C.copy().items():
            intr_x1 = max(x1_p, x1)
            intr_x2 = min(x2_p, x2)
            intr_y1 = max(y1_p, y1)
            intr_y2 = min(y2_p, y2)
            intr_z1 = max(z1_p, z1)
            intr_z2 = min(z2_p, z2)
            if (  # if there's an intersection between that previous cuboid and the current one
                intr_x1 < intr_x2 and intr_y1 < intr_y2 and intr_z1 < intr_z2
            ):
                # we 'cancel' its order
                C[(intr_x1, intr_x2, intr_y1, intr_y2, intr_z1, intr_z2)] -= ordr_p
        # if order is `on`, we turn on the current cuboid:
        C[(x1, x2, y1, y2, z1, z2)] += max(0, ordr)

    cnt = 0
    for (x1, x2, y1, y2, z1, z2), ordr in C.items():
        cnt += (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1) * ordr
    return cnt


print(f"P1: {reboot(p1=True)}")
print(f"P2: {reboot(p1=False)}")
