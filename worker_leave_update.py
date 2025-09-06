#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
leave_id = form.getvalue("id")
leave_type_id = form.getvalue("leave_type_id")
from_date = form.getvalue("from_date")
to_date = form.getvalue("to_date")
reason = form.getvalue("reason")

if not (leave_id and leave_type_id and from_date and to_date):
    print("<script>alert('All fields are required.');window.location='worker_leave.py';</script>")
    raise SystemExit

try:
    db = mysql.connector.connect(host="localhost", user="root", password="", database="drw")
    cur = db.cursor()

    cur.execute("""
        UPDATE leave_master
        SET leave_type_id=%s, from_date=%s, to_date=%s, reason=%s, status='Pending'
        WHERE id=%s
    """, (leave_type_id, from_date, to_date, reason.strip(), leave_id))
    db.commit()

    print("<script>alert('Leave application updated successfully.');window.location='worker_leave.py';</script>")
except Exception as e:
    print(f"<script>alert('Error updating leave: {e}');window.location='worker_leave.py';</script>")
