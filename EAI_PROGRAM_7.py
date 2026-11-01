# Data Cleaning and Exploratory Data Analysis using Pandas
import pandas as pd

raw_data = {
    "Name": ["Anitha", "Bala", "Chitra", "Dinesh", "Ezhil", "Fathima"],
    "Department": ["CSE", "CSE", "ECE", "CSE", "ECE", "CSE"],
    "Attendance": [92, 85, None, 88, 95, 90],
    "Mark": [86, 91, 78, None, 95, 82]
}
data_df = pd.DataFrame(raw_data)

print("--- Original Dataset ---")
print(data_df)
print("\nMissing Values:")
print(data_df.isnull().sum())

# Missing value treatment
data_df["Attendance"] = data_df["Attendance"].fillna(data_df["Attendance"].mean())
data_df["Mark"] = data_df["Mark"].fillna(data_df["Mark"].mean())

# Remove duplicate records
data_df = data_df.drop_duplicates()

print("\n--- Cleaned Dataset ---")
print(data_df)
print("\n--- Descriptive Statistics ---")
print(data_df.describe())
print("\n--- Department-wise Average Marks ---")
print(data_df.groupby("Department")["Mark"].mean().round(2))
print("\n--- EDA Summary ---")
print("Highest Mark :", data_df["Mark"].max())
print("Lowest Mark  :", data_df["Mark"].min())
print("Average Mark :", round(data_df["Mark"].mean(), 2))
print("Average Attendance :", round(data_df["Attendance"].mean(), 2))