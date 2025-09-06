#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
id          = form.getvalue("id")
name        = form.getvalue("name")
email       = form.getvalue("email")
password    = form.getvalue("password")
street      = form.getvalue("street")
city        = form.getvalue("city")
pincode     = form.getvalue("pincode")
state       = form.getvalue("state")
designation = form.getvalue("designation_id")
department  = form.getvalue("department_id")
role        = form.getvalue("role")
status      = form.getvalue("status")

mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor()

query = """UPDATE employee_master 
           SET name=%s, email=%s, password=%s, street=%s, city=%s, pincode=%s, state=%s, 
               designation_id=%s, department_id=%s, role=%s, status=%s 
           WHERE id=%s"""
cur.execute(query, (name, email, password, street, city, pincode, state, designation, department, role, status, id))
mydb.commit()

print('''
<script>
    alert("Employee updated successfully!");
    location.href="employeelist.py";
</script>
''')
