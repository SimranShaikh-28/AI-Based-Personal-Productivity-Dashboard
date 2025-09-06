#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
id = form.getvalue("id")

mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor()

# 1. Delete selected row
query = "DELETE FROM task_category_master WHERE id=%s"
cur.execute(query, (id,))
mydb.commit()

# 2. Reset AUTO_INCREMENT so next id continues from max(id)+1
reset = "ALTER TABLE task_category_master AUTO_INCREMENT = 1"
cur.execute(reset)
mydb.commit()

print('''
<script>
    alert("Task Category deleted successfully and ID reset!");
    location.href="taskcategorylist.py";
</script>
''')
