import pandas as pd
import numpy as np
import pickle

import snowflake.connector
#import pandas as pd
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine

#importing from the snowflake
print("Intigrating with Snowflake....")
url = URL(
    user='jayaharisai',
    password='4821_neWpassword55',
    account='BSB00500.us-east-1',
    warehouse='TEST',
    database='CSV',
    schema='PUBLIC',
    role = 'ACCOUNTADMIN'
)
engine = create_engine(url)
 
connection = engine.connect()

print("Importing the data")
query = "select * from cancer"
 
df = pd.read_sql(query, connection)
 
print(df.head())

print("checking the null values")
print(df.isnull().sum())         #chcking the null values
print(df.shape)

print("Checking the duplicates")
duplicate = df[df.duplicated()]          #checking the duplicates
print(duplicate.shape ) 
print(duplicate.index)

print("Removing the duplicates")
df.drop_duplicates(inplace = True)

from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
print(df.gender.unique())
print(df.lung_cancer.unique())


df.gender = LE.fit_transform(df.gender)
df.lung_cancer = LE.fit_transform(df.lung_cancer)

print(df.head())

#from the pycarrot training
from pycaret.classification import *
training = setup(data = df, target = 'lung_cancer', log_experiment = True)

print(training)
best = compare_models(cross_validation=True)



#print(best)

#saving to pickle
print("Pickle file is creating......")
with open("my_model.pkl", 'wb') as f:
    pickle.dump(best,f)
print("Done _|_")


