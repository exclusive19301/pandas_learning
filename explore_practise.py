import pandas as pd

df = pd.read_csv("results.csv")

# print(df)

# df.info()

print (df.describe())

# print (df["home_score"]).value_counts(normalize=True), * 100)

print(df["home_score"] < 7)

mask = df["home_score"] < 5

masked_df = df[mask]

print(masked_df["home_score"].mean())