# Problem Statement : Ask the user to enter a word or short sentence. Display the number of characters, vowels (a, e, i, o, u), and spaces. Use a for loop to examine each character.

# Solve :

User = input(str("Enter a word or short sentence: "))

# 1. Display the number of characters

char = len(User)
print(f"Number of Characters: {char}")

# 2. Count the number of vowels and spaces

if char == 0:
    print("You did not enter any characters.")
elif char != 0:
    vowels = 0
    spaces = 0

    for i in User:
        if i.lower() in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1
        elif i == " ":
            spaces += 1

    print(f"Number of Vowels: {vowels}")
    print(f"Number of Spaces: {spaces}")