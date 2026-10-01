location = (10, 20)
x, y = location
print(f"Location: ({x}, {y})")

single = (42,)
print(f"Single element tuple: {single}, type: {type(single)}")

visited = [1, 2, 3, 2, 4, 1, 5]
print(f"Visited (with duplicates): {visited}")

unique_visited = set(visited)
print(f"Unique visited (as set): {unique_visited}")
print(f"Unique visited (as sorted list): {sorted(unique_visited)}")
