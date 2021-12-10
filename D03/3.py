import pandas as pd
from bitstring import BitArray

df = pd.read_csv("3.in", header=None, names=["binary"], dtype=str)
for i in range(len(df["binary"][0])):
    df[i] = df["binary"].apply(lambda word: word[i])

gamma = ""
epsilon = ""
for i in range(len(df["binary"][0])):
    gamma += str(df[i].value_counts().index[0])
    epsilon += str(df[i].value_counts().index[1])

print(f"P1: {BitArray(bin=gamma).uint * BitArray(bin=epsilon).uint}")


with open("3.in") as f:
    inlines = f.read().splitlines()
N = []
for line in inlines:
    line = line.strip()
    N.append(line)

width = len(N[0])

A = list(N)
B = list(N)
for i in range(width):
    if len(A) > 1:
        a0 = len([x for x in A if x[i] == "0"])
        a1 = len([x for x in A if x[i] == "1"])
        if a1 >= a0:
            A = [x for x in A if x[i] == "1"]
        else:
            A = [x for x in A if x[i] == "0"]
    if len(B) > 1:
        b0 = len([x for x in B if x[i] == "0"])
        b1 = len([x for x in B if x[i] == "1"])
        if b1 >= b0:
            B = [x for x in B if x[i] == "0"]
        else:
            B = [x for x in B if x[i] == "1"]
print(f"P2: {int(A[0], 2) * int(B[0], 2)}")
