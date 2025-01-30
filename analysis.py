import pandas as pd

# Load the dataset
df = pd.read_csv("houseRental.csv")

# Display the first few rows
# print(df.head())

# Check the number of rows and columns
# print(df.shape)

# # Check column names and data types
# print(df.info())

# # Check for missing values
# print(df.isnull().sum())

# # Check summary statistics
# print(df.describe())
print(df['Rent'].unique())
