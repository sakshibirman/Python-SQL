import os
import sqlite3
from sqlite3.dbapi2 import OperationalError
import pandas as pd
from pandas._libs import missing

def connectDB(DB_name):
    global conn
    global curr
    conn = sqlite3.connect(DB_name)
    curr = conn.cursor()

def dataSQL(dataLoc, tableName):
    df = pd.read_csv(dataLoc)
    df.to_sql(tableName, conn)
    print("Data added succesfully!!!")