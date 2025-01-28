# -*- coding: utf-8 -*-
"""Feature_scaling(AD).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dTWi3bk20vFxdPiPqUDFqpfgC2iH8e18
"""

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Sample DataFrame
data = {
    'gender': ['male', 'female', 'female', 'male', 'female'],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Chicago', 'New York'],
    'age': [23, 34, 45, 25, 36]
}

df = pd.DataFrame(data)

# Display original dataframe
print("Original dataframe:")
print(df)

# Initialize OneHotEncoder
one_hot_encoder = OneHotEncoder(sparse_output=False)

# Columns to encode
columns_to_encode = ["gender", "city"]

# Apply OneHotEncoder
encoded_data = one_hot_encoder.fit_transform(df[columns_to_encode])

# Get encoded column names
encoded_columns = one_hot_encoder.get_feature_names_out(columns_to_encode)

# Convert encoded data to DataFrame
encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns)

# Concatenate the original dataframe with the encoded data
df_encoded = pd.concat([df, encoded_df], axis=1).drop(columns=columns_to_encode)

# Display the resulting DataFrame
print("\nDataFrame with One-Hot Encoded Columns:")
print(df_encoded)

