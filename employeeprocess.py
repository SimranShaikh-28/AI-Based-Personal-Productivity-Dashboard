#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
name         = form.getvalue("name")
email        = form.getvalue("email")
password     = form.getvalue("password")
street       = form.getvalue("street")
city         = form.getvalue("city")
pincode      = form.getvalue("pincode")
state        = form.getvalue("state")
designation  = form.getvalue("designation_id")
department   = form.getvalue("department_id")
role         = form.getvalue("role")
status       = form.getvalue("status")

mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor()
query = f"""INSERT INTO employee_master
(name,email,password,street,city,pincode,state,designation_id,department_id,role,status)
VALUES ('{name}','{email}','{password}','{street}','{city}','{pincode}','{state}','{designation}','{department}','{role}','{status}')"""
print(query)

cur.execute(query)
mydb.commit()

print('''
<script>
    alert("Employee saved successfully!");
    location.href="employeelist.py";
</script>
''')
