import pandas as pd

# languages = pd.Series (["Python", "Javascript", "HTML", "SQL"])

# Ranking = pd.Series([3, 1, 2, 4])

# # print(languages)
# # print(Ranking)

# # df = pd.DataFrame([("Anne", 30), ("Bill", 27), ("Charlie", 55)], columns=["Name", "Age"])
# # print(df)

# # df = pd.DataFrame({
# #     "Languages": languages,
# #     "Ranking": Ranking
# # })

# df = pd.concat([languages, Ranking], axis=1)

# print(df)

# df = pd.read_csv("speeds.csv")

df = pd.read_excel("speeds.xlsx")

print(df)