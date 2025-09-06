#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")

formdata = cgi.FieldStorage()
department_name = formdata.getvalue("department_name")
description = formdata.getvalue("description")

mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor()
query = f"""INSERT INTO department_master(department_name, description) 
            VALUES ('{department_name}','{description}')"""
print(query)

cur.execute(query)
mydb.commit()

print('''
<script>
    alert("Department saved successfully!");
    location.href="departmentlist.py";
</script>
''')
