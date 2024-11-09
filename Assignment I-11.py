import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/Users/anniehuang/Code/ I-11 Getting started with AI/AirlineReviews.csv')
print(df.head())

numerical_columns = [
    'OverallRating', 'SeatComfort', 'CabinStaffService',
    'GroundService', 'ValueForMoney', 'Food&Beverages',
    'InflightEntertainment', 'Wifi&Connectivity'
]
mean_values = df[numerical_columns].mean()
median_values = df[numerical_columns].median()
std = df[numerical_columns].std()

print("\nMean Values:\n", mean_values, sep="")
print("\nMedian Values:\n", median_values, sep="")
print("\nStandard Deviation Values:\n", std, sep="")

plt.figure(figsize=(12, 6))
sns.boxplot(data=df[numerical_columns])
plt.title('Boxplot of Review Scores')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()