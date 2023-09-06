import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'tiger'

)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE swastiks")

print("All done!")