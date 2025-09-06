#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
id = form.getvalue("id")
designation_name = form.getvalue("designation_name")
description = form.getvalue("description")

mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor()

query = "UPDATE designation_master SET designation_name=%s, description=%s WHERE id=%s"
cur.execute(query, (designation_name, description, id))
mydb.commit()

print('''
<script>
    alert("Designation updated successfully!");
    location.href="designationlist.py";
</script>
''')
