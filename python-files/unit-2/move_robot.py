def move_robot(x, y, speed=1.0):
    """Move robot to coordinates at given speed."""
    print(f"moving to ({x}, {y}) at {speed} m/s")

move_robot(3, 4)
move_robot(3, 4, 0.5)
move_robot(y=4, x=3)
move_robot(3, speed=2.0, y=4)

def log(*values):
    """Log multiple values as a tuple."""
    print(f"Logged: {values}")

log("start")
log("waypoint", 1, 2, 3)

def config(**options):
    """Configure with keyword arguments as dictionary."""
    print(f"Config: {options}")

config(speed=2.0, timeout=30, debug=True)
