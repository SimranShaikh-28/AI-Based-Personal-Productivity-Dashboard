#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
id            = form.getvalue("id")
category_name = form.getvalue("category_name")
description   = form.getvalue("description")

mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor()

query = "UPDATE task_category_master SET category_name=%s, description=%s WHERE id=%s"
cur.execute(query, (category_name, description, id))
mydb.commit()

print('''
<script>
    alert("Task Category updated successfully!");
    location.href="taskcategorylist.py";
</script>
''')
