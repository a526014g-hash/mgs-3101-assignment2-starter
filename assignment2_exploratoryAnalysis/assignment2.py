import pandas as pd
import os

# Load dataset 
script_dir = os.path.dirname(__file__)
csv_path = os.path.join(script_dir, "../data/Sales-Export_2019-2020.csv")
df = pd.read_csv(csv_path)

# (rows, columns)
print("==== Dataset Shape ====")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# Show column data types
print("\n==== Column Data Types ====")
print(df.dtypes)
