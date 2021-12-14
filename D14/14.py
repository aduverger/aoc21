from collections import defaultdict

# Parse the input file
rules = {}
lines = open("14.in").read().split("\n")
template = lines[0].strip()
for line in lines[2:]:
    line = line.strip()
    rules[line.split("->")[0].strip()[:2]] = line.split("->")[1].strip()

# Initialize letters and pairs counts with the template
letters_count = defaultdict(int)
pairs_count = defaultdict(int)
for i in range(len(template) - 1):
    letters_count[template[i]] += 1
    pairs_count[template[i] + template[i + 1]] += 1
letters_count[template[-1]] += 1

for step in range(40):
    pairs_count_temp = pairs_count.copy()
    for pair, cnt in pairs_count_temp.items():
        new_letter = rules[pair]
        letters_count[new_letter] += cnt
        pairs_count[pair] -= cnt
        pairs_count[pair[0] + new_letter] += cnt
        pairs_count[new_letter + pair[1]] += cnt
    if step == 9:
        print(f"P1: {max(letters_count.values()) - min(letters_count.values())}")
print(f"P2: {max(letters_count.values()) - min(letters_count.values())}")
