import configparser

from create_ini_sql import run_me
from configparser import ConfigParser

import pandas as pd
import numpy as np
import mysql.connector as sql

import snowflake.connector
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine

def mysql():
    config_writer = configparser.ConfigParser()

    host = input("Enter the host name: ")
    database = input("Enter the database name you want to use: ")
    user =input("enter thr user name: ")
    password = input("Enter the correct passwod: ")
    quary = input("Enter the Tbale you are using: ")
    config_writer['account']={}
    config_writer["account"]['host']= host
    config_writer["account"]['database']= database
    config_writer["account"]['user']= user
    config_writer["account"]['password']= password
    config_writer["account"]['quary']= quary
    file_name = input("Enter the file name you want to save: ")
    print(file_name)
    with open(file_name+".ini", 'w') as configfile:
        config_writer.write(configfile)
        #return(host, database, user, password, quary, file_name)
    print(host, database, user, password, quary, file_name)
    file = file_name + ".ini"
    config = ConfigParser()
    print(config.read(file))
    table_name = config["account"]["quary"]
    db_connection = sql.connect(host= config['account']['host'], 
                                database=config['account']['database'], 
                                user=config['account']['user'], 
                                password=config['account']['password'])
    db_cursor = db_connection.cursor()
    query = """select * from"""+""" """+ table_name+""";"""
    df = pd.read_sql(sql=query, con=db_connection)
    print(df.head())

def snowflake():
    config_writer = configparser.ConfigParser()

    user = input("Enter the username: ")
    password = input("Enter the password: ")
    account =input("enter thr user name: ")
    warehouse = input("Enter the warehouse you want to use: ")
    database = input("Enter the Database name: ")
    schema = input("Enter the schema name: ")
    role = input("Enter the role using: ")
    quary = input("enter the quary you want to use: ")
    config_writer['account']={}
    config_writer["account"]['user']= user
    config_writer["account"]['password']= password
    config_writer["account"]['account']= account
    config_writer["account"]['warehouse']= warehouse
    config_writer["account"]['database']= database
    config_writer["account"]['schema']= schema
    config_writer["account"]['role']= role
    config_writer["account"]['quary']= quary
    file_name = input("Enter the file name you want to save: ")
    file = "snowflake.ini"
    config = ConfigParser()
    print(config.read(file))
    file = "snowflake.ini"
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
    query = "select * from "+ quary +";"
    df = pd.read_sql(query, connection)
 
    print(df.head())

def sql_server():
    print("sql server")

def postgre():
    print("Postgre SQL")


database_name =input('''ENter the database you want to use
                        1. mysql 
                        2. snowflake
                        3. SQL server 
                        4. postgre SQL
                        ''')

if database_name == "1":
    mysql()
elif database_name == "2":
    snowflake()
elif database_name == "3":
    sql_server()
elif database_name == "4":
    postgre()
else:
    print("Select only 1 dude :)")
