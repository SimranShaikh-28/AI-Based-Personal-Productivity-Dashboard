#!C:\Python310\python.exe
import cgi
import cgitb
import mysql.connector

cgitb.enable()
print("Content-Type: text/html\n")


formdata = cgi.FieldStorage()
username = formdata.getvalue("username")
userpassword = formdata.getvalue("userpassword")

#print(username)
#print(userpassword)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password='',
    database="task" 
)

mycursor = mydb.cursor(dictionary=True)

query =f"""select * from login where email = '{username}' AND password='{userpassword}'"""
mycursor.execute(query)
mydata = mycursor.fetchone()
# print(mydata)

if mycursor.rowcount == 1:
       print('Ok Login')
   
else :
      print('''
    <script>
      alert("Login Failed");
      location.href="login.py";
      </script>
      ''')

      # want to show lat long google map query kolhapur lat long zoom level 16
      # simple url to show on google map browser