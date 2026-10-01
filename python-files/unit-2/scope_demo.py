count = 0

def tick_wrong():
    """Shadowing the global with a local variable."""
    count = 0
    count += 1
    return count

print(tick_wrong(), tick_wrong(), tick_wrong())

THRESHOLD = 70

def is_alert(value):
    """Read global constant."""
    return value > THRESHOLD

print(f"is_alert(85): {is_alert(85)}")
print(f"is_alert(60): {is_alert(60)}")

count = 0

def tick_with_global():
    """Uses global keyword to modify the global."""
    global count
    count += 1
    return count

print(tick_with_global(), tick_with_global(), tick_with_global())
print(f"Global count is now: {count}")

def make_ticker():
    """Returns a closure that maintains state without global."""
    count = [0]
    
    def tick():
        count[0] += 1
        return count[0]
    
    return tick

counter = make_ticker()
print(counter(), counter(), counter())
