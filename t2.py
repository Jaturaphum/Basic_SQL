from datetime import date
from importlib.metadata import distribution
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="longuser",
  password="longuser"
)

mycursor=mydb.cursor(dictionary=True)
sql="INSERT INTO hard_ware (name, hw_name, status, value) VALUES ('A3', 'light', 'OFF', 0.00)"
mycursor.execute(sql)
mydb.commit()
ID=mycursor.lastrowid
print(f"ID :{ID}" )
print(mycursor.rowcount, "record inserted.")
