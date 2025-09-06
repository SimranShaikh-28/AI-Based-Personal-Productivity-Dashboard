#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()

form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("userpassword")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="drw"   # use drw DB, not sale
)
cursor = conn.cursor(dictionary=True)

query = """
SELECT * FROM employee_master
WHERE name=%s AND password=%s
  AND role='Manager' AND status='Active'
"""
cursor.execute(query, (username, password))
user = cursor.fetchone()

if user:
    # send cookies before Content-Type
    print(f"Set-Cookie: adminid={user['id']}; Path=/; HttpOnly")
    print(f"Set-Cookie: adminname={user['name']}; Path=/;")
    print("Content-Type: text/html\n")
    print("<script>alert('Welcome Admin!');location.href='admin_dashboard.py';</script>")
else:
    print("Content-Type: text/html\n")
    print("<script>alert('Admin Login Failed');location.href='admin_login.py';</script>")
