#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
id               = form.getvalue("id")
department_name  = form.getvalue("department_name")
description      = form.getvalue("description")

mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor()

query = """UPDATE department_master 
           SET department_name=%s, description=%s 
           WHERE id=%s"""
values = (department_name, description, id)

cur.execute(query, values)
mydb.commit()

print('''
<script>
    alert("Department updated successfully!");
    location.href="departmentlist.py";
</script>
''')
