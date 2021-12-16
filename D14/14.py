from collections import defaultdict

# Parse the input file
template, _, *rules = open("14.in").read().split("\n")
rules = {r.split("->")[0].strip(): r.split("->")[1].strip() for r in rules}

# Initialize letters and pairs counts with the template
letters_count = defaultdict(int)
pairs_count = defaultdict(int)
for i in range(len(template) - 1):
    letters_count[template[i]] += 1
    pairs_count[template[i] + template[i + 1]] += 1
letters_count[template[-1]] += 1

for step in range(40):
    for pair, cnt in pairs_count.copy().items():
        new_letter = rules[pair]
        letters_count[new_letter] += cnt
        pairs_count[pair] -= cnt
        pairs_count[pair[0] + new_letter] += cnt
        pairs_count[new_letter + pair[1]] += cnt
    if step == 9:
        print(f"P1: {max(letters_count.values()) - min(letters_count.values())}")
print(f"P2: {max(letters_count.values()) - min(letters_count.values())}")
