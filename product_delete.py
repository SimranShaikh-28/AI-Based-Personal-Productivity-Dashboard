#!C:\Python310\python.exe
import cgi
import cgitb
import mysql.connector

cgitb.enable()

print("Content-Type: text/html\n")

formdata = cgi.FieldStorage()
id = formdata.getvalue("id")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password='',
    database="sale"
)
mycursor = mydb.cursor()

query = f"DELETE FROM products WHERE id = {id}"
mycursor.execute(query)
mydb.commit()

print(f"Product with ID {id} has been deleted successfully.")