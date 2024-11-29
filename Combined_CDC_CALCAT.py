import pandas as pd

# Load the two datasets (Replace file paths with actual paths or preloaded DataFrames)
calcat_data = pd.read_csv(r"C:\Users\zw091\Downloads\Grouped_County_Data.csv")  # Replace with actual calcat file path
cdc_data = pd.read_csv(r"C:\Users\zw091\Downloads\Updated_COVID_Data.csv")  # Replace with actual CDC file path

calcat_data['target_date'] = pd.to_datetime(calcat_data['target_date']).dt.strftime('%Y-%m')
cdc_data['case_month'] = pd.to_datetime(cdc_data['case_month']).dt.strftime('%Y-%m')

# Standardize column names and values (convert to lowercase and strip whitespace)
calcat_data['location'] = calcat_data['location'].str.lower().str.strip()
cdc_data['res_county'] = cdc_data['res_county'].str.lower().str.strip()

# Rename columns in CDC data for consistency
cdc_data.rename(columns={'res_county': 'location', 'case_month': 'target_date'}, inplace=True)

# Perform the merge on 'location' and 'target_date'
merged_data = pd.merge(calcat_data, cdc_data, on=['location', 'target_date'], how='inner')

# Drop the 'res_state' column
merged_data = merged_data.drop(columns=['res_state'])

# Rename columns for clarity
merged_data.rename(columns={'case_y': 'case_year', 'case_m': 'case_month'}, inplace=True)

# Reorder the columns
column_order = [
    'location', 'target_date', 'case_year', 'case_month', 'age_group',
    'sex', 'race', 'ethnicity', 'current_status', 'symptom_status',
    'hosp_yn', 'icu_yn', 'value'
]
merged_data = merged_data[column_order]

# Save the updated DataFrame to a CSV
output_file_path = r"C:\Users\zw091\Downloads\Ordered_Merged_Data.csv"
merged_data.to_csv(output_file_path, index=False)

print(f"Updated merged data saved to: {output_file_path}")
