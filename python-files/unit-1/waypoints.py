waypoints = [1, 2, 3]

print("Original:", waypoints)
print("Length:", len(waypoints))

waypoints.append(4)
print("After append:", waypoints)

waypoints.insert(1, 1.5)
print("After insert:", waypoints)

waypoints.remove(1.5)
print("After remove:", waypoints)

numbers = [3, 1, 4, 1, 5]
print("Sorted:", sorted(numbers))
