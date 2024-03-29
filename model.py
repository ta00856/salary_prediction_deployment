# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

try:
    dataset = pd.read_csv('hiring.csv', encoding='utf-8')  # Try UTF-8 first
except UnicodeDecodeError:
    try:
        dataset = pd.read_csv('hiring.csv', encoding='latin1')  # Try latin1
    except UnicodeDecodeError:
        dataset = pd.read_csv('hiring.csv', encoding='cp1252')  # Try cp1252


dataset['experience'].fillna(0, inplace=True)

dataset['test_score'].fillna(dataset['test_score'].mean(), inplace=True)

X = dataset.iloc[:, :3]


y = dataset.iloc[:, -1]

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2, 9, 6]]))