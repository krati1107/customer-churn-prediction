# customer-churn-prediction
"This project analyzes customer churn patterns using Python. The goal is to identify key factors that influence customer attrition by performing exploratory data analysis on customer demographics, tenure, and account behavior. Insights help businesses understand what drives customer loyalty and churn, enabling better retention strategies."

## Dataset
- The dataset is a synthetic CSV file (`churn_data.csv`) with customer details:
  - CustomerID: Unique identifier
  - Age: Age of the customer
  - Gender: Male or Female
  - Balance: Account balance
  - Tenure: Number of months the customer has been with the service
  - NumOfProducts: Number of products held by the customer
  - Churn: Whether the customer churned (1) or not (0)

## Tools Used
- Python (Pandas for data analysis)
- SQL-like queries with Pandas DataFrame
- Jupyter Notebook or command-line Python script

## Analysis Steps
1. Load the dataset.
2. Perform exploratory data analysis (EDA) on churn by gender, tenure, and balance.
3. Use SQL-like queries to filter and count churn patterns.

## Insights
- Churn rate by gender, tenure, and balance groups is calculated.
- Tenure and balance appear to influence churn patterns.

## Future Work
- Connect to a real SQL database (e.g., SQLite) for more complex queries.
- Integrate visualization (e.g., Matplotlib or Seaborn) to enhance insights.
