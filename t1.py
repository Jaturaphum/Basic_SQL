import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="longtest",
    password="longtest",
    database="longtest",
)

mycursor = mydb.cursor(dictionary=True)

#sql = "SELECT name,hw_name,status,value,id FROM hard_ware"
sql = "SELECT * FROM hard_ware"

mycursor.execute(sql)
data = mycursor.fetchall()
print(data)
for i in data:
    print(i)

# sql = "SELECT * FROM hard_ware WHERE id = {}".format(ID)
# mycursor.execute(sql)
# data = mycursor.fetchall()
# print(data)
# for i in data:
#     print(i)