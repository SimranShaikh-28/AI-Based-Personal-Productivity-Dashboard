#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
leave_id = form.getfirst("id")
status   = form.getfirst("status")

if leave_id and status:
    db = mysql.connector.connect(host="localhost", user="root", password="", database="drw")
    cur = db.cursor()
    cur.execute("UPDATE leave_master SET status=%s WHERE id=%s", (status, leave_id))
    db.commit()

print(f'''
<script>
    alert("Leave updated to {status}!");
    location.href="leaveapplication.py";
</script>
''')
