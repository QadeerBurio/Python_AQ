import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['New York', 'Los Angeles', 'Chicago']}
# Load data
df = pd.read_csv('data.csv')

# Inspect data
print(df.head())
print(df.info())

# Clean data
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Filter data
df_filtered = df[df['Age'] > 25]

# Add new column
df_filtered['Salary'] = df_filtered['Age'] * 1000

# Group and summarize
summary = df_filtered.groupby('City')['Salary'].mean()

# Save results
summary.to_csv('summary.csv')