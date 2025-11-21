import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

#hi i used lab 5 for reference for the preprocessing, feel free to add or change anything you want
#loading data for both years
df_2024=pd.read_csv('data/2024_data.csv')
df_2019=pd.read_csv('data/2019_data.csv')

#replacing missing values with mean 
df_2024.fillna(df_2024.mean(numeric_only=True),inplace=True) 
df_2019.fillna(df_2019.mean(numeric_only=True),inplace=True)

#inputs and target separation
inputs_2024, target_2024= df_2024.drop('target', axis=1),df_2024['target']
inputs_2019, target_2019= df_2019.drop('target', axis=1),df_2019['target']

#scaling features
scaler= StandardScaler()
inputs_2024_scaled= scaler.fit_transform(inputs_2024)
inputs_2019_scaled= scaler.fit_transform(inputs_2019)
