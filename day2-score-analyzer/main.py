MARKS = [78, 85, 90, 67, 85, 92, 78]

def calculate_average(marks):
    return sum(marks) / len(marks)

def calculate_highest(marks):
    return max(marks)

def calculate_lowest(marks):
    return min(marks)

def count_above_average(marks, average):
    count = 0
    for score in marks:
        if score > average:
            count += 1
    return count

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "FAIL"

def grade_distribution(marks):
    distribution = {"A": 0, "B": 0, "C": 0, "FAIL": 0}
    for score in marks:
        grade = get_grade(score)
        distribution[grade] += 1
    return distribution


print("=" * 45)
print("       STUDENT SCORE ANALYZER")
print("=" * 45)

print(f"\nMarks List : {MARKS}")
print(f"Total Students : {len(MARKS)}")

average   = calculate_average(MARKS)
highest   = calculate_highest(MARKS)
lowest    = calculate_lowest(MARKS)
above_avg = count_above_average(MARKS, average)

print("\n--- STATISTICS ---")
print(f"Average Score          : {average:.2f}")
print(f"Highest Score          : {highest}")
print(f"Lowest Score           : {lowest}")
print(f"Students Above Average : {above_avg}")

print("\n--- GRADE DISTRIBUTION ---")
dist = grade_distribution(MARKS)
for grade, count in dist.items():
    print(f"  Grade {grade:>4} : {count} student(s)")

print("\n--- INDIVIDUAL GRADES ---")
for i, score in enumerate(MARKS, start=1):
    grade = get_grade(score)
    print(f"  Student {i} | Score: {score} | Grade: {grade}")

print("\n" + "=" * 45)
print("        Analysis Complete!")
print("=" * 45)
