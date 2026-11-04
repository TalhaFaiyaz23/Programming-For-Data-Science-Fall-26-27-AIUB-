# Titanic Dataset Analysis Using Pandas and the Titanic dataset, write a Python program to answer the following questions:
# 1. How many passengers are in the dataset?
# 2. What is the average passenger age?
# 3. Which passenger class has the highest number of passengers?
# 4. What is the average fare paid by male and female passengers?
 #5. Which gender has a higher survival rate?
# 6. How does the survival rate differ across passenger classes? Present the results using appropriate Pandas operations and briefly explain your findings.


import pandas as pd

# Load the Titanic dataset
df = pd.read_csv("train.csv")


# 1. Total passengers
total_passengers = len(df)
print(f"1. Total Passengers: {total_passengers}")

# 2. Average age
average_age = df["Age"].mean()
print(f"2. Average Passenger Age: {average_age:.2f} years")

# 3. Passenger class with the highest count
class_counts = df["Pclass"].value_counts()
highest_class = class_counts.idxmax()
print(f"3. Class with Highest Passengers: Class {highest_class} ({class_counts[highest_class]} passengers)")

# 4. Average fare paid by male and female passengers
avg_fare_gender = df.groupby("Sex")["Fare"].mean()
print("\n4. Average Fare by Gender:")
print(avg_fare_gender)

# 5. Gender survival rate comparison
survival_by_gender = df.groupby("Sex")["Survived"].mean()
higher_survival_gender = survival_by_gender.idxmax()
print("\n5. Survival Rate by Gender:")
print(survival_by_gender)
print(f"-> {higher_survival_gender.capitalize()} passengers had a significantly higher survival rate.")

# 6. Survival rate across passenger classes
survival_by_class = df.groupby("Pclass")["Survived"].mean()
print("\n6. Survival Rate by Passenger Class:")
print(survival_by_class)