# import required libraries
import pandas as pd
import boto3


from configparser import ConfigParser

import snowflake.connector

from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine

file = "cred/snowflake.ini"
config = ConfigParser()
print(config.read(file))

url = URL(
    user = config["account"]["user"],
    password=config["account"]["password"],
    account=config["account"]["account"],
    warehouse=config["account"]["warehouse"],
    database=config["account"]["database"],
    schema=config["account"]["schema"],
    role = config["account"]["role"]
)

engine = create_engine(url)
connection = engine.connect()
query = "select * from cancer"


# importing the data
def load_data():
    data = pd.read_sql(query, connection)
    #data = pd.read_csv("survey lung cancer.csv")  # loading the dataset to dataframe
    #print(data.head())
    return data
#helollo
# calling the function
load_data()
