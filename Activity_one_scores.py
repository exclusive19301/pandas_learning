import pandas as pd

df = pd.read_csv("results.csv")

# df.info()
# print(df.describe())

df = pd.read_csv("results.csv")

# print(df.shape)

# print(df.columns)

# print(df.index)

# print(df.dtypes)


#how many different tournaments were there?
tournament_counts = df["tournament"].value_counts()
unique_tournaments = len(tournament_counts)  
print(f"Number of different tournaments: {unique_tournaments}")


#how many matches were played in each tournament
print("Matches played under each tournament:")
print(tournament_counts)

home_team_counts = df["home_team"].value_counts()
most_reported_home_team = home_team_counts.index[0]
print(f"Most reported home team: {most_reported_home_team}")

home_team_counts = df["home_team"].value_counts()
print(home_team_counts).head()

# 4. The most reported home team
home_team_counts = df["home_team"].value_counts()
most_reported_home_team = home_team_counts.index[0]
print(f"Most reported home team: {most_reported_home_team}")

# 5. The most reported away team
away_team_counts = df["away_team"].value_counts()
most_reported_away_team = away_team_counts.index[0]
print(f"Most reported away team: {most_reported_away_team}")

# 6. The least reported home team
least_reported_home_team = df["home_team"].value_counts().index[-1]
print(f"Least reported home team: {least_reported_home_team}")

# 7. The least reported away team
least_reported_away_team = df["away_team"].value_counts().index[-1]
print(f"Least reported away team: {least_reported_away_team}")