#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector, os, http.cookies
cgitb.enable()
import header_exec

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
task_id = form.getvalue("task_id")

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
mydb = mysql.connector.connect(host="localhost", user="root", password="", database="drw")
cur = mydb.cursor(dictionary=True)

# --- Get logged-in worker ---
cur.execute("SELECT * FROM employee_master WHERE id=%s AND role='Executive' AND status='Active'", (empid,))
worker = cur.fetchone()
if not worker:
    print("<script>alert('Worker not found');location.href='worker_login.py';</script>")
    raise SystemExit

# --- Get dropdown data ---
cur.execute("SELECT id, title FROM task_assignment WHERE assign_to=%s", (empid,))
tasks = cur.fetchall()

cur.execute("SELECT id, client_name FROM client_master WHERE status='Active'")
clients = cur.fetchall()

cur.execute("SELECT id, category_name FROM task_category")
categories = cur.fetchall()


print('''
<div class="main-content">
  <div class="page-content">
    <div class="container-fluid">
      <h4 class="mb-0">Apply for Leave</h4>

      <form method="post" action="leave_process.py" class="mt-3">
        <div class="row">
''')

db = mysql.connector.connect(host="localhost", user="root", password="", database="drw")
cur = db.cursor(dictionary=True)

# Employee dropdown

print(f"""
<div class="col-lg-6 mb-3">
 <label>Employee</label>
 <input type="text" class="form-control" value="{worker['name']}" readonly>
</div>
""")

# Leave type dropdown
print('''
<div class="col-lg-6 mb-3">
  <label class="form-label">Leave Type</label>
  <select name="leave_type_id" class="form-control" style="border:1px solid black !important;">
''')
cur.execute("SELECT id, leave_type FROM leave_type_master")
for lt in cur.fetchall():
    print(f"<option value='{lt['id']}'>{lt['leave_type']}</option>")
print("</select></div>")

# Leave from_date
print('''
<div class="col-lg-6 mb-3">
  <label class="form-label">From Date</label>
  <input type="date" name="from_date" class="form-control form-control-sm" style="border:1px solid black !important;">
</div>
''')

# Leave to_date
print('''
<div class="col-lg-6 mb-3">
  <label class="form-label">To Date</label>
  <input type="date" name="to_date" class="form-control form-control-sm" style="border:1px solid black !important;">
</div>
''')


# Reason
print('''
<div class="col-lg-12 mb-3">
  <label class="form-label">Reason</label>
  <textarea name="reason" class="form-control form-control-sm" style="border:1px solid black !important;"></textarea>
</div>
''')

# Submit button
print('''
<div class="col-lg-12">
  <button type="submit" class="btn btn-success">Apply Leave</button>
</div>

</div>
</form>
    </div>
  </div>
</div>
''')

import footer
