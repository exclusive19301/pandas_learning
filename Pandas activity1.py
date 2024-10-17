# import pandas as pd

# df = pd.DataFrame([
#     ("Mercury", 167, 2439.7, "Gray", "Closest planet to the Sun"),
#     ("Venus", 464, 6051.8, "Yellow", "Hottest planet in the solar system"),
#     ("Earth", 15, 6371, "Blue", "Only planet known to support life"),
#     ("Mars", -65, 3389.5, "Red", "Has the tallest volcano (Olympus Mons)"),
#     ("Jupiter", -110, 69911, "Brown", "Largest planet in the solar system"),
#     ("Saturn", -140, 58232, "Yellow", "Has the most extensive ring system"),
#     ("Uranus", -195, 25362, "Cyan", "Rotates on its side"),
#     ("Neptune", -200, 24622, "Blue", "Strongest winds in the solar system")
# ], columns=["Name", "Average Temperature (°C)", "Radius (KM)", "Color", "Interesting Feature"])

# print(df)

# df.to_excel("planets.xlsx", index=False)

# print("DataFrame has been written to planets.xlsx")


import pandas as pd
import numpy as np

planet_name = pd.Series(["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"])
planet_average_temperature = pd.Series([167, 464, 15, -65, -110, -140, -195, -200])
planet_radius = pd.Series([2439.7, 6051.8, 6371, 3389.5, 69911, 58232, 25362, 24622])
planet_colour = pd.Series(["Gray", "Yellow", "Blue", "Red", "Brown", "Yellow", "Cyan", "Blue"])
planet_interesting_feature = pd.Series([
    "Closest planet to the Sun", 
    "Hottest planet in the solar system", 
    "Only planet known to support life", 
    "Has the tallest volcano (Olympus Mons)", 
    "Largest planet in the solar system", 
    "Has the most extensive ring system", 
    "Rotates on its side", 
    "Strongest winds in the solar system"
])

df = pd.DataFrame({
    "Name": planet_name,
    "Average Temperature (°C)": planet_average_temperature,
    "Radius (KM)": planet_radius,
    "Colour": planet_colour,
    "Interesting Feature": planet_interesting_feature
})

print(df)

df.to_excel("planets.xlsx")