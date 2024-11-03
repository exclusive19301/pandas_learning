import pandas as pd

df = pd.read_excel("results2024-10-24-1533.xlsx")

print(df)
#Here i am getting the mean of the upload + download speed
print(df['Download (Mb/s)'].mean())
print(df['Upload (Mb/s)'].mean())
# Here i am getting the median of the upload + download speed
print(df['Download (Mb/s)'].median())
print(df['Upload (Mb/s)'].median())

# 1. I am sorting the values by fastest upload speed

print(df.sort_values(by='Upload (Mb/s)', ascending=False))

# 2. I am sorting the values by slowest upload speed

print(df.sort_values(by='Upload (Mb/s)', ascending=True))

# 2. I am sorting the values by fastest download speed

print(df.sort_values(by='Download (Mb/s)', ascending=False))

# I am sorting the dataframe by the download speeds in ascending order 

print(df.sort_values(by='Download (Mb/s)', ascending=True))

# Here I am calculating the mean download speed

mean_download_speed = df['Download (Mb/s)'].mean()

# and below i am filtering the dataframe to create a new dataframe which includes only the rows where the download speed is greater than the mean.

faster_than_mean = df[df['Download (Mb/s)'] > mean_download_speed]

# and finally below i am printing the filtered data frame

print(f"Mean download speed: {mean_download_speed:.2f} Mbps")
print("Download speeds faster than the mean:")
print(faster_than_mean[['Date-time', 'Download (Mb/s)']])