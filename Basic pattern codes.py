#Basic Python codes for making the pattern
#1
num = 1

for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

#2
for i in range(1, 6):
    print("*" * i)

#3

for i in range(1, 6):
    for j in range(6 - i):
        print(i, end=" ")
    print()

#4

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()