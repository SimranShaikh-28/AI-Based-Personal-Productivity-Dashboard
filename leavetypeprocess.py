#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")

formdata = cgi.FieldStorage()
leave_type = formdata.getfirst("leave_type")
description = formdata.getfirst("description")

mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor()

query = """INSERT INTO leave_type_master(leave_type, description) VALUES (%s, %s)"""
cur.execute(query, (leave_type, description))
mydb.commit()

print('''
<script>
    alert("Leave Type saved successfully!");
    location.href="leavetypelist.py";
</script>
''')
