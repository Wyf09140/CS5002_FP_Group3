import pandas as pd

# Import the datasets
data_2024 = pd.read_csv(r"C:\Users\zw091\Downloads\outputfile.csv", dtype=str)
data_20_23 = pd.read_csv(r"C:\Users\zw091\Downloads\historical_archive_2020_2023\historical_archive_2020_2023\nowcast_2020_2023.csv", dtype=str)

# Combine the datasets
combined_data = pd.concat([data_2024, data_20_23], ignore_index=True)

# Drop the specified columns
columns_to_drop = ['disease', 'target', 'model', 'quantile', 'archivedt', 'Unnamed: 0']
cleaned_data = combined_data.drop(columns=columns_to_drop)

# Filter the dataset to include only rows where location_level is 'county'
county_data = cleaned_data[cleaned_data['location_level'] == 'county'].copy()  # Create a copy to avoid warnings

# Convert the target_date column to yyyy-mm format
county_data['target_date'] = pd.to_datetime(county_data['target_date']).dt.strftime('%Y-%m')

# Convert the value column to numeric
county_data['value'] = pd.to_numeric(county_data['value'], errors='coerce')

# Drop the location_level column
county_data = county_data.drop(columns=['location_level'])

# Group by 'location' and 'target_date', calculating the average of 'value'
grouped_data = county_data.groupby(['location', 'target_date'], as_index=False)['value'].mean()

# Save the grouped data as a CSV file
output_file_path = r"C:\Users\zw091\Downloads\Grouped_County_Data.csv"
grouped_data.to_csv(output_file_path, index=False)

print(f"Processed CSV file saved at: {output_file_path}")
