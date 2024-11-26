import pandas as pd

# Read the CSV file
data = pd.read_csv(r"C:\Users\zw091\Downloads\COVID-19_Case_Surveillance_Public_Use_Data_with_Geography_20241125.csv")

# Ensure the 'case_month' column is in datetime format
data['case_month'] = pd.to_datetime(data['case_month'], format='%Y-%m')

# Format 'case_month' back to 'yyyy-mm'
data['case_month'] = data['case_month'].dt.strftime('%Y-%m')

# Add two new columns: case_year and case_m
data['case_y'] = pd.to_datetime(data['case_month']).dt.year
data['case_m'] = pd.to_datetime(data['case_month']).dt.month

columns = list(data.columns)
columns.insert(1, columns.pop(columns.index('case_y')))  # Move 'case_year' after 'case_month'
columns.insert(2, columns.pop(columns.index('case_m')))     # Move 'case_m' after 'case_year'
data = data[columns]


output_file_path = r"C:\Users\zw091\Downloads\Updated_COVID_Data.csv"
data.to_csv(output_file_path, index=False)

