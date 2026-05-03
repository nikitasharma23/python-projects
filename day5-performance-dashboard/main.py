import pandas as pd

data = {
    "NAME":    ["AMIT", "RIYA", "JOHN"],
    "MATH":    [80, 90, 60],
    "SCIENCE": [70, 88, 65],
    "ENGLISH": [85, 92, 70]
}

df = pd.DataFrame(data)

df["AVERAGE"] = df[["MATH", "SCIENCE", "ENGLISH"]].mean(axis=1).round(2)

def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    else:
        return "FAIL"

df["GRADE"] = df["AVERAGE"].apply(get_grade)

overall_avg = df["AVERAGE"].mean().round(2)
topper = df.loc[df["AVERAGE"].idxmax(), "NAME"]
above_avg_count = len(df[df["AVERAGE"] > overall_avg])

subject_avg = df[["MATH", "SCIENCE", "ENGLISH"]].mean().round(2)

print("=" * 55)
print("        STUDENT PERFORMANCE DASHBOARD")
print("=" * 55)

print("\n--- FULL REPORT ---")
print(df.to_string(index=False))

print("\n--- STATISTICS ---")
print(f"  Overall Average        : {overall_avg}")
print(f"  Topper                 : {topper}")
print(f"  Students Above Average : {above_avg_count}")

print("\n--- SUBJECT-WISE AVERAGE ---")
for subject, avg in subject_avg.items():
    print(f"  {subject:<10} : {avg}")

print("\n" + "=" * 55)
print("           Analysis Complete!")
print("=" * 55)