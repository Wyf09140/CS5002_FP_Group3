import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load your merged dataset
merged_data = pd.read_csv(r"C:\Users\zw091\Downloads\Ordered_Merged_Data.csv")

# Binary Encoding for 'sex' and 'hosp_yn'
merged_data['sex'] = merged_data['sex'].map({'Male': 0, 'Female': 1})
merged_data['hosp_yn'] = merged_data['hosp_yn'].map({'No': 0, 'Yes': 1, 'Missing': 0})
merged_data['symptom_status'] = merged_data['symptom_status'].map({'Asymptomatic': 0, 'Symptomatic': 1})

# Label Encoding for categorical features with multiple categories
categorical_cols = ['location', 'age_group', 'race', 'ethnicity', 'current_status']

label_encoders = {}  # To store the encoders in case you need them later
for col in categorical_cols:
    le = LabelEncoder()
    merged_data[col] = le.fit_transform(merged_data[col])
    label_encoders[col] = le

# Drop unnecessary columns (if any)
# merged_data = merged_data.drop(columns=['icu_yn']) # already removed based on your description

# Save to CSV (optional)
output_file_path = r"C:\Users\zw091\Downloads\Encoded_Merged_Data.csv"
merged_data.to_csv(output_file_path, index=False)

print(f"Encoded data saved to: {output_file_path}")
