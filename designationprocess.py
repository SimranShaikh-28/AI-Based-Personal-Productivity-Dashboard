#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")

formdata = cgi.FieldStorage()
designation_name = formdata.getvalue("designation_name")
description = formdata.getvalue("description")

mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor()
query = f"""INSERT INTO designation_master(designation_name, description) 
            VALUES ('{designation_name}','{description}')"""
print(query)

cur.execute(query)
mydb.commit()

print('''
<script>
    alert("Designation saved successfully!");
    location.href="designationlist.py";
</script>
''')
