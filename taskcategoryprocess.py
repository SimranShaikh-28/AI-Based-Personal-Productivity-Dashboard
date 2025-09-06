#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")

formdata = cgi.FieldStorage()
category_name = formdata.getvalue("category_name")
description = formdata.getvalue("description")

mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor()
query = f"""INSERT INTO task_category_master(category_name, description) 
            VALUES ('{category_name}','{description}')"""
print(query)

cur.execute(query)
mydb.commit()

print('''
<script>
    alert("Task Category saved successfully!");
    location.href="taskcategorylist.py";
</script>
''')
