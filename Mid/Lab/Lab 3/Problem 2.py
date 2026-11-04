# Problem 2 – Data Filtering. Using the Titanic dataset:
# 1. Display passengers belonging to first class (Pclass == 1).
# 2. Find passengers younger than 18.
# 3. Find male passengers who survived.
# 4. Find passengers who paid a fare greater than 100


import pandas as pd

# Load the Titanic dataset
df = pd.read_csv("train.csv")


# 1. Display passengers belonging to first class (Pclass == 1)
first_class = df[df["Pclass"] == 1]
print("--- First Class Passengers ---")
print(first_class.head())

# 2. Find passengers younger than 18
under_18 = df[df["Age"] < 18]
print("\n--- Passengers Younger than 18 ---")
print(under_18.head())

# 3. Find male passengers who survived
male_survived = df[(df["Sex"] == "male") & (df["Survived"] == 1)]
print("\n--- Male Passengers Who Survived ---")
print(male_survived.head())

# 4. Find passengers who paid a fare greater than 100
high_fare = df[df["Fare"] > 100]
print("\n--- Passengers with Fare > 100 ---")
print(high_fare.head())