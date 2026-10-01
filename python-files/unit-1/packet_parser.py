data = "T:25.4;H:60;B:78"

print("Original:", data)
print("First 5 chars:", data[:5])
print("After colon:", data[2:6])

parts = data.split(";")
for part in parts:
    key, value = part.split(":")
    print(f"{key} = {value}")

print("Upper:", data.upper())
print("Replace:", data.replace("T", "TEMP"))
print("Find:", data.find(";"))
