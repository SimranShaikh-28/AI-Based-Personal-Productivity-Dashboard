#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
id          = form.getvalue("id")
leave_type  = form.getvalue("leave_type")
description = form.getvalue("description")

mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor()

query = "UPDATE leave_type_master SET leave_type=%s, description=%s WHERE id=%s"
cur.execute(query, (leave_type, description, id))
mydb.commit()

print('''
<script>
    alert("Leave Type updated successfully!");
    location.href="leavetypelist.py";
</script>
''')
