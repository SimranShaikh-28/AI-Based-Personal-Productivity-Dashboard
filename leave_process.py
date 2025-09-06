#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector, os, http.cookies
cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()

# --- Get empid from query or cookie ---
empid = form.getvalue("empid")
if not empid:
    cookies = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE", ""))
    empid = cookies["empid"].value if "empid" in cookies else None

if not empid:
    print("<script>alert('Session expired. Please log in again.');location.href='worker_login.py';</script>")
    raise SystemExit

try:
    empid = int(empid)
except ValueError:
    print("<script>alert('Invalid session.');location.href='worker_login.py';</script>")
    raise SystemExit

# --- Collect form inputs ---
leave_type_id = form.getfirst("leave_type_id")
from_date = form.getfirst("from_date")
to_date = form.getfirst("to_date")
reason = form.getfirst("reason")

# --- Validate ---
if not (leave_type_id and from_date and to_date and reason):
    print("<script>alert('All fields are required.');history.back();</script>")
    raise SystemExit

# --- DB Connection ---
db = mysql.connector.connect(host="localhost", user="root", password="", database="drw")
cur = db.cursor()

# --- Insert leave application ---
query = """
INSERT INTO leave_master (emp_id, leave_type_id, from_date, to_date, reason, status)
VALUES (%s, %s, %s, %s, %s, %s)
"""
cur.execute(query, (empid, leave_type_id, from_date, to_date, reason, "Pending"))
db.commit()

print("""
<script>
    alert("Leave application submitted successfully!");
    location.href="worker_leave.py";
</script>
""")
