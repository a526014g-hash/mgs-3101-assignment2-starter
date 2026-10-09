import pandas as pd
import os

# Load dataset 
script_dir = os.path.dirname(__file__)
csv_path = os.path.join(script_dir, "../data/Sales-Export_2019-2020.csv")
df = pd.read_csv(csv_path, thousands=",")

# (rows, columns)
print("==== Dataset Shape ====")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# Show column data types
print("\n==== Column Data Types ====")
print(df.dtypes)

print(df.head())
# check for and report missing values in each column
print(df.isnull().sum())

# Calculate descriptive statistics for at least two numeric columns
numeric_df = df.select_dtypes(include=["int64", "float64"])
print(numeric_df.describe())

# Groups the data by at least one categorical column and summarizes a numeric column 
print("\n==== All Column Names ====")
print(df.columns)
#1 Groups the data by countryand summarizes numeric columns
group_result = df.groupby("country")[[" order_value_EUR ", " cost "]].agg(["mean", "sum"])
print(group_result)

# Identifies the single highest and single lowest value for a numeric column of your choice, along with the row(s) they belong to
#highest and lowest order_value_EUR
order = " order_value_EUR "
max_order_val = df[order].max()
min_order_val = df[order].min()
print(f"Highest order_value_EUR: {max_order_val:.2f}")
print(f"Lowest order_value_EUR: {min_order_val:.2f}")
print("\nRow with maximum order_value_EUR:")
print(df.loc[df[order].idxmax()])
print("\nRow with minimum order_value_EUR:")
print(df.loc[df[order].idxmin()])

#highest and lowest cost
cost = " cost "
max_cost_val = df[cost].max()
min_cost_val = df[cost].min()
print(f"Highest cost: {max_cost_val:.2f}")
print(f"Lowest cost: {min_cost_val:.2f}")
print("\nRow with maximum cost:")
print(df.loc[df[cost].idxmax()])
print("\nRow with minimum cost:")
print(df.loc[df[cost].idxmin()])

#Use if/else statement to check if average order value meets the predefined threshold
target_avg_order = 110000
avg_order_value = df[order].mean()
total_revenue = df[order].sum()
avg_cost = df[cost].mean()



print(f"Average Order Value: {avg_order_value:.2f} EUR")
print(f"Total Revenue: {total_revenue:,.2f} EUR")
print(f"Average Cost: {avg_cost:.2f} EUR")

if avg_order_value >= target_avg_order:
    print(f"The average order value ({avg_order_value:.2f} EUR) meets thetarget threshold of {target_avg_order} EUR.")
else:
    print(f"The average order value ({avg_order_value:.2f} EUR) does not meet the target threshold of {target_avg_order} EUR.")

