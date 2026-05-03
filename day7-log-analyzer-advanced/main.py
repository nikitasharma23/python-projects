LOGS = [
    "ERROR DISK FULL",
    "INFO STARTED",
    "ERROR FILE MISSING",
    "WARNING MEMORY LOW"
]

def count_log_types(logs):
    counts = {"ERROR": 0, "INFO": 0, "WARNING": 0}
    for log in logs:
        log_upper = log.upper()
        if log_upper.startswith("ERROR"):
            counts["ERROR"] += 1
        elif log_upper.startswith("INFO"):
            counts["INFO"] += 1
        elif log_upper.startswith("WARNING"):
            counts["WARNING"] += 1
    return counts

def find_most_frequent(counts):
    return max(counts, key=counts.get)

def get_logs_by_type(logs, log_type):
    return [log for log in logs if log.upper().startswith(log_type.upper())]

print("=" * 45)
print("           SIMPLE LOG ANALYZER")
print("=" * 45)

print("\n--- ALL LOGS ---")
for i, log in enumerate(LOGS, start=1):
    print(f"  [{i}] {log}")

counts = count_log_types(LOGS)

print("\n--- LOG TYPE COUNTS ---")
for log_type, count in counts.items():
    print(f"  {log_type:<10} : {count}")

most_frequent = find_most_frequent(counts)
print(f"\n--- MOST FREQUENT LOG TYPE ---")
print(f"  {most_frequent} ({counts[most_frequent]} occurrence/s)")

print("\n--- ERROR LOGS ---")
for e in get_logs_by_type(LOGS, "ERROR"):
    print(f"  [!] {e}")

print("\n--- WARNING LOGS ---")
for w in get_logs_by_type(LOGS, "WARNING"):
    print(f"  [~] {w}")

print("\n--- INFO LOGS ---")
for info in get_logs_by_type(LOGS, "INFO"):
    print(f"  [i] {info}")

print("\n" + "=" * 45)
print("          Analysis Complete!")
print("=" * 45)
