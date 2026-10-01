"""Sensor module with readings and alerts."""

THRESHOLD = 75.0

def average(readings):
    """Return the average of readings."""
    if not readings:
        return 0
    return sum(readings) / len(readings)

def is_alert(value):
    """Return True if value exceeds threshold."""
    return value > THRESHOLD

if __name__ == "__main__":
    readings = [62, 84, 71, 88, 65]
    print(f"Readings: {readings}")
    print(f"Average: {average(readings):.1f}")
    print(f"Threshold: {THRESHOLD}")
    for r in readings:
        status = "ALERT" if is_alert(r) else "OK"
        print(f"  {r} --> {status}")
