import pandas as pd

df= pd.read_csv("spotify_songs.csv")

# df.info()

# print(df.shape)

# print(df.columns)

# print(df.index)

# print(df.dtypes)

# print(df['track_artist']) 

# print(df["playlist_genre"].value_counts())

# print(df["track_artist"].value_counts())

# print(df["playlist_genre"].mode())

# print(df["playlist_genre"].mode(0))

# print(df ["duration_ms"].median())

# print(df ["duration_ms"].mean())


# max_duration = df["duration_ms"].max()
# min_duration = df["duration_ms"].min()

# total_ms = max_duration - min_duration


# total_seconds = total_ms / 1000

# print("Difference between max and min duration (in seconds):", total_seconds)


# print(df.sort_values(by=["duration_ms"] ))



# element = df.loc[row_label, column_label]


# element = df.iloc[row_index, column_index]

# df_sorted = df.sort_values(by="duration_ms", ascending=False)
# print(df_sorted)

# print(df.groupby('playlist_genre')['duration_ms'].min())

# print(df.query("track_artist == 'Ricky Martin'")

pd.set_option('display.max_rows', None)

mean_val = df["duration_ms"].mean()

longer_tracks = df.query("duration_ms > mean_val")

print(longer_tracks)
