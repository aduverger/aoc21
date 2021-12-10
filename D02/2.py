import pandas as pd

df = pd.read_csv("2.in", sep=" ", header=None, names=["move", "units"])
df["horizontal"] = 0
df["depth"] = 0

for index, row in df.iterrows():
    if index > 0:
        df.iloc[index, 2] = df.iloc[index - 1, 2]
        df.iloc[index, 3] = df.iloc[index - 1, 3]
    if row["move"] == "forward":
        df.iloc[index, 2] += row["units"]
    elif row["move"] == "down":
        df.iloc[index, 3] += row["units"]
    else:
        df.iloc[index, 3] -= row["units"]

print(f"P1: {df.iloc[index, 2] * df.iloc[index, 3]}")

df = pd.read_csv("2.in", sep=" ", header=None, names=["move", "units"])
df["horizontal"] = 0
df["depth"] = 0
current_aim = 0

for index, row in df.iterrows():
    if index > 0:
        df.iloc[index, 2] = df.iloc[index - 1, 2]
        df.iloc[index, 3] = df.iloc[index - 1, 3]
    if row["move"] == "down":
        current_aim += row["units"]
    elif row["move"] == "up":
        current_aim -= row["units"]
    else:
        df.iloc[index, 2] += row["units"]
        df.iloc[index, 3] += row["units"] * current_aim

print(f"P2: {df.iloc[index, 2] * df.iloc[index, 3]}")
