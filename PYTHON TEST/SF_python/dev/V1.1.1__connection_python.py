import os
import snowflake.connector
from snowflake.connector import *
import pandas as pd
from snowflake.connector.pandas_tools import write_pandas
import PYTHON_TEST.SF_python.testes.connection

# C:\Users\Celia.A.Pereira\Desktop\Devop - git\Pipeline_SF\PYTHON TEST\SF_python\testes\connection.py

# SF_python\testes\connection.py


# print(SF_python\testes\connection.py)


# print(df_drop)
# account = os.environ['SF_ACCOUNT']
# password = os.environ['SF_PASSWORD']
# username= os.environ['SF_USERNAME']


# # print(f"SF ACCOUNT IS:  {account}")
# # print(f"SF PASSWORD IS:  {password}")
# # print(f"SF USERNAME IS:  {username}")

# print("Estamos na pasta dev")

# conn = snowflake.connector.connect (
#     user=username,
#     password=password,
#     account=account

# )
# cursor = conn.cursor()

# conn.cursor().execute("USE WAREHOUSE COMPUTE_WH;")

# conn.cursor().execute("CREATE OR REPLACE SCHEMA DEV.REPORT; ")

# conn.cursor().execute(""" CREATE TABLE DEV.REPORT.TITANIC_REPORT (
#     PASSENGERID INT,
#     SURVIVED INT, 
#     PCLASS INT, 
#     SEX VARCHAR(6), 
#     AGE INT, 
#     SIBSP INT, 
#     PARCH INT, 
#     AGERANGE VARCHAR(5)
#     )""")


# success, num_chunks, num_rows, output = write_pandas(
#             conn=conn,
#             df=d.df_drop,
#             table_name='TITANIC_REPORT',
#             database='DEV',
#             schema='REPORT'
#         )
# cursor.close()

