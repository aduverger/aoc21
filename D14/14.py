from collections import defaultdict

# Parse the input file
is_template = True
rules = {}
for line in open("14.in"):
    line = line.strip()
    if is_template:
        template = line
        is_template = False
    elif line != "":
        rules[line.split("->")[0].strip()[:2]] = line.split("->")[1].strip()

# Initialize letters and pairs counts with the template
letters_count = defaultdict(int)
pairs_count = defaultdict(int)
for i in range(len(template) - 1):
    letters_count[template[i]] += 1
    pairs_count[template[i] + template[i + 1]] += 1
letters_count[template[-1]] += 1

# Function to print the answer for parts 1 and 2
def print_answer(letters_count, part="P1"):
    min_value, max_value = 0, 0
    for value in letters_count.values():
        if min_value == 0 or value < min_value:
            min_value = value
        elif value > max_value:
            max_value = value
    print(f"{part}: {max_value - min_value}")


for step in range(40):
    pairs_count_temp = pairs_count.copy()
    for pair, cnt in pairs_count_temp.items():
        new_letter = rules[pair]
        letters_count[new_letter] += cnt
        pairs_count[pair] -= cnt
        pairs_count[pair[0] + new_letter] += cnt
        pairs_count[new_letter + pair[1]] += cnt
    if step == 9:
        print_answer(letters_count, "P1")
print_answer(letters_count, "P2")
