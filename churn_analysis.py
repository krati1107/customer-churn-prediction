import pandas as pd

# Load dataset
df = pd.read_csv('../data/churn_data.csv')

# Display first few rows
print("First few rows of the data:")
print(df.head())

# Basic EDA: Churn rate by gender
churn_by_gender = df.groupby('Gender')['Churn'].mean()
print("\nChurn rate by Gender:")
print(churn_by_gender)

# Churn rate by tenure (tenure in groups)
df['TenureGroup'] = pd.cut(df['Tenure'], bins=[0, 3, 6, 9, 12], labels=['0-3', '4-6', '7-9', '10-12'])
churn_by_tenure = df.groupby('TenureGroup')['Churn'].mean()
print("\nChurn rate by Tenure Group:")
print(churn_by_tenure)

# Churn rate by balance
churn_by_balance = df.groupby(pd.cut(df['Balance'], bins=3))['Churn'].mean()
print("\nChurn rate by Balance Range:")
print(churn_by_balance)

# Example SQL-like operation: Count churn by tenure
churn_tenure_sql = df.query('Churn == 1').groupby('Tenure')['CustomerID'].count()
print("\nCount of churned customers by Tenure:")
print(churn_tenure_sql)
