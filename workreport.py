#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector, os, http.cookies
import header_exec
cgitb.enable()
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

print(f"""
<div class="main-content">
 <div class="page-content">
  <div class="container-fluid">
    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Submit Work Report</h4>
            <form method="post" action="workreportprocess.py">
              <input type="hidden" name="emp_id" value="{empid}">
              <div class="row">
""")

# --- Employee (locked to logged-in) ---
print(f"""
<div class="col-lg-6 mb-3">
 <label>Employee</label>
 <input type="text" class="form-control" value="{worker['name']}" readonly>
</div>
""")

# --- Task (if coming from tasks.py, preselect) ---
print("""<div class="col-lg-6 mb-3"><label>Task</label>
<select name="task_id" class="form-control" required>""")
for t in tasks:
    sel = "selected" if str(t["id"]) == str(task_id) else ""
    print(f"<option value='{t['id']}' {sel}>{t['title']}</option>")
print("</select></div>")

# --- Client ---
print("""<div class="col-lg-6 mb-3"><label>Client</label>
<select name="client_id" class="form-control" required>
  <option value="">-- Select Client --</option>
""")
for c in clients:
    cname = c["client_name"] if c["client_name"] else f"Client #{c['id']}"
    print(f"<option value='{c['id']}'>{cname}</option>")
print("</select></div>")

# --- Category ---
print("""<div class="col-lg-6 mb-3"><label>Task Category</label>
<select name="category_id" class="form-control" required>
  <option value="">-- Select Category --</option>
""")
for cat in categories:
    print(f"<option value='{cat['id']}'>{cat['category_name']}</option>")
print("</select></div>")

# --- Description ---
print("""
<div class="col-lg-12 mb-3">
 <label>Work Description</label>
 <textarea name="description" class="form-control" required placeholder="Describe the work done..."></textarea>
</div>
""")

# --- Date ---
print(f"""
<div class="col-lg-6 mb-3">
 <label>Date</label>
 <input type="date" name="date" class="form-control" required>
</div>
""")

# --- Status ---
print("""
<div class="col-lg-6 mb-3">
 <label>Status</label>
 <select name="status" class="form-control" required>
   <option value="Pending" selected>Pending</option>
   <option value="Completed">Completed</option>
   <option value="Partial">Partial</option>
 </select>
</div>
""")


print("""
              </div> <!-- row -->
              <div class="col-12 mt-3">
                <button type="submit" class="btn btn-primary">Submit Report</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>

  </div> <!-- container-fluid -->
 </div> <!-- page-content -->
</div> <!-- main-content -->
""")

import footer

