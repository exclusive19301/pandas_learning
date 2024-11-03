import matplotlib.pyplot as plt

years = [2018, 2019, 2020, 2021, 2022,
2023]
python_position = [7, 4, 4, 3, 4, 3]

js_position = [1, 1, 1, 1, 1, 1]

sql_position = [4,3,3,4,3,4]

typescript_position = [12,10,9,7,5,5]

plt.title("Most-Wanted Language Ranking" )
plt.xlabel("Year" )
plt.ylabel("Position")
plt.ylim(bottom = 15, top =0)
# plt.plot(years, python_position)
# plt.plot(years, js_position)
# plt.plot(years, sql_position)
# plt.plot(years, typescript_position)

# plt. legend( [
# "Python",
# "JavaScript",
# "SQL",
# "Typescript"

# ])

# better way to do plot and legend in 1 - also add linestyles.

plt.plot(years, python_position, label = "Python") # defaults to a solid line
plt.plot(years, js_position, label = "JavaScript", linestyle = "dashed" )
plt.plot(years, sql_position, label = "SQL", linestyle = "dotted")
plt.plot(years, typescript_position, label = "Typescript", linestyle = "dashdot")

plt. show( )