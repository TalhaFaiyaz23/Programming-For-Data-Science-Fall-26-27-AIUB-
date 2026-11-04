# Problem 1 – Dataset Inspection.
# 1. Display the first 10 rows.
# 2. Find the number of rows and columns.
# 3. Identify all column names.
# 4. Determine the data type of each column.
# 5. Display descriptive statistics for numerical columns.


# import pandas library first
import pandas as pd

# Load the Titanic dataset
df = pd.read_csv("train.csv")


# 1. Display the first 10 rows
print("--- First 10 Rows ---")
print(df.head(10))

# 2. Find the number of rows and columns
rows, cols = df.shape
print(f"\nNumber of Rows: {rows}, Number of Columns: {cols}")

# 3. Identify all column names
print("\n--- Column Names ---")
print(df.columns.tolist())

# 4. Determine the data type of each column
print("\n--- Data Types ---")
print(df.dtypes)

# 5. Display descriptive statistics
print("\n--- Descriptive Statistics ---")
print(df.describe())