import pandas as pd
import mysql.connector 
con = mysql.connector.connect(host="localhost",user ="root",password = "",database="world")
pd.read_json("train.json")
pd.read_sql_query("SELECT* FROM country  WHERE LifeExpectancy > 60",con)
