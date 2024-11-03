import pandas as pd

df = pd.read_excel("first_hour_sales.xlsx")

df = df.set_index("Transaction ID")

# dropping columns see both methods

# df = df.drop( "Till ID", axis=1)
# 2 # OR
# 3 df = df. drop(columns=["Till ID" ] )

df = df.drop(columns=["Till ID"])

# print(df.info())

# NaN stands for "not a
# number."

# It is an undefined
# number.

# If a system is asked to
# do something
# mathematically
# impossible, it may return
# NaN.

# How to remove NaNs - 

# Our rows with NaN in are
# voids or till checks - but
# they record that we sold
# three items each time.

# This will impact our
# statistics and we should
# remove them.

# We can use the drop()
# method to remove rows.

# We target them via the
# index.
# Basically - this is how you drop individual rows to go in and target stuff specifically.
df = df.drop( [6.0])

# The .dropna() method allows us to drop NULL values
# like NaN. It can be used to get rid of many rows quickly.

# The how argument specifies how strict is should be.
# Do all the values in the row need to be NaN, or just any
# value?

# Alex Arditti is explaining how to use the dropna() method in pandas to efficiently remove rows containing missing values (NaN) from a dataset. 
# He notes that manually removing rows with missing data could be time-consuming if the dataset is large. 
# The dropna() method allows for quick removal of these rows by specifying the how argument, 
# which determines how strictly rows should be dropped. If how='all' is used, only rows where all values are NaN will be dropped. If how='any' is used,
#  rows with any NaN values will be removed. This method helps clean up the dataset without manually checking each row.
# So basically, this just lets you drop rows that have invalid data in them, saves time over dropping individual rows one by one.
df = df.dropna(how="any" )
# This shows if there are any dupes in the set and where.
print(df[df.duplicated()])
# This automatically drops any duplicates
df = df.drop_duplicates()
print(df)

# Outliers

# To change this single
# cell, we can use the .at
# property, and reassign
# the value.

df.at[15.0, "Cost"] = 6.00
print(df)

# The .at property take
# the arguments in the
# order [ row, column ]

def float_to_time(time_record):
    # Convert the float into a string
    time_record = str(time_record)
    # Split the input string at the decimal point
    hours, minutes = time_record.split('.')
    # Format the hours and minutes into HH:MM
    timestamp = f"{int(hours):02}:{int(minutes):02}"
    return timestamp

df [ "Time" ] = df [ "Time" ].apply(float_to_time)

df ["Time"] = pd.to_datetime(df["Time"])

print(df.info())

print(df)

# float_to_time(8.32)

# df [ "Time" ] = df [ "Time" ].apply(float_to_time)

# We need to update the "Time" column to the
# re-formatted values.
# .apply() will run the function against every value.
# What do you notice about float_to_time?

def split_basket(string):
    items = string.split(",")
    stripped_items = [item.strip() for item in items]
    return stripped_items

df ["Basket" ] = df ["Basket" ].apply(split_basket)
print(df["Basket"])

exploded_data = df.explode("Basket", ignore_index=False)
print(exploded_data["Basket"])

# Prevention

# Data will come from many sources and will likely be
# inconsistent.

# There is nothing you can do to if you are not the data
# collector to reduce the amount of cleaning you need to
# do.

# If you are in control of how the data is collected,
# consider restricting certain aspects.

# Ensure the data coming in is the data you expect to
# work with.

# Free text boxes are not as useful as you may think!

# Drop down menus, tick
# boxes, casting,
# methods like .strip(),
# .capitalize(), and
# validation will help
# clean the data at point
# of entry, making the
# cleaning much easier in
# the long run!

# If you are in control of how the data is collected,
# consider restricting certain aspects.

# Ensure the data coming in is the data you expect to
# work with.

# Free text boxes are not as useful as you may think!

# Learning Objectives

# Recording has started.

# To be able to perform basic cleaning on data
# To be able to isolate relevant data to work with

# To recognise the issues with outliers

# Activity 1

# Now your data is clean, find out:

# The average price of an item
# The average basket price
# The maximum spend in one
# transaction
# The minimum spend in one
# transaction
# The most common spend
# amount

# The most common payment type

# Activity 2

# Download
# cleaning_activity.xlsx
# from Teams.

# Ensure this data is clean
# and accurate.

exploded_data = df.explode("Basket", ignore_index=False)

total_cost = exploded_data['Cost'].sum()

total_items = exploded_data['Basket'].count()

average_price_per_item = total_cost / total_items

print(f"Average price per item: £{average_price_per_item:.2f}")

# Average basket price

average_basket_price = df['Cost'].mean()

print(f"Average basket price: £{average_basket_price:.2f}")

# # Max spend in a transaction

# max_spend = df['Cost'].max()

# print(f"Maximum spend in one transaction: £{max_spend:.2f}")

# # Common spend amount

most_common_spend = df['Cost'].mode()[0]

print(f"Most common spend amount: £{most_common_spend:.2f}")

# # Most common payment type

# most_common_payment_type = df['Payment Method'].mode()[0]

# print(f"Most common payment type: {most_common_payment_type}")


# import pandas as pd


# df = pd.read_excel("cleaning_activity.xlsx")


# df = df.set_index("Transaction ID")


# df = df.drop(columns=["Till ID"])

# df = df.dropna(how="any")

# df = df.drop_duplicates()


# df.at[56.0, "Cost"] = 6.00

# exploded_data = df.explode("Basket", ignore_index=False)

# print(exploded_data.head())


# total_cost = exploded_data['Cost'].sum()
# total_items = exploded_data['Basket'].count()
# average_price_per_item = total_cost / total_items
# print(f"Average price per item: £{average_price_per_item:.2f}")


# average_basket_price = df['Cost'].mean()
# print(f"Average basket price: £{average_basket_price:.2f}")


# max_spend = df['Cost'].max()
# print(f"Maximum spend in one transaction: £{max_spend:.2f}")


# min_spend = df['Cost'].min()
# print(f"Minimum spend in one transaction: £{min_spend:.2f}")


# most_common_spend = df['Cost'].mode()[0]
# print(f"Most common spend amount: £{most_common_spend:.2f}")


# most_common_payment_type = df['Payment Method'].mode()[0]
# print(f"Most common payment type: {most_common_payment_type}")