# import pandas as pd
# import matplotlib.pyplot as plt

# Monday_df = pd.read_excel("Group task/monday_voucher_data.xlsx")
# Tuesday_df = pd.read_excel("Group task/tuesday_voucher_data.xlsx")
# Wednesday_df = pd.read_excel("Group task/wednesday_voucher_data.xlsx")
# Thursday_df = pd.read_excel("Group task/thursday_voucher_data.xlsx")
# Friday_df = pd.read_excel("Group task/friday_voucher_data.xlsx")
# Saturday_df = pd.read_excel("Group task/saturday_voucher_data.xlsx")
# Sunday_df = pd.read_excel("Group task/sunday_voucher_data.xlsx")

# df = pd.concat([Monday_df , Tuesday_df , Wednesday_df , Thursday_df , Friday_df , Saturday_df , Sunday_df], axis=0)


# df[df.select_dtypes(include='object').columns] = df.select_dtypes(include='object').apply(lambda col: col.str.upper())

# # # Continue with the rest of your code
# # df["New Transaction ID"] = range(1, len(df["Transaction ID"]) + 1)
# # df = df.drop(columns=["Transaction ID"])
# # df = df.set_index("New Transaction ID")
# # df = df.dropna(how="any")

# print(df)
 
# # # print(df)
 
# # df["New Transaction ID"] = range(1, len(df["Transaction ID"])+1)
# # print(df)
 
# df = df.drop(columns = ["Transaction ID"])
# df = df.set_index("New Transaction ID")
# df = df.dropna(how = "any")
# # print(df)
 
# def split_basket(string):
#     items = string.split(",")
#     stripped_items = [item.strip() for item in items]
#     return stripped_items
 
# df["Basket"] = df["Basket"].apply(split_basket)

 
# # print(df.head(5))
# # print(df.describe())
# # print(df.info())
 
# exploded_data_df = df.explode("Basket", ignore_index=False)
# # print(exploded_data_df["Basket"])
 
# df.to_excel("new_sales_excel.xlsx")
 
 
# ...................................................................................................................
# 1st Question:             How many sales were made on each payment type? Ticked
# ...................................................................................................................
 
# print(df["Payment Method"].value_counts())
 
# Payment Method
# DEBIT            165
# CASH             102
# CREDIT            67
# VOUCHER           33
# MOBILE WALLET     31
 
 
# ..................................................................................................................
# 2nd Question:          How many unique items were paid for by each payment type?
# ..................................................................................................................
 
# print(df["Total Items"].sum())  # 1514
# print(df.groupby("Payment Method")["Total Items"].sum())
 
# Payment Method
# CASH             395.0
# CREDIT           246.0
# DEBIT            650.0
# MOBILE WALLET     97.0
# VOUCHER          126.0
 
# # Counting each item by each payment method
# # Standardize 'Payment Method' values to title case for consistency
# df['Payment Method'] = df['Payment Method'].str.title()
 
# # Get all unique items across baskets
# unique_items = set(item for basket in df['Basket'] for item in basket)
 
# # Initialize an empty dictionary to store counts
# item_payment_counts = {}
 
# # Loop over each unique item and payment method
# for item in unique_items:
#     item_payment_counts[item] = {}
#     for method in df['Payment Method'].unique():
#         # Count orders that include the item and use the payment method
#         count = df[(df['Payment Method'] == method) &
#                      (df['Basket'].apply(lambda items: item in items))].shape[0]
#         item_payment_counts[item][method] = count
 
# # Display the results in a DataFrame for readability
# item_payment_counts_df = pd.DataFrame(item_payment_counts).T
# # print(item_payment_counts_df)
 
# Cash  Debit  Mobile Wallet  Credit  Voucher
# Croissant         8     11              3       3        1
# Muffin            4     14              1       2        2
# Tea              42     74              8      30       12
# Stroopwafel       6     12              2       1        1
# Toast             6     10              0       3        1
# Hot Chocolate    45     69             17      33       15
# Latte            48     66             11      30       18
# Buttered Roll     7     12              2       4        2
# Panini            3      9              2       2        1
# Cappuccino       47     70              8      35       18
# Mocha            44     80              9      21       20
# Gift Voucher      0      7              1       3        0
# Americano        46     66             13      24       10
 
 
# .................................................................................................................
# 3rd Question:        What percentage of income made came from vouchers?
# .................................................................................................................
 
# print(df.groupby("Payment Method")["Cost"].sum())
# Payment Method
# Cash              684.2
# Credit            519.5
# Debit            1237.8
# Mobile Wallet     198.4
# Voucher           228.7
 
 
# Group by 'Payment Method' and calculate total income per method
# income_by_payment = df.groupby('Payment Method')['Cost'].sum()
 
# # Plot the pie chart
# plt.figure(figsize=(8, 8))
# plt.pie(income_by_payment, labels=income_by_payment.index, autopct='%1.1f%%', startangle=140)
# plt.title("Percentage of Income by Payment Method")
# plt.show()
 
 
# 33 vouchers per week make the income 228.7 £.
# We bought them for 33 * 0.91 to 33 * 2 (30 to 66) £. +25/3 >>>> 38 to 74 £
# So they worth it.
# 1051 for the software x * (228.7 - 56) = 1051 >>>>>> after 6 weeks, using VOUCHERS can benefit the store.

