# Basic Python code 
This are the basic code for Learning the basic function of class and identifiers of the java script
By this codes we will get the practical knowledge of the java script


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


# 2. Restuarent Bill

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



# 3. Traffic Signal Program

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



# 4. Storing Details of a student in a registration form


print("----- Student Registration Form -----")

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
age = input("Enter Age: ")
gender = input("Enter Gender: ")
course = input("Enter Course Name: ")
mobile = input("Enter Mobile Number: ")

print("\n----- Student Details -----")
print("Name      :", name)
print("Roll No   :", roll_no)
print("Age       :", age)
print("Gender    :", gender)
print("Course    :", course)
print("Mobile No :", mobile)

print("\nRegistration Successful")



# 5 Basic code of python to gerate student marksheet

print(-----Students Marksheet-----)
name = input("Name: ")
dep = input("Department: ")
yr = input("Year: ")
sem = input("Semester: ")
sec = input("Section: ")
roll = input("Roll Number: ")

s1 = float(input("Enter marks for subject 1: "))
s2 = float(input("Enter marks for subject 2: "))
s3 = float(input("Enter marks for subject 3: "))
s4 = float(input("Enter marks for subject 4: "))
s5 = float(input("Enter marks for subject 5: "))

print("STUDENT MARKSHEET")
print("Name:", name)
print("Department:", dep)
print("Year:", yr)
print("Semester:", sem)
print("Section:", sec)
print("Roll Number:", roll)

print("Subject 1 Marks:", s1)
print("Subject 2 Marks:", s2)
print("Subject 3 Marks:", s3)
print("Subject 4 Marks:", s4)
print("Subject 5 Marks:", s5)

total = s1 + s2 + s3 + s4 + s5
per = total / 5

print("Total Marks:", float(total))
print(f"Percentage: {per:.2f}%")



# 6 Basic code for tempreture classification

print("Temperature Classification Program")
print("----------------------------------")

try:
    temperature = float(input("Enter temperature in degree Celsius: "))

    if temperature < -273.15:
        print("Invalid temperature: below absolute zero")
    elif temperature == -273.15:
        print("Temperature is absolute zero")
    elif temperature == 0:
        print("Temperature is at the freezing point")
    elif temperature < 0:
        print("Temperature is below freezing")
    elif 0 < temperature < 100:
        print("Temperature is in the normal range")
    elif temperature == 100:
        print("Temperature is at the boiling point")
    else:
        print("Temperature is above the boiling point")

except ValueError:
    print("Please enter a valid numeric value for temperature.")



# Python Basic Practical Codes

# 1.
i = 1
while i <= 20:
    print("Hello Students")
    i += 1

# 2.
n = int(input("Enter a number: "))
i = 1
total = 0

while i <= n:
    total += i
    i += 1

print("Sum =", total)


# 3.
num = int(input("Enter a number: "))
temp = num
total = 0

while temp != 0:
    rem = temp % 10
    total += rem ** 3
    temp //= 10

if total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


# 4.
n = int(input("Enter a number: "))

for i in range(1, 11):
 print(n, "x", i, "=", n * i)


# Basic Python codes for making the pattern

# 1
num = 1

for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


# 2
for i in range(1, 6):
    print("*" * i)


# 3

for i in range(1, 6):
    for j in range(6 - i):
        print(i, end=" ")
    print()

# 4

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()



