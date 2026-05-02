data = [10, None, 20, 10, "", 30, None, 40]

clean_list = []
removed_count = 0

for item in data:
    if item is None or item == "":
        removed_count += 1
        continue

    if item not in clean_list:
        clean_list.append(item)
    else:
        removed_count += 1

clean_list.sort()

print("Original List:", data)
print("Clean List:", clean_list)
print("Removed Values:", removed_count)