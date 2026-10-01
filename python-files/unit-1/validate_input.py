while True:
    value = int(input("Enter a value between 0 and 100: "))
    if 0 <= value <= 100:
        print(f"Valid! You entered {value}")
        break
    else:
        print("Invalid! Please try again.")
