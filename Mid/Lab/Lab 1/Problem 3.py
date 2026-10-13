# Problem Statement :  Input a temperature in Celsius and convert it to Fahrenheit and Kelvin using the formulas: F = (C × 9/5) + 32,  K = C + 273.15

# Solve:


#1.
# letting user choose for their desired temperature type

Query = input("What is the type of your temperature? Choose from F as Fahrenheit, K as Kelvin, C as Celsius: ").upper()


if Query not in ["f","F","k","K","c","C"]:
    print("Invalid input. Please enter 'F', 'K', or 'C' for the temperature type.")

else:
    print("You have chosen", Query, "as your temperature type.")

# Getting the Numeric Data for the conversion

temp = float(input("Enter the temperature in numeric value: "))



#2.
#letting user choose for their desired conversion type

Choice = input(str("Enter 'F' to convert to Fahrenheit or 'K' to convert to Kelvin or 'C' to convert to Celsius or 'B' to convert to all: ")).upper()

if Choice == "F" and Query == "F":      # F to F conversion

    fahrenheit = temp
    print(f"{temp}°F is equal to {fahrenheit}°F")

elif Choice == "F" and Query == "C":     # C to F conversion
       
    celcius = (temp * 9/5) + 32
    print(f"{temp}°F is equal to {celcius}°C")

elif Choice == "C" and Query == "C":     # C to C conversion

    celcius = temp
    print(f"{temp}°C is equal to {celcius}°C")

elif Choice == "K" and Query == "F":    # F to K conversion

    kelvin = temp + 273.15
    print(f"{temp}°K is equal to {kelvin}°K")

elif Choice == "K" and Query == "K":   # K to K conversion

    kelvin = temp
    print(f"{temp}°K is equal to {kelvin}°K")

elif Choice == "C" and Query == "K":    # K to C conversion

    celcius = temp - 273.15
    print(f"{temp}°C is equal to {celcius}°C")

elif Choice == "F" and Query == "K":    # K to F conversion

    fahrenheit = ((temp - 273.15) * 9/5) + 32
    print(f"{temp}°K is equal to {fahrenheit}°F")

elif Choice == "B" and Query == "C":    # C to all conversion

    celcius = temp
    fahrenheit = (temp * 9/5) + 32
    kelvin = temp + 273.15
    print(f"{temp}°C is equal to {fahrenheit}°F and {kelvin}°K and {celcius}°C")

elif Choice == "B" and Query == "K":    # K to all conversion

    celcius = temp - 273.15
    fahrenheit = ((temp - 273.15) * 9/5) + 32
    kelvin = temp
    print(f"{temp}°K is equal to {fahrenheit}°F and {kelvin}°K and {celcius}°C")

elif Choice == "B" and Query == "F":    # F to all conversion

    celcius = (temp - 32) * 5/9
    fahrenheit = temp
    kelvin = (temp - 32) * 5/9 + 273.15
    print(f"{temp}°F is equal to {fahrenheit}°F and {kelvin}°K and {celcius}°C")

else:
    print("Invalid choice. Please choose 'F', 'K', 'C', or 'B'.")


