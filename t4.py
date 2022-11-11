import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="longtest",
    password="longtest",
    database="longtest",
)

mycursor = mydb.cursor(dictionary=True)
sql = "DELETE FROM hard_ware WHERE id = 7"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record deleted.")