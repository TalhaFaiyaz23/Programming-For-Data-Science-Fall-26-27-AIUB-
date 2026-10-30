# Loading necessary libraries

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


DATA_PATH = Path(__file__).resolve().parent / "telecom_churn.csv"
TARGET = "Churn"


if not DATA_PATH.exists():
    raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")


# Overview of the dataset and basic statistics

df = pd.read_csv(DATA_PATH)

if TARGET not in df.columns:
    raise ValueError(f"The dataset must contain a {TARGET!r} column.")

print("Dataset shape:", df.shape)
print("\nFirst five rows:")
print(df.head())

print("\nColumn data types and non-null counts:")
df.info()

print("\nMissing values by column:")
print(df.isna().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nDescriptive statistics:")
print(df.describe().T.round(2))


# Churn analysis and feature exploration

churn_counts = df[TARGET].value_counts().reindex([0, 1], fill_value=0)
churn_percentages = df[TARGET].value_counts(normalize=True).reindex(
    [0, 1], fill_value=0
) * 100
print("\nChurn counts (0 = retained, 1 = churned):")
print(churn_counts)
print("\nChurn percentages:")
print(churn_percentages.round(2))
print(f"\nOverall churn rate: {df[TARGET].mean():.2%}")

print("\nAverage values by churn status:")
print(
    df.groupby(TARGET)[
        ["DayMins", "MonthlyCharge", "CustServCalls", "DataUsage"]
    ]
    .mean()
    .round(2)
)

print("\nChurn rate by contract renewal and data plan:")
for feature in ["ContractRenewal", "DataPlan"]:
    churn_rate = df.groupby(feature)[TARGET].mean().mul(100).round(2)
    print(f"\n{feature} (percentage):")
    print(churn_rate)

print("\nChurn rate by customer service calls:")
service_calls_churn = df.groupby("CustServCalls")[TARGET].agg(
    customers="count", churn_rate="mean"
)
service_calls_churn["churn_rate"] = service_calls_churn["churn_rate"].mul(100)
print(service_calls_churn.round(2))


# CUstomer churn correlation analysis and visualizations

print("\nFeatures with the strongest linear correlation to churn:")
print(df.corr(numeric_only=True)[TARGET].drop(TARGET).sort_values().round(3))

fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(
    ["Retained (0)", "Churned (1)"],
    [churn_counts.loc[0], churn_counts.loc[1]],
    color=["steelblue", "tomato"],
)
ax.set_title("Customer Churn Counts")
ax.set_ylabel("Number of customers")
fig.tight_layout()


# Visualizing feature distributions and relationships with churn

distribution_features = [
    "AccountWeeks",
    "DataUsage",
    "CustServCalls",
    "DayMins",
    "DayCalls",
    "MonthlyCharge",
    "OverageFee",
    "RoamMins",
]
fig, axes = plt.subplots(2, 4, figsize=(16, 8))
for feature, ax in zip(distribution_features, axes.flat):
    ax.hist(df[feature], bins=25, color="steelblue", edgecolor="white")
    ax.set_title(feature)
    ax.set_ylabel("Frequency")
fig.suptitle("Feature Distributions", fontsize=16)
fig.tight_layout()


# Visualizing churn rates by categorical features and boxplots for selected features

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for feature, ax in zip(["ContractRenewal", "DataPlan"], axes):
    churn_rate = df.groupby(feature)[TARGET].mean().mul(100)
    ax.bar(churn_rate.index.astype(str), churn_rate, color="mediumpurple")
    ax.set_title(f"Churn Rate by {feature}")
    ax.set_xlabel(f"{feature} (0 = No, 1 = Yes)")
    ax.set_ylabel("Churn rate (%)")
fig.tight_layout()


# Visualizing boxplots for selected features by churn status

boxplot_features = ["CustServCalls", "DayMins", "MonthlyCharge"]
fig, axes = plt.subplots(1, len(boxplot_features), figsize=(12, 4))
for feature, ax in zip(boxplot_features, axes):
    df.boxplot(column=feature, by=TARGET, ax=ax, showfliers=False)
    ax.set_title(feature)
    ax.set_xlabel("Churn (0 = No, 1 = Yes)")
    ax.set_ylabel(feature)
fig.suptitle("Selected Features by Churn Status")
fig.tight_layout()


# Visualizing the correlation matrix of features

correlation = df.corr(numeric_only=True)
fig, ax = plt.subplots(figsize=(10, 8))
image = ax.imshow(correlation, cmap="coolwarm", vmin=-1, vmax=1)
ax.set_xticks(range(len(correlation.columns)))
ax.set_xticklabels(correlation.columns, rotation=45, ha="right")
ax.set_yticks(range(len(correlation.columns)))
ax.set_yticklabels(correlation.columns)
ax.set_title("Feature Correlation Matrix")
fig.colorbar(image, ax=ax, label="Correlation")
fig.tight_layout()

plt.show()