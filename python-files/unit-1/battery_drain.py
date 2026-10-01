battery = 100
minutes = 0

while battery > 20:
    battery -= 7
    minutes += 1
    print(f"Minute {minutes}: Battery at {battery}%")

print(f"Low battery alert after {minutes} minutes")
