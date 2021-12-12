from collections import defaultdict

D = defaultdict(list)
for line in open("12.in"):
    a, b = line.strip().split("-")
    D[a].append(b)
    D[b].append(a)


def is_small(x):
    return x != "end" and x.lower() == x


def search(pos, visited, twice):
    if pos == "end":
        return 1
    cnt = 0
    for next in D[pos]:
        if next == "start":
            continue
        elif is_small(next):
            if next in visited:
                if not twice:
                    cnt += search(next, visited, True)
            else:
                cnt += search(next, visited + [next], twice)
        else:
            cnt += search(next, visited, twice)
    return cnt


print(f'P1: {search("start", [], True)}')
print(f'P2: {search("start", [], False)}')
