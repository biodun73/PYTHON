import mysql.connector
dbcon = mysql.connector.connect(host="localhost",user="root",password="", database="pythontest")
dbcreate = dbcon.cursor()
dbcreate.execute("SELECT * FROM logins")
fetch = dbcreate.fetchone()
for x in fetch:
    print(x)