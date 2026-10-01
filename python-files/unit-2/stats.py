def get_stats(values):
    """Return mean, minimum, maximum as a tuple."""
    mean = sum(values) / len(values)
    return mean, min(values), max(values)

readings = [22.5, 23.1, 21.8, 24.0, 22.9]
mean, lo, hi = get_stats(readings)
print(f"Mean: {mean:.2f}, Min: {lo:.2f}, Max: {hi:.2f}")

def append_reading(data, value):
    """Mutates the caller's list by appending."""
    data.append(value)

def rebind_list(data):
    """Does not mutate - rebinds the local variable."""
    data = [99, 100]

original = [10, 20]
print(f"Original: {original}")

append_reading(original, 30)
print(f"After append: {original}")

rebind_list(original)
print(f"After rebind: {original}")
