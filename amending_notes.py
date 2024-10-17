import pandas as pd

languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])
ranking = pd.Series([3,1,2,4])

df = pd.DataFrame({
    "Languages": languages,
    "Ranking": ranking
})

df. loc[4] = ["PHP", 11]


# df.loc[3.5] = ["KESL", 20]

# df = df.sort_index()
# df = df.reset_index()
new_data = pd.DataFrame({
"Languages": ["Java", "Typescript"],
    "Ranking": [7, 5]
})

df = pd.concat([df,new_data], ignore_index=True)

df ["Ranking 2022"] = [4,1,2,3,10,6,5]

df = df.sort_values("Ranking")



print(df)
