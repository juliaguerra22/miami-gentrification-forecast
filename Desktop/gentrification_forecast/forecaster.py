import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df_2024=pd.read_csv('data/2024_data.csv')
df_2019=pd.read_csv('data/2019_data.csv')