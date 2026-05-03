import pandas as pd

data = {
    "NAME":   ["AMIT", "RIYA", "JOHN", "SARA", "RAHUL"],
    "AGE":    [25, 32, 28, 22, 35],
    "SALARY": [60000, 45000, 75000, 55000, 40000]
}

df = pd.DataFrame(data)

high_salary = df[df["SALARY"] > 50000]
young = df[df["AGE"] < 30]
combined = df[(df["SALARY"] > 50000) & (df["AGE"] < 30)]

high_salary.to_csv("high_salary.csv", index=False)
young.to_csv("young_employees.csv", index=False)
combined.to_csv("filtered_result.csv", index=False)

print("=" * 45)
print("         DATA FILTERING TOOL")
print("=" * 45)

print("\n--- FULL DATASET ---")
print(df.to_string(index=False))

print("\n--- SALARY > 50000 ---")
print(high_salary.to_string(index=False))

print("\n--- AGE < 30 ---")
print(young.to_string(index=False))

print("\n--- SALARY > 50000 AND AGE < 30 ---")
print(combined.to_string(index=False))

print("\n[✓] Filtered data saved to CSV files.")
print("\n" + "=" * 45)
print("          Filtering Complete!")
print("=" * 45)
