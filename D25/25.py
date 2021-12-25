from itertools import product


def get_nxt_cell(G, r, c):
    nxt_r, nxt_c = r, c
    if G[r][c] == ">":
        nxt_c = c + 1 if c + 1 < len(G[0]) else 0
    elif G[r][c] == "v":
        nxt_r = r + 1 if r + 1 < len(G) else 0
    return (nxt_r, nxt_c)


def will_move(G, r, c):
    nxt_r, nxt_c = get_nxt_cell(G, r, c)
    if G[nxt_r][nxt_c] != "." or G[r][c] == ".":
        return False
    return True


def move_cell(G, r, c):
    nxt_r, nxt_c = get_nxt_cell(G, r, c)
    if will_move(G, r, c):
        G[nxt_r][nxt_c] = G[r][c]
        G[r][c] = "."
    return G


def move_all(G):
    step = 0
    changed = True
    while changed == True:
        changed = False
        for herd in (">", "v"):
            G2 = [[c for c in r] for r in G]
            for r, c in product(range(len(G2)), range(len(G2[0]))):
                if G2[r][c] == herd and will_move(G2, r, c):
                    changed = True
                    G = move_cell(G, r, c)
        step += 1
    return step


G = []
for line in open("25.txt"):
    line = line.strip()
    G.append([c for c in line])


print(move_all(G))
