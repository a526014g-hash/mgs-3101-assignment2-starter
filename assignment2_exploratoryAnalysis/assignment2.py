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