import pandas as pd
import matplotlib.pyplot as plt

# Load all daily data files
Monday_df = pd.read_excel("Group task/monday_voucher_data.xlsx")
Tuesday_df = pd.read_excel("Group task/tuesday_voucher_data.xlsx")
Wednesday_df = pd.read_excel("Group task/wednesday_voucher_data.xlsx")
Thursday_df = pd.read_excel("Group task/thursday_voucher_data.xlsx")
Friday_df = pd.read_excel("Group task/friday_voucher_data.xlsx")
Saturday_df = pd.read_excel("Group task/saturday_voucher_data.xlsx")
Sunday_df = pd.read_excel("Group task/sunday_voucher_data.xlsx")

# Concatenate the dataframes for all days of the week
df = pd.concat([Monday_df, Tuesday_df, Wednesday_df, Thursday_df, Friday_df, Saturday_df, Sunday_df], axis=0)

# Clean up string columns by making them uppercase
df[df.select_dtypes(include='object').columns] = df.select_dtypes(include='object').apply(lambda col: col.str.upper())

# Calculate the total unique items paid for by each payment method
unique_items_per_payment = df.groupby("Payment Method")["Total Items"].sum()

# # Ensure total_unique_items is calculated correctly
# total_unique_items = unique_items_per_payment.sum() if not unique_items_per_payment.empty else 0

# # Define a color palette that provides good contrast with white text
# custom_colors = ['#3498db', '#e74c3c', '#2ecc71', '#9b59b6', '#f39c12', '#1abc9c', '#34495e']

# # Plot the bar chart with custom colors
# plt.figure(figsize=(10, 6))
# bars = plt.bar(unique_items_per_payment.index, unique_items_per_payment.values, color=custom_colors[:len(unique_items_per_payment)])

# # Add a title and labels
# plt.title("Total Unique Items Paid by Each Payment Type", fontsize=16)
# plt.xlabel("Payment Method", fontsize=12)
# plt.ylabel("Total Unique Items", fontsize=12)
# plt.xticks(rotation=45)

# # Add numbers and percentages inside the bars with percentages on a new line
# for bar, value in zip(bars, unique_items_per_payment.values):
#     yval = bar.get_height()
#     if total_unique_items > 0:  # Only calculate percentage if the total is greater than zero
#         percentage = (value / total_unique_items) * 100
#         plt.text(
#             bar.get_x() + bar.get_width() / 2, 
#             yval - 10, 
#             f"{int(value)}\n({percentage:.1f}%)",  # Separate number and percentage with a newline
#             ha='center', 
#             va='top', 
#             color='white', 
#             fontweight='bold'
#         )

# plt.tight_layout()
# plt.show()



import pandas as pd
import matplotlib.pyplot as plt

# # Assuming df is already loaded and cleaned as in your previous example

# # Calculate the count of sales by payment method
# sales_by_payment_method = df["Payment Method"].value_counts()

# # Calculate the total number of sales for percentage calculation
# total_sales = sales_by_payment_method.sum()

# # Define a consistent color palette
# custom_colors = ['#3498db', '#e74c3c', '#2ecc71', '#9b59b6', '#f39c12', '#1abc9c', '#34495e']

# # Plot the bar chart
# plt.figure(figsize=(10, 6))
# bars = plt.bar(sales_by_payment_method.index, sales_by_payment_method.values, color=custom_colors[:len(sales_by_payment_method)])

# # Add title and labels
# plt.title("Number of Sales by Payment Type", fontsize=16)
# plt.xlabel("Payment Method", fontsize=12)
# plt.ylabel("Number of Sales", fontsize=12)
# plt.xticks(rotation=45)

# # Add numbers and percentages on top of each bar
# for bar, value in zip(bars, sales_by_payment_method.values):
#     # Calculate the percentage of each payment type
#     percentage = (value / total_sales) * 100
#     plt.text(
#         bar.get_x() + bar.get_width() / 2, 
#         bar.get_height() - 5,  # Adjust position slightly for the text
#         f"{int(value)}\n({percentage:.1f}%)",  # Display count and percentage on separate lines
#         ha='center', 
#         va='top', 
#         color='white', 
#         fontweight='bold'
#     )

# plt.tight_layout()
# plt.show()

average_spend_per_payment = df.groupby("Payment Method")["Cost"].mean()

# Plot bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(average_spend_per_payment.index, average_spend_per_payment.values, color=custom_colors[:len(average_spend_per_payment)])
plt.title("Average Spend Per Transaction by Payment Type")
plt.xlabel("Payment Method")
plt.ylabel("Average Spend (£)")
plt.xticks(rotation=45)

# Add values on bars
for bar, value in zip(bars, average_spend_per_payment.values):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 0.5, f"£{value:.2f}", ha='center', va='top', color='white', fontweight='bold')

plt.tight_layout()
plt.show()