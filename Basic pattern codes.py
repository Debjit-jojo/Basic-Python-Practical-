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


#5

n = 5

for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# Python Codes for making matrix

import numpy as np

# Input 5x3 matrix
print("Enter elements of 5x3 matrix:")
matrix1 = np.array([[int(input()) for j in range(3)] for i in range(5)])

# Input 3x2 matrix
print("Enter elements of 3x2 matrix:")
matrix2 = np.array([[int(input()) for j in range(2)] for i in range(3)])

print("\nMatrix 1 (5x3):")
print(matrix1)

print("\nMatrix 2 (3x2):")
print(matrix2)

# Matrix multiplication
product = np.dot(matrix1, matrix2)

print("\nProduct Matrix (5x2):")
print(product)

    






