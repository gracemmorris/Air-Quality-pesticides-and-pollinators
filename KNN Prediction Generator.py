# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 16:37:56 2023

@author: grace
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.preprocessing import StandardScaler
from math import sqrt
import numpy as np


# load spreadsheet with data 
df1 = pd.read_excel('LatLongPanTrap.xlsx')
#load spreadsheets with the lat & long co ordinates we want to predict for
df2 = pd.read_excel('Lat and long to generate.xlsx')

features=["x","y"]
target="Count"
 
X = df1[features]
Y = df1[target]

#split into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


knn_model = KNeighborsRegressor(n_neighbors=10)
knn_model.fit(X_train, Y_train)

#find the nearest n neighbours from the first dataset for an (x,y) in the second
distances, indices = knn_model.kneighbors(df2[['x', 'y']], n_neighbors=8, return_distance=True)

#gaussian kernal weights the data points from df1 based on their distance away from the point in df2
def gaussian_kernel(distance, bandwidth=1):
    return np.exp(-0.5 * (distance / bandwidth) ** 2)


for i, (neighbor_distances, neighbor_indices) in enumerate(zip(distances, indices)):
    neighbor_counts = Y.iloc[neighbor_indices]
    
    # Calculate weights using Gaussian kernel
    weights = gaussian_kernel(neighbor_distances)
    
    # Weighted average of neighbor counts
    weighted_average_count = (neighbor_counts * weights).sum() / weights.sum()
    
    df2.at[i, 'predicted_count'] = weighted_average_count


# Evaluate the performance on the test set from the first spreadsheet (optional)
y_pred_test = knn_model.predict(X_test)
rmse = sqrt(mean_squared_error(y_test, y_pred_test))
print(f'Root Mean Squared Error on the test set: {rmse}')

# Save the updated second spreadsheet with predicted count values
df2.to_excel('just_pantrap_predictions.xlsx', index=False)


