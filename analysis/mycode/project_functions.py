import pandas as pd
import numpy as n

def first_python_module(url_or_path_to_csv_file):

   # Method Chain 1 (Load data,rename columns, get rid of null values and drop necessary data with missing data)

    df1 = (
          pd.read_csv(url_or_path_to_csv_file)    
            .drop(['instant','dteday','yr','season','mnth','holiday','workingday','weekday','atemp'], axis=1)
            .rename(columns={'cnt': 'total users', 'weathersit':'weathercondition'})  
            .dropna(axis=0)
        )
    
    df2 = (
        df1.dropna(subset=['windspeed','hum','temp','weathercondition','casual','registered','total users'])
            .loc[lambda x: x['windspeed']>0.1]
            .loc[lambda x: x['windspeed'] < 0.26]
            .loc[lambda x: x['hum'] > 0.5]
            .assign(rainy_day=lambda x: x['hum'] > 0.7)  # create a new column 'rainy' based on the condition
            .assign(rainy_day=lambda x: x['rainy_day'].astype(int)) # replace values with int to define rainyday or not 
            .reset_index(drop = True) 
    )

    return df2
