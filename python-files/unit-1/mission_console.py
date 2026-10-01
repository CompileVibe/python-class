readings = []

while True:
    print("\n=== MISSION CONSOLE ===")
    print("1. Add sensor reading")
    print("2. Show report")
    print("3. Exit")
    
    choice = input("Choose: ").strip()
    
    if choice == '1':
        try:
            value = float(input("Enter reading value: "))
            readings.append(value)
            print(f"Reading added: {value}")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    elif choice == '2':
        if not readings:
            print("No readings yet!")
        else:
            average = sum(readings) / len(readings)
            alert_count = sum(1 for r in readings if r > 80)
            
            print("\n--- REPORT ---")
            print(f"Total readings: {len(readings)}")
            print(f"Average: {average:.2f}")
            print(f"Alerts (>80): {alert_count}")
            print(f"Min: {min(readings):.2f}, Max: {max(readings):.2f}")
    
    elif choice == '3':
        print("Exiting...")
        break
    
    else:
        print("Invalid choice.")
