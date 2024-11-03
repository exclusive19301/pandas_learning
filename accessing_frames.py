import pandas as pd
import numpy as np

df = pd.read_excel("dev_rankings.xlsx")
df = df.set_index("Languages")
print(df)

print(df["Ranking 2019"])

print(df [["Ranking 2022", "Ranking 2019"]])

print(df.loc[:,"Ranking 2020"])

print(df.loc["Python", "HTML",:1,"Ranking 2023", "Ranking 2021", "Ranking 2019"]])



# df.loc[["Python", "JavaScript", "HTML"], ["Ranking 2023", "Ranking 2021", "Ranking 2019"]]

# print(df)