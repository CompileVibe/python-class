robot_name = "alpha"
battery_pct = 78.5
is_docked = True
waypoints = 12

print(robot_name, battery_pct, is_docked, waypoints)
print(type(robot_name), type(battery_pct), type(is_docked), type(waypoints))

if battery_pct < 15:
    print("WARNING: Low battery!")
