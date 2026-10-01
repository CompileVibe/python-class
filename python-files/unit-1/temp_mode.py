temp = float(input("Enter temperature (°C): "))

if temp < 0:
    mode = "HEATER ON"
elif temp < 40:
    mode = "NORMAL"
elif temp <= 60:
    mode = "COOLING ON"
else:
    mode = "SHUTDOWN"

print(f"Operating mode: {mode}")
