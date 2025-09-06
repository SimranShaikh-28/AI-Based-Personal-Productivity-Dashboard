#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector, os, http.cookies
cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
report_id = form.getvalue("id")

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

# --- DB connection ---
mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor(dictionary=True)

# --- Verify logged-in employee exists and is Executive ---
cur.execute("SELECT * FROM employee_master WHERE id=%s AND role='Executive' AND status='Active'", (empid,))
worker = cur.fetchone()
if not worker:
    print("<script>alert('Worker not found.');location.href='worker_login.py';</script>")
    raise SystemExit

# --- Check that the report belongs to this employee ---
cur.execute("SELECT * FROM work_report WHERE id=%s AND emp_id=%s", (report_id, empid))
report = cur.fetchone()
if not report:
    print("<script>alert('Unauthorized: You can only delete your own reports.');location.href='workreportlist.py';</script>")
    raise SystemExit

# --- Delete report ---
cur.execute("DELETE FROM work_report WHERE id=%s AND emp_id=%s", (report_id, empid))
mydb.commit()

print("""
<script>
  alert("Work Report deleted successfully!");
  window.location="workreportlist.py";
</script>
""")
