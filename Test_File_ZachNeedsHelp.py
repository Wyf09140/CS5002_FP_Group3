import pickle
import numpy as np
import pandas

# Encoder Files
modelFile = 'Models/bNB.pkl'
catXFile = 'Encoders/catX_Enc.pkl'
discFile = 'Encoders/binDiscrete10.pkl'
labelFile = 'Encoders/labelEncN_Y.pkl'



# Sample Represents the input data coming from
sample_data = {
    "location": "santa clara",
    "month": 12,                    
    "age_group": "65+ years",
    "sex": "Male",             
    "race": "White",                
    "ethnicity": "Non-Hispanic/Latino",
    "current_status": "Laboratory-confirmed case",  
    "symptom_status": "Symptomatic", 
    "average_value": 1.33 #estimation
}

# Convert to dataframe
inputDf = pandas.DataFrame([sample_data])

# Open Categorical Encoder
with open(catXFile, 'rb') as f:
    ohe = pickle.load(f)

# Split continuous and categorical
X_cont = inputDf['average_value']
inputDf = inputDf.drop(['average_value'], axis = 1)

# Apply ohe encoding to input data
X_enc = ohe.transform(inputDf)
X_processed = pandas.DataFrame(X_enc.toarray(), columns = ohe.get_feature_names_out())
print(X_processed.columns)

# Open bin encoder
with open(discFile, 'rb') as f:
    est = pickle.load(f)

# Apply transformation
transCSR = est.transform(pandas.DataFrame(X_cont))
df_cont = pandas.DataFrame(transCSR.toarray(), columns = est.get_feature_names_out())

# Combine the two dataframes
X_processed = pandas.concat([X_processed, df_cont], axis = 1)


# Load the model
with open(modelFile, 'rb') as f:
    model = pickle.load(f)

# make prediction
pred_y = model.predict_proba(X_processed)
print(pred_y)

























# # Encoding the sample data (assuming simple label encoding)
# def encode_sample_data(data):
#     # Encoding each field based on assumed label encoding used in training
#     county_mapping = {"Alameda": 0, "Santa Clara": 1, "San Francisco": 2} 
#     race_mapping = {"American Indian/Alaska Native": 0, "Asian": 1, "Black": 2, "Multiple/Other": 3,
#                     "Native Hawaiian/Other Pacific Islander": 4, "White": 5}
#     ethnicity_mapping = {"Hispanic/Latino": 0, "Non-Hispanic/Latino": 1}
#     sex_mapping = {"Male": 0, "Female": 1}
#     age_group_mapping = {"0 - 17 years": 0, "18 to 49 years": 1, "50 to 64 years": 2, "65+ years": 3}
#     current_status_mapping = {"Laboratory-confirmed case": 0, "Probable Case": 1}
#     symptoms_mapping = {"Asymptomatic": 0, "Symptomatic": 1}

#     # Verify that the input data contains valid values
#     if data["County"] not in county_mapping:
#         raise ValueError(f"Invalid County: {data['County']}")
#     if data["Race"] not in race_mapping:
#         raise ValueError(f"Invalid Race: {data['Race']}")
#     if data["Ethnicity"] not in ethnicity_mapping:
#         raise ValueError(f"Invalid Ethnicity: {data['Ethnicity']}")
#     if data["Sex"] not in sex_mapping:
#         raise ValueError(f"Invalid Sex: {data['Sex']}")
#     if data["Age Group"] not in age_group_mapping:
#         raise ValueError(f"Invalid Age Group: {data['Age Group']}")
#     if data["Current Status"] not in current_status_mapping:
#         raise ValueError(f"Invalid Current Status: {data['Current Status']}")
#     if data["Symptoms"] not in symptoms_mapping:
#         raise ValueError(f"Invalid Symptoms: {data['Symptoms']}")

#     # Return encoded values
#     return [
#         county_mapping[data["County"]],
#         data["Month"],
#         race_mapping[data["Race"]],
#         ethnicity_mapping[data["Ethnicity"]],
#         sex_mapping[data["Sex"]],
#         age_group_mapping[data["Age Group"]],
#         current_status_mapping[data["Current Status"]],
#         symptoms_mapping[data["Symptoms"]]
#     ]

# # Transform the sample data
# try:
#     encoded_sample = encode_sample_data(sample_data)
# except ValueError as e:
#     print(e)
#     encoded_sample = None

# # Proceed only if the data is valid
# if encoded_sample:
#     # Pad the encoded sample with zeros to match the expected number of features (43)
#     encoded_sample = np.pad(encoded_sample, (0, 43 - len(encoded_sample)), 'constant')

#     # Make sure the sample data is in the correct format for prediction (e.g., a 2D array)
#     encoded_sample = np.array([encoded_sample])

#     # Predict the probability of hospitalization
#     probability = model.predict_proba(encoded_sample)

#     # Print the probability of hospitalization
#     print("Probability of hospitalization:", probability)
