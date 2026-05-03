import matplotlib.pyplot as plt

DATES = ["MON", "TUE", "WED", "THU", "FRI"]
SALES = [200, 250, 300, 280, 350]

highest_idx = SALES.index(max(SALES))
lowest_idx  = SALES.index(min(SALES))

plt.figure(figsize=(8, 5))
plt.plot(DATES, SALES, marker="o", color="steelblue", linewidth=2, label="Daily Sales")

plt.scatter(DATES[highest_idx], SALES[highest_idx], color="green", s=120, zorder=5, label=f"Highest: {max(SALES)}")
plt.scatter(DATES[lowest_idx],  SALES[lowest_idx],  color="red",   s=120, zorder=5, label=f"Lowest: {min(SALES)}")

plt.annotate(f"High: {max(SALES)}", xy=(DATES[highest_idx], SALES[highest_idx]), xytext=(highest_idx - 0.3, SALES[highest_idx] + 15), fontsize=9, color="green")
plt.annotate(f"Low: {min(SALES)}",  xy=(DATES[lowest_idx],  SALES[lowest_idx]),  xytext=(lowest_idx  + 0.1, SALES[lowest_idx]  - 25), fontsize=9, color="red")

plt.title("Weekly Sales Trend", fontsize=14, fontweight="bold")
plt.xlabel("Day of the Week")
plt.ylabel("Sales")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("sales_trend.png")
plt.show()

print("=" * 45)
print("       SALES TREND VISUALIZATION")
print("=" * 45)
print(f"\n  Days  : {DATES}")
print(f"  Sales : {SALES}")
print(f"\n  Highest Sale : {max(SALES)} on {DATES[highest_idx]}")
print(f"  Lowest Sale  : {min(SALES)} on {DATES[lowest_idx]}")
print("\n  [✓] Chart saved as sales_trend.png")
print("\n" + "=" * 45)
