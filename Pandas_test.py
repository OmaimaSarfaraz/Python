# Pandas Series
import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)


# DataFrame Basics
data = {
    "Name": ["Ali", "Sara", "Omaima"],
    "Age": [20, 22, 19],
    "Marks": [88, 92, 95]
}

df = pd.DataFrame(data)
print(df)


# Read CSV File
df = pd.read_csv("students.csv", encoding="utf-8", engine="python")
print(df)


# Selecting Data
print(df["Name"])  # Select single column:
print(df[["Name", "Marks"]])  # Select multiple columns:


# Filtering Data
high = df[df["Marks"] > 90]
print(high)


# Sorting
sorted_df = df.sort_values(by="Marks", ascending=False)
print(sorted_df)


# Basic Analysis
print(df["Marks"].max())
print(df["Marks"].min())
print(df["Marks"].mean())


# Export Back to CSV
df.to_csv("output.csv", index=False)


# Mini Project (students.csv Analysis)
# import pandas as pd

# df = pd.read_csv("students.csv")

# print("Top Students:")
# print(df[df["Marks"] > 90])

# print("\nAverage Marks:", df["Marks"].mean())

# print("\nSorted by Marks:")
# print(df.sort_values(by="Marks", ascending=False))