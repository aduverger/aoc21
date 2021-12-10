matching_table = {")": "(", "]": "[", "}": "{", ">": "<"}
scoring_table1 = {">": 25137, "}": 1197, "]": 57, ")": 3}
scoring_table2 = {"<": 4, "{": 3, "[": 2, "(": 1}
score1 = 0
scores2 = []

for line in open("10.in"):
    openers = []
    score2 = 0
    is_incomplete = True
    for char in line.strip():
        if char in ["(", "[", "{", "<"]:
            openers.append(char)
        elif matching_table[char] == openers[-1]:
            openers.pop(-1)
        else:
            score1 += scoring_table1[char]
            is_incomplete = False
            break
    if is_incomplete:
        for char in openers[-1::-1]:
            score2 = score2 * 5 + scoring_table2[char]
        scores2.append(score2)

print(f"P1: {score1}")
print(f"P2: {sorted(scores2)[len(scores2) // 2]}")
