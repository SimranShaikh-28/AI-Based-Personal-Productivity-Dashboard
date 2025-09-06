#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
id = form.getvalue("id")

mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor()

query = "DELETE FROM leave_type_master WHERE id=%s"
cur.execute(query, (id,))
mydb.commit()

print('''
<script>
    alert("Leave Type deleted successfully!");
    location.href="leavetypelist.py";
</script>
''')
