import pandas as pd

# group results loaded into pandas
df = pd.read_excel('group_results.xlsx')

# cleaning data here by dropping any NaN values.
df = df.drop(columns=["Package (if known)"], errors='ignore')
df = df.dropna(how="any")

# Here i am calculating mean median and mode for download and upload speeds
mean_download = df['Mean Download'].mean()
median_download = df['Median Download'].median()
fastest_download = df['Fastest Download'].max()
slowest_download = df['Slowest Download'].min()

mean_upload = df['Mean Upload'].mean()
median_upload = df['Median Upload'].median()
fastest_upload = df['Fastest Upload'].max()
slowest_upload = df['Slowest Upload'].min()

# I am using mode to calculate the most common internet service providers
mode_service_provider = df['Internet Service Provider'].mode()

# I have coded the national average speeds which I sourced from ofcom.
national_median_download = 69.4
national_median_upload = 18.4

# These are comparison strings compareing the cohorts mean, median and national averages.

download_comparison = f"Mean download speed: {mean_download:.2f}, Median download speed: {median_download:.2f}, National median download speed: {national_median_download:.2f}"
upload_comparison = f"Mean upload speed: {mean_upload:.2f}, Median upload speed: {median_upload:.2f}, National median upload speed: {national_median_upload:.2f}"

# Here I am filtering rows that the download speed is faster than the mean.
faster_than_mean_download = df[df['Mean Download'] > mean_download]['Mean Download']

# I am sorting by fastest and slowest upload speeds.
sorted_by_fastest_upload = df.sort_values(by='Fastest Upload', ascending=False)
sorted_by_slowest_upload = df.sort_values(by='Fastest Upload', ascending=True)

# Here I am using a series of F strings to report all of my findings into the console which I will then use in my powerpoint.
print(f"Fastest Download: {fastest_download:.2f} Mb/s")
print(f"Slowest Download: {slowest_download:.2f} Mb/s")
print(f"Mean Download: {mean_download:.2f} Mb/s")
print(f"Median Download: {median_download:.2f} Mb/s")
print(f"Fastest Upload: {fastest_upload:.2f} Mb/s")
print(f"Slowest Upload: {slowest_upload:.2f} Mb/s")
print(f"Mean Upload: {mean_upload:.2f} Mb/s")
print(f"Median Upload: {median_upload:.2f} Mb/s")
print(f"Comparison with national averages:\n{download_comparison}\n{upload_comparison}")
print(f"Most Common Service Providers: {mode_service_provider.tolist()}")
print(f"Download speeds faster than the mean: \n{faster_than_mean_download}")

# here i am exporting into an excel sheet
sorted_by_fastest_upload.to_excel("sorted_by_fastest_upload.xlsx", index=False)
sorted_by_slowest_upload.to_excel("sorted_by_slowest_upload.xlsx", index=False)
