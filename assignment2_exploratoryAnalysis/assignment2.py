import pandas as pd
import os
import matplotlib.pyplot as plt

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

#Created bar chart plot to visualize 
country_group = df.groupby("country")[order].agg(["mean", "sum"]).reset_index()
country_group = country_group.sort_values('mean', ascending=False)
plt.figure(figsize=(10,6))
plt.bar(country_group["country"], country_group["mean"], color='skyblue')
plt.title("Average Order Value by Country",fontsize=16)
plt.ylabel("Average Order Value (EUR)",fontsize=14)
plt.xlabel("Country",fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
#scatter plot to visualize the relationship between order value and cost
plt.figure(figsize=(8,6))
plt.scatter(df[order], df[cost], alpha=0.5, color="pink")
plt.title("Relationship between Order Value and Cost", fontsize=14)
plt.xlabel("Order Value (EUR)", fontsize=12)
plt.ylabel("Cost (EUR)", fontsize=12)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("order_vs_cost_scatter.png", dpi=300)
plt.show()
#Histogram
plt.figure(figsize=(8,6))
plt.hist(df[order], bins=25, alpha=0.7, color="purple")
plt.title("Distribution of Order Value", fontsize=14)
plt.xlabel("Order Value (EUR)", fontsize=12)
plt.ylabel("Number of Transactions", fontsize=12)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("order_value_hist.png", dpi=300)
plt.show()
#建议2：丹麦市场执行捆绑套餐促销，假设每笔丹麦订单金额提升20%，成本同步提升12%
denmark_df = df[df["country"] == "Denmark"].copy()
dk_avg_order_real = denmark_df[order].mean()
dk_avg_cost_real = denmark_df[cost].mean()
dk_gross_profit_real = (denmark_df[order] - denmark_df[cost]).mean()
denmark_df["sim_order_value"] = denmark_df[order] * 1.20
denmark_df["sim_cost"] = denmark_df[cost] * 1.12

dk_avg_order_sim = denmark_df["sim_order_value"].mean()
dk_avg_cost_sim = denmark_df["sim_cost"].mean()
dk_gross_profit_sim = (denmark_df["sim_order_value"] - denmark_df["sim_cost"]).mean()

print(f"【Denmark Real Baseline】")
print(f"Average order value: {dk_avg_order_real:.2f} EUR")
print(f"Average cost: {dk_avg_cost_real:.2f} EUR")
print(f"Average gross profit per order: {dk_gross_profit_real:.2f} EUR")

print(f"\n【After bundle offer simulation (+20% order value, +12% cost)】")
print(f"Simulated average order value: {dk_avg_order_sim:.2f} EUR")
print(f"Simulated average cost: {dk_avg_cost_sim:.2f} EUR")
print(f"Simulated average gross profit per order: {dk_gross_profit_sim:.2f} EUR")
profit_gain = dk_gross_profit_sim - dk_gross_profit_real
print(f"Average profit increase per Danish order: {profit_gain:.2f} EUR")

#建议3：对大额订单（order_value>200000 EUR）进行原料议价，大额订单成本降低8%；营收不变
print(f"\n=================================================")
large_orders_df = df[df[order] > 200000].copy()
lo_avg_order_real = large_orders_df[order].mean()
lo_avg_cost_real = large_orders_df[cost].mean()
lo_gross_profit_real = (large_orders_df[order] - large_orders_df[cost]).mean()
large_orders_df["sim_cost_negotiate"] = large_orders_df[cost] * 0.92

lo_avg_cost_sim = large_orders_df["sim_cost_negotiate"].mean()
lo_gross_profit_sim = (large_orders_df[order] - large_orders_df["sim_cost_negotiate"]).mean()
print(f"Large Orders(>200000EUR) Real Baseline")
print(f"Average order value: {lo_avg_order_real:.2f} EUR")
print(f"Average original cost: {lo_avg_cost_real:.2f} EUR")
print(f"Average gross profit per large order: {lo_gross_profit_real:.2f} EUR")

print(f"\n After raw material negotiation: cost -8%, revenue unchanged ")
print(f"Simulated average cost: {lo_avg_cost_sim:.2f} EUR")
print(f"Simulated average gross profit per large order: {lo_gross_profit_sim:.2f} EUR")
profit_gain_large = lo_gross_profit_sim - lo_gross_profit_real
print(f"Average profit gain per large size order: {profit_gain_large:.2f} EUR")
