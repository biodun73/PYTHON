import mysql.connector
dbcon = mysql.connector.connect(host="localhost",user="root",password="", database="pythontest")
createtable = dbcon.cursor()
createtable.execute("CREATE TABLE logins (username VARCHAR(255), password VARCHAR(255))")
createtable.execute("ALTER TABLE logins ADD COLUMN INT PRIMARY KEY AUTO_INCREMENT")
