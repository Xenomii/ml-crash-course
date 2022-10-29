# 1. Importing the libraries

# numpy -> Allow us to work with arrays (need them for inputs to ML models)
# matplotlib -> Allow us to plot nice charts
# pandas -> Allow us to import the dataset

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 2. Importing the dataset

dataset = pd.read_csv('Data.csv')

# Determine the independent variables (inputs)
x = dataset.iloc[:, :-1].values # [All rows, All columns except the last column]
# Determine the dependent variables (outputs)
y = dataset.iloc[:, -1].values # [All rows, Only the last column]

# print(x)
# print(y)

# 3. Taking care of missing data

# There are two methods:
#   1. Delete the missing data
#   2. Replace the missing data with the average value of that column

# Using the SimpleImputer class
from sklearn.impute import SimpleImputer

# Replace nan values with the average value
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
# Exclude columns with string values for the replacement
imputer.fit(x[:, 1:3]) # [All rows, Include 2nd and 3rd columns]
# Perform the replacement and update the dataset values
x[:, 1:3] = imputer.transform(x[:, 1:3])

# print(x)

# 4. Encoding categorical data

# We have a column with string values so it will be difficult for the model to compute correlations between the inputs and output
# Have to turn (encode) the string values into numbers

# We are going to be using one hot encoding for the Country column
#   - The Country column will turn into 3 columns
#   - The numerical value is in binary

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

# Apply the encoding technique on the 1st column and keep the other columns
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
# Perform the encoding and convert the return value into an array
x = np.array(ct.fit_transform(x))

# print(x)

# We are using label encoding on the Purchased column
#   - This is OK for the dependent variable
#   - The numerical value is either 0 or 1

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
y = le.fit_transform(y)

# print(y)

# 5. Splitting dataset into training and test sets

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=1) # random_state is optional (seed)

# print(x_train)
# # [[0.0 0.0 1.0 38.77777777777778 52000.0]
# #  [0.0 1.0 0.0 40.0 63777.77777777778]
# #  [1.0 0.0 0.0 44.0 72000.0]
# #  [0.0 0.0 1.0 38.0 61000.0]
# #  [0.0 0.0 1.0 27.0 48000.0]
# #  [1.0 0.0 0.0 48.0 79000.0]
# #  [0.0 1.0 0.0 50.0 83000.0]
# #  [1.0 0.0 0.0 35.0 58000.0]]
# print(x_test)
# # [[0.0 1.0 0.0 30.0 54000.0]
# #  [1.0 0.0 0.0 37.0 67000.0]]
# print(y_train)
# # [0 1 0 0 1 1 0 1]
# print(y_test)
# # [0 1]

# 6. Feature scaling

# Scaling the inputs so that a feature does not dominate and be eliminated in some models
#   - All features are equal

# There are two methods to perform feature scaling
#   1. Standardization
#       - Good all the time :D
#   2. Normalization
#       - Recommended when most of your features have a normal distribution

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
# Fitting, transforming is performed on the training set (not the encoded column)
x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])
# Apply the same scaler on the test set
x_test[:, 3:] = sc.transform(x_test[:, 3:])

# print(x_train)
# # [[0.0 0.0 1.0 -0.19159184384578545 -1.0781259408412425]
# #  [0.0 1.0 0.0 -0.014117293757057777 -0.07013167641635372]
# #  [1.0 0.0 0.0 0.566708506533324 0.633562432710455]
# #  [0.0 0.0 1.0 -0.30453019390224867 -0.30786617274297867]
# #  [0.0 0.0 1.0 -1.9018011447007988 -1.420463615551582]
# #  [1.0 0.0 0.0 1.1475343068237058 1.232653363453549]
# #  [0.0 1.0 0.0 1.4379472069688968 1.5749910381638885]
# #  [1.0 0.0 0.0 -0.7401495441200351 -0.5646194287757332]]
# print(x_test)
# # [[0.0 1.0 0.0 -1.4661817944830124 -0.9069571034860727]
# #  [1.0 0.0 0.0 -0.44973664397484414 0.2056403393225306]]
