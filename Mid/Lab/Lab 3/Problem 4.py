# Problem 3 – Sorting and Aggregation. Using the Titanic dataset:
# 1. Display the 10 passengers who paid the highest fares.
# 2. Calculate the average passenger age.
# 3. Count the number of male and female passengers.
# 4. Calculate the average fare for each passenger class.
# 5. Calculate the survival rate for each passenger class.


import pandas as pd

# Load the Titanic dataset
df = pd.read_csv("train.csv")


# 1. Display the 10 passengers who paid the highest fares
top10_fare = df.sort_values(by="Fare", ascending=False).head(10)
print("--- Top 10 Highest Fares ---")
print(top10_fare[["Name", "Pclass", "Fare"]])

# 2. Calculate the average passenger age
avg_age = df["Age"].mean()
print(f"\nAverage Passenger Age: {avg_age:.2f} years")

# 3. Count the number of male and female passengers
gender_counts = df["Sex"].value_counts()
print("\n--- Gender Breakdown ---")
print(gender_counts)

# 4. Calculate the average fare for each passenger class
avg_fare_pclass = df.groupby("Pclass")["Fare"].mean()
print("\n--- Average Fare by Passenger Class ---")
print(avg_fare_pclass)

# 5. Calculate the survival rate for each passenger class
survival_rate_pclass = df.groupby("Pclass")["Survived"].mean()
print("\n--- Survival Rate by Passenger Class ---")
print(survival_rate_pclass)