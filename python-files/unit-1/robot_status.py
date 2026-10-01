status = {}

status['name'] = 'Alpha'
status['battery'] = 78.5
status['docked'] = True
print("Initial status:", status)

location = status.get('location', 'Unknown')
print(f"Location: {location}")

status['battery'] = 65
print(f"After update: {status}")

sensor_readings = ['temp', 'humidity', 'temp', 'battery', 'humidity', 'temp']
count = {}
for reading in sensor_readings:
    count[reading] = count.get(reading, 0) + 1

print("Sensor reading counts:")
for sensor, freq in count.items():
    print(f"  {sensor}: {freq}")
