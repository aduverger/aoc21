import pandas as pd

df = pd.read_csv("1.in", header=None, names=["depth"])
df["increased"] = 0

for index, _ in df.iterrows():
    if index > 0 and df.iloc[index, 0] > df.iloc[index - 1, 0]:
        df.iloc[index, 1] = 1

print(f'P1: {df["increased"].sum()}')


df = pd.read_csv("1.in", header=None, names=["depth"])
df["window"] = 0
df["increased"] = 0

for index, _ in df.iterrows():
    if index < df.shape[0] - 2:
        df.iloc[index, 1] = (
            df.iloc[index, 0] + df.iloc[index + 1, 0] + df.iloc[index + 2, 0]
        )

for index, _ in df.iterrows():
    if index > 0 and df.iloc[index, 1] > df.iloc[index - 1, 1]:
        df.iloc[index, 2] = 1

print(f'P2: {df["increased"].sum()}')
