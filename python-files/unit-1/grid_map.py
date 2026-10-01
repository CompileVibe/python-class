grid = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 1]
]

obstacle_count = 0
for row in grid:
    for cell in row:
        if cell == 1:
            obstacle_count += 1
            print("#", end=" ")
        else:
            print(".", end=" ")
    print()

print(f"\nTotal obstacles: {obstacle_count}")
