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


import pandas as pd

# Data for planets
data = {
    "Name": ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"],
    "Average Temperature (°C)": [167, 464, 15, -65, -110, -140, -195, -200],
    "Radius (KM)": [2439.7, 6051.8, 6371, 3389.5, 69911, 58232, 25362, 24622],
    "Color": ["Gray", "Yellow", "Blue", "Red", "Brown", "Yellow", "Cyan", "Blue"],
    "Interesting Feature": [
        "Closest planet to the Sun",
        "Hottest planet in the solar system",
        "Only planet known to support life",
        "Has the tallest volcano (Olympus Mons)",
        "Largest planet in the solar system",
        "Has the most extensive ring system",
        "Rotates on its side",
        "Strongest winds in the solar system"
    ]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)