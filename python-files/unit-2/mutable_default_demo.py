def add_waypoint_wrong(wp, route=[]):
    """Add waypoint to route."""
    route.append(wp)
    return route

r1 = add_waypoint_wrong((0, 0))
r2 = add_waypoint_wrong((5, 5))
print("TRAP:")
print(f"r1: {r1}")
print(f"r2: {r2}")
print(f"r1 is r2: {r1 is r2}")

print()

def add_waypoint(wp, route=None):
    """Add waypoint to route."""
    if route is None:
        route = []
    route.append(wp)
    return route

r1 = add_waypoint((0, 0))
r2 = add_waypoint((5, 5))
print("FIXED:")
print(f"r1: {r1}")
print(f"r2: {r2}")
print(f"r1 is r2: {r1 is r2}")
