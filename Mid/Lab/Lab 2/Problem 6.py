# Problem Statement : Write a program using a while loop that asks the user for a non-negative integer and prints a countdown from that number to zero

# Solve :

n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    while n >= 0:
        print(n)
        n -= 1