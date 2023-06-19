import mysql.connector
dbcon = mysql.connector.connect(host="localhost",user="root",password="")
dbcreate = dbcon.cursor()
dbcreate.execute("CREATE DATABASE pythontest")
