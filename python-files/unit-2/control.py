"""Control module that imports from sensors within the package."""

from . import sensors

def safe_move():
    """Only move if temperature is safe."""
    temp = sensors.read_temperature(1)
    battery = sensors.read_battery(1)
    
    if sensors.is_critical_temp(temp):
        return "Temperature too high - cannot move"
    
    if battery < 20:
        return "Battery low - cannot move"
    
    return "OK to move"

if __name__ == "__main__":
    print(f"Robot status: {safe_move()}")
