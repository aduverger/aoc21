G = {}
p1 = False
for line in open("13.in"):
    line = line.strip()
    if line != "" and line[0] != "f":  # if coords
        x, y = line.split(",")
        x, y = int(x), int(y)
        G[(x, y)] = "#"
    elif line != "" and line[0] == "f":  # if fold
        ax = line.split("=")[0][-1]
        val = int(line.split("=")[1])
        G2 = {}
        if ax == "x":
            for x, y in G:
                if x < val:
                    G2[(x, y)] = "#"
                elif x > val:
                    G2[(2 * val - x, y)] = "#"
        else:
            for x, y in G:
                if y < val:
                    G2[(x, y)] = "#"
                elif y > val:
                    G2[(x, 2 * val - y)] = "#"
        if not p1:
            print(f"P1: {len(G2)}")
            p1 = True
        G = G2

X = [x for x, _ in G]
Y = [y for _, y in G]

for y in range(max(Y) + 1):
    for x in range(max(X) + 1):
        print(G[(x, y)] if (x, y) in G else " ", end="")
    print()
