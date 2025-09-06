#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector, os, http.cookies
cgitb.enable()
import header_exec
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

# --- Fetch the work report (must belong to this employee) ---
cur.execute("SELECT * FROM work_report WHERE id=%s AND emp_id=%s", (report_id, empid))
report = cur.fetchone()
if not report:
    print("<script>alert('Unauthorized access: You can only edit your own reports.');location.href='workreportlist.py';</script>")
    raise SystemExit

# --- Dropdown data ---
cur.execute("SELECT id, title FROM task_assignment WHERE assign_to=%s", (empid,))
tasks = cur.fetchall()

cur.execute("SELECT id, client_name FROM client_master WHERE status='Active'")
clients = cur.fetchall()

cur.execute("SELECT id, category_name FROM task_category")
categories = cur.fetchall()

print(f"""
<div class="main-content">
 <div class="page-content">
  <div class="container-fluid">
    <h3>Edit Work Report (Welcome {worker['name']})</h3>
    <div class="card">
      <div class="card-body">
        <form method="post" action="workreportupdate.py">
          <input type="hidden" name="id" value="{report['id']}">
          <input type="hidden" name="emp_id" value="{empid}">
          <div class="row">
""")

# --- Task ---
print("""<div class="col-lg-6 mb-3"><label>Task</label>
<select name="task_id" class="form-control" required>""")
for t in tasks:
    sel = "selected" if t["id"] == report["task_id"] else ""
    print(f"<option value='{t['id']}' {sel}>{t['title']}</option>")
print("</select></div>")

# --- Client ---
print("""<div class="col-lg-6 mb-3"><label>Client</label>
<select name="client_id" class="form-control" required>""")
for c in clients:
    sel = "selected" if c["id"] == report["client_id"] else ""
    cname = c["client_name"] if c["client_name"] else f"Client #{c['id']}"
    print(f"<option value='{c['id']}' {sel}>{cname}</option>")
print("</select></div>")

# --- Category ---
print("""<div class="col-lg-6 mb-3"><label>Task Category</label>
<select name="category_id" class="form-control" required>""")
for cat in categories:
    sel = "selected" if cat["id"] == report["category_id"] else ""
    print(f"<option value='{cat['id']}' {sel}>{cat['category_name']}</option>")
print("</select></div>")

# --- Description ---
print(f"""
<div class="col-lg-12 mb-3">
 <label>Work Description</label>
 <textarea name="description" class="form-control" required>{report['description'] or ''}</textarea>
</div>
""")

# --- Date ---
print(f"""
<div class="col-lg-6 mb-3">
 <label>Date</label>
 <input type="date" name="date" value="{report['date']}" class="form-control" required>
</div>
""")

# --- Status ---
print(f"""
<div class="col-lg-6 mb-3">
 <label>Status</label>
 <select name="status" class="form-control" required>
   <option value="Pending" {"selected" if report['status']=="Pending" else ""}>Pending</option>
   <option value="Completed" {"selected" if report['status']=="Completed" else ""}>Completed</option>
   <option value="Partial" {"selected" if report['status']=="Partial" else ""}>Partial</option>
 </select>
</div>
""")

print("""
<div class="col-12">
 <button type="submit" class="btn btn-primary">Update Report</button>
</div>
</div> <!-- row -->
</form>
</div>
</div>
</div>
</div>
</div>
""")

import footer
