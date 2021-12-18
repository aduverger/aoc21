import ast
from itertools import product
from math import floor, ceil


def addition(pair1, pair2):
    return ["["] + pair1 + [","] + pair2 + ["]"]


def explode(number, idx_explo):
    """Here idx_explo is the index of the left value of the pair to explode"""
    # the pair's left value is added to the first regular number
    # to the left of the exploding pair (if any)
    for i in range(idx_explo - 1, -1, -1):
        if number[i] not in ["[", "]", ","]:  # if we find a regular number to the left
            number[i] = str(int(number[i]) + int(number[idx_explo]))
            break
    # the pair's right value is added to the first regular number
    # to the right of the exploding pair (if any)
    for i in range(idx_explo + 3, len(number)):
        if number[i] not in ["[", "]", ","]:  # if we find a regular number to the right
            number[i] = str(int(number[i]) + int(number[idx_explo + 2]))
            break
    # Then, the entire exploding pair is replaced with the regular number 0.
    number[idx_explo - 1 : idx_explo + 4] = "0"
    return number


def should_explode(number):
    """Return the index of the left value to explode (if any), else return -1"""
    brackets_cnt = 0
    for idx in range(len(number)):
        if number[idx] == "[":
            brackets_cnt += 1
        elif number[idx] == "]":
            brackets_cnt -= 1
        elif number[idx] != "," and brackets_cnt > 4:
            return idx
    return -1


def split(number, idx_split):
    new_number = number[:idx_split]
    lft_value = floor(int(number[idx_split]) / 2)
    rght_value = ceil(int(number[idx_split]) / 2)
    new_number += ["[", str(lft_value), ",", str(rght_value), "]"]
    new_number += number[idx_split + 1 :]
    return new_number


def should_split(number):
    """Return the index of the value to split (if any), else return -1"""
    for idx in range(len(number)):
        if number[idx] not in ["[", "]", ","] and int(number[idx]) > 9:
            return idx
    return -1


def reduce(number):
    idx_explo, idx_split = 0, 0
    while idx_explo != -1 or idx_split != -1:
        idx_explo = should_explode(number)
        if idx_explo != -1:
            number = explode(number, idx_explo)
        else:
            idx_split = should_split(number)
            if idx_split != -1:
                number = split(number, idx_split)
    return number


def get_magnitude(number):
    if isinstance(number, int):
        return number  # The magnitude of a regular number is just that number
    elif isinstance(number[0], str):
        # If number (string) has not already been transformed into a list of int
        number = ast.literal_eval("".join(n for n in number))
    return 3 * get_magnitude(number[0]) + 2 * get_magnitude(number[1])


# PARSE INPUT
N = []
for line in open("18.txt"):
    N.append([c for c in line.strip()])

# PART 1
for i in range(len(N) - 1):
    if i == 0:
        number = N[i]
    number = reduce(addition(number, N[i + 1]))
print(f"P1: {get_magnitude(number)}")

## PART 2
magnitudes = []
for i, j in product(range(len(N)), range(len(N))):
    if i != j:
        magnitudes.append(get_magnitude(reduce(addition(N[i], N[j]))))
print(f"P2: {max(magnitudes)}")
