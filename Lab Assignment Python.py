# Lab Assignment

#1
string = input("Enter a string: ")

vowels = 0
consonants = 0
spaces = 0
lowercase = 0

for ch in string:
    if ch in "aeiouAEIOU":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    
    if ch == " ":
        spaces += 1
    
    if ch.islower():
        lowercase += 1

print("Number of Vowels:", vowels)
print("Number of Consonants:", consonants)
print("Number of Spaces:", spaces)
print("Number of Lowercase Letters:", lowercase)


#2
def capitalize_lines():
    print("Enter lines (type 'END' to stop):")
    
    while True:
        line = input()
        if line == "END":
            break
        print(line.upper())

capitalize_lines()


#3

nums = input("Enter integers separated by space: ")
t = tuple(map(int, nums.split()))
print("Total number of items:", len(t))
if len(t) > 0:
    print("Last item:", t[-1])
else:
    print("Tuple is empty")
print("Tuple in reverse order:", t[::-1])
if 5 in t:
    print("Yes")
else:
    print("No")

if len(t) > 2:
    new_tuple = tuple(sorted(t[1:-1]))
    print("After removing first & last and sorting:", new_tuple)
else:
    print("Not enough elements to remove first and last")



#4

prices_input = input("Enter prices separated by space: ")
prices = tuple(map(float, prices_input.split()))
print("Total items sold:", len(prices))

if len(prices) > 0:
    print("Cheapest item price:", min(prices))
    print("Costliest item price:", max(prices))
    print("Prices in ascending order:", tuple(sorted(prices)))
    costliest = max(prices)
    count = prices.count(costliest)
    print("Number of costliest items sold:", count)
else:

    print("No items sold")





