#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
leave_id = form.getvalue("id")

if not leave_id:
    print("<script>alert('Invalid leave ID.');window.location='worker_leave.py';</script>")
    raise SystemExit

try:
    db = mysql.connector.connect(host="localhost", user="root", password="", database="drw")
    cur = db.cursor()
    cur.execute("DELETE FROM leave_master WHERE id=%s", (leave_id,))
    db.commit()
    print("<script>alert('Leave application deleted.');window.location='worker_leave.py';</script>")
except Exception as e:
    print(f"<script>alert('Error deleting leave: {e}');window.location='worker_leave.py';</script>")
