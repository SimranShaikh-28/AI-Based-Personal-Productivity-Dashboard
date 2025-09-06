#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("userpassword")
role = form.getvalue("role")
status = form.getvalue("status")

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="task"
    )
    cursor = conn.cursor()

    query = "INSERT INTO employees (name, password, role, status) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (username, password, role, status))
    conn.commit()

    print('''
    <script>
        alert("Registration Successful! You can now login.");
        location.href="admin_login.py";
    </script>
    ''')
except mysql.connector.Error as e:
    print(f"<h3>Database Error: {e}</h3>")
finally:
    if 'cursor' in locals(): cursor.close()
    if 'conn' in locals() and conn.is_connected(): conn.close()
