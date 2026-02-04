# 1. Simple Bill Calculator

print("----- Electricity Bill Calculator -----")

try:
    units = int(input("Enter electricity units consumed: "))

    if units < 0:
        print("Units cannot be negative. Please enter a valid value.")
    else:
        bill = 0

        if units <= 100:
            bill = 0
        elif units <= 200:
            bill = (units - 100) * 5
        elif units <= 300:
            bill = (100 * 5) + (units - 200) * 7
        else:
            bill = (100 * 5) + (100 * 7) + (units - 300) * 10

        print("Units Consumed:", units)
        print("Total Electricity Bill: ₹", bill)

except ValueError:
    print("Invalid input! Please enter numeric units only.")


