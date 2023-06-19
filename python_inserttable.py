import mysql.connector
dbcon = mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="pythontest"
)
dbinsert=dbcon.cursor()
insert = "INSERT INTO logins(username, password) VALUES(%s,%s)" 
values = ("john","12345")
dbinsert.execute(insert,values)
dbcon.commit()
print(dbinsert.rowcount,"data inserted")