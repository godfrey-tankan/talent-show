import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'tanatswa123'
	)
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE employees")

print("All set!.")