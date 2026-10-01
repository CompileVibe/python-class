cap = float(input("Enter battery capacity (mAh): "))
draw = float(input("Enter current draw (mA): "))
hours = cap / draw
print(f"Estimated runtime: {hours:.2f} hours")
