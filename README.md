# Basic Python code 
**1. Simple Bill Calculator**
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


**2. Restuarent Bil**l

    tea_count = 0
coffee_count = 0
pizza_count = 0
total = 0
amount = 0

print("Welcome to Talukdar's Restaurant!!!")
print("----------------------------------------------")

while True:
    ch = int(input(
        "Enter Your Choice:\n"
        "1) Biryani\n"
        "2) Special Biryani\n"
        "3) Special Mutton Biryani\n"
        "4) Exit\n"
    ))

    if ch == 1:
        print("Biryani Selected")
        tea_count += 1
        amount = amount + 90

    elif ch == 2:
        print("Special Biryani Selected")
        coffee_count += 1
        amount = amount + 160

    elif ch == 3:
        print("Special Masala Biryani Selected")
        pizza_count += 1
        amount = amount + 200

    elif ch == 4:
        print("Welcome to Rahman Restaurant!!!")
        print("Items\t\tCount\tItem")
        print("----------------------------------------------")
        print(f"Biryani\t\t{tea_count}\t90")
        print(f"Special Biryani\t{coffee_count}\t160")
        print(f"Special Masala Biryani\t{pizza_count}\t200")
        print("----------------------------------------------")

        total = tea_count + coffee_count + pizza_count
        print(f"Total\t\t{total}\t{amount}")
        print("----------------------------------------------")
        print("Bhaiya firse aao")
        break

    else:
        print("Enter Correct Choice")

**3. Traffic Signal Program**

def traffic_signal():
    print("Welcome to the Traffic Signal Simulation Program")
    print("------------------------------------------------")
    print("You can choose one of the following options:")
    print("1. red    -> Stop")
    print("2. green  -> Go")
    print("3. orange -> Ready")
    print("Type 'exit' to quit the program.")
    print("------------------------------------------------")

    while True:
        # Taking user input
        ch = input("Enter your choice (red/green/orange/exit): ").lower()

        # Decision making based on input
        if ch == "red":
            print("The signal is RED. Please stop your vehicle immediately.")
            print("Stopping ensures safety for pedestrians and other vehicles.")
            print("------------------------------------------------")
        elif ch == "green":
            print("The signal is GREEN. You may go ahead safely.")
            print("Always check both sides before moving forward.")
            print("------------------------------------------------")
        elif ch == "orange":
            print("The signal is ORANGE. Be ready to move, but proceed with caution.")
            print("Orange means the signal is about to change, so stay alert.")
            print("------------------------------------------------")
        elif ch == "exit":
            print("Exiting the Traffic Signal Simulation Program.")
            print("Thank you for using it. Drive safely!")
            break
        else:
            print("Invalid choice entered.")
            print("Please enter either 'red', 'green', 'orange', or 'exit'.")
            print("------------------------------------------------")

        
