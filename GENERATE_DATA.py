# Synthetic dataset generator for a mid-market healthcare company
import pandas as pd
import numpy as np

# Set reproducibility seed
np.random.seed(42)

# Generate monthly date range
dates = pd.date_range(start="2021-01-01", end="2024-01-01", freq="M")

# Simulate financial metrics
data = {
    "date": dates,
    "revenue": np.random.normal(200000, 30000, len(dates)).round(2),
    "COGS": np.random.normal(90000, 10000, len(dates)).round(2),
    "SGA": np.random.normal(25000, 4000, len(dates)).round(2),
    "R&D": np.random.normal(15000, 2000, len(dates)).round(2),
    "depreciation": np.random.normal(3000, 500, len(dates)).round(2),
    "cash": np.random.normal(80000, 10000, len(dates)).round(2),
    "accounts_receivable": np.random.normal(45000, 5000, len(dates)).round(2),
    "inventory": np.random.normal(35000, 4000, len(dates)).round(2),
    "accounts_payable": np.random.normal(25000, 3000, len(dates)).round(2),
}

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv("synthetic_healthcare_financials.csv", index=False)
print("Synthetic financial data saved to 'synthetic_healthcare_financials.csv'")


python generate_data.py
