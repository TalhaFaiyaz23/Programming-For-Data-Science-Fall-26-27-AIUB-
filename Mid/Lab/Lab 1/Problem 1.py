 # Problem Statement :  Write a program that inputs two numbers and displays their sum, difference, product, and quotient. Convert the inputs to numeric values before calculating.


# Solve:
# take input from user

num1 = float(input("Enter a numeric value: "))
num2 = float(input("Enter another numeric value: "))

def calculator(num1, num2):

    # addition

    add = num1 + num2

    print("The addition of",num1, "and", num2, "is: ", add)

    # subtraction

    sub = num1 - num2

    print("The subtraction of",num1, "and", num2, "is: ", sub)

    # multiplication

    mul = num1 * num2

    print("The multiplication of",num1, "and", num2, "is: ", mul)

    # division

    if num2 != 0:
        div = num1 / num2
        print("The division of",num1, "and", num2, "is: ", div)
    else:
        print("Error: Division by zero is not allowed.")