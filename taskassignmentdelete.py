#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
id = form.getvalue("id")

mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor()

delete_sql = "DELETE FROM task_assignment WHERE id=%s"
cur.execute(delete_sql, (id,))
mydb.commit()

print("""
<script>
  alert("Task deleted successfully!");
  window.location="taskassignmentlist.py";
</script>
""")
