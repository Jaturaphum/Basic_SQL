import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="longtest",
    password="longtest",
    database="longtest",
)

mycursor = mydb.cursor(dictionary=True)
sql = "UPDATE hard_ware SET status = 'ON' WHERE name = 'A1'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record updated.")