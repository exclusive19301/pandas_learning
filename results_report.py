import pandas as pd

# Load the data
df = pd.read_excel('group_results.xlsx')

# Calculate average download and upload speeds
mean_download_speed = df['Mean Download'].mean()
mean_upload_speed = df['Mean Upload'].mean()

# Calculate median download and upload speeds
median_download_speed = df['Median Download'].median()
median_upload_speed = df['Median Upload'].median()

# Get the most common ISPs (mode)
mode_isp = df['Internet Service Provider'].mode()[0]

# Compare with UK national averages
national_download_median = 69.4
national_upload_median = 18.4

download_comparison = mean_download_speed - national_download_median
upload_comparison = mean_upload_speed - national_upload_median

# Output results
print(f"Mean download speed for the cohort: {mean_download_speed:.2f} Mbps")
print(f"Mean upload speed for the cohort: {mean_upload_speed:.2f} Mbps")
print(f"Median download speed for the cohort: {median_download_speed:.2f} Mbps")
print(f"Median upload speed for the cohort: {median_upload_speed:.2f} Mbps")

print(f"Most common provider in the cohort: {mode_isp}")
print(f"Difference between cohort's mean download and national: {download_comparison:.2f} Mbps")
print(f"Difference between cohort's mean upload and national: {upload_comparison:.2f} Mbps")

# Count the occurrences of each ISP and rank them
isp_ranking = df['Internet Service Provider'].value_counts()

# Output the ranking
print("Ranking of most common providers in the cohort:")
print(isp_ranking)