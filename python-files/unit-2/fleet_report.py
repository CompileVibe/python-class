def battery_band(pct):
    """Return CRITICAL, LOW or OK for a battery percentage."""
    if pct < 15:
        return "CRITICAL"
    elif pct < 30:
        return "LOW"
    return "OK"

fleet = {"Alpha": 8, "Beta": 22, "Gamma": 76}
for name, pct in fleet.items():
    print(f"{name}: {battery_band(pct)}")
