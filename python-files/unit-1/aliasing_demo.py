list1 = [1, 2, 3]
list2 = list1
list3 = list1.copy()

print("Original:")
print(f"list1: {list1}")
print(f"list2 (alias): {list2}")
print(f"list3 (copy): {list3}")

list1.append(4)
print("After list1.append(4):")
print(f"list1: {list1}")
print(f"list2 (alias): {list2}")
print(f"list3 (copy): {list3}")

print(f"list1 is list2: {list1 is list2}")
print(f"list1 is list3: {list1 is list3}")
