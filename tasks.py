#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector, os, http.cookies
cgitb.enable()
import header_exec

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
empid = form.getvalue("empid")

# fallback: cookie
if not empid:
    cookies = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE", ""))
    empid = cookies["empid"].value if "empid" in cookies else None

if not empid:
    print("<script>alert('Session expired. Please log in again.');location.href='worker_login.py';</script>")
    raise SystemExit

try:
    empid = int(empid)
except ValueError:
    print("<script>alert('Invalid ID');location.href='worker_login.py';</script>")
    raise SystemExit

db = mysql.connector.connect(host="localhost", user="root", password="", database="drw")
cur = db.cursor(dictionary=True)

# Validate worker
cur.execute("SELECT * FROM employee_master WHERE id=%s AND role='Executive' AND status='Active'", (empid,))
worker = cur.fetchone()
if not worker:
    print("<script>alert('Worker not found');location.href='worker_login.py';</script>")
    raise SystemExit

print(f"""
<div class="main-content">
 <div class="page-content">
  <div class="container-fluid">
    <h3>Welcome {worker['name']} (ID: {worker['id']})</h3>
    
    <hr>
    <h4>Task Assignment List</h4>
    <div class="table-responsive">
    <table class="table table-bordered">
      <thead>
        <tr>
          <th>ID</th>
          <th>Title</th>
          <th>Description</th>
          <th>Category</th>
          <th>Date Assign</th>
          <th>Due Date</th>
          <th>Status</th>
          <th>Report</th>
        </tr>
      </thead>
      <tbody>
""")

# Fetch only this worker’s tasks
cur.execute("""
    SELECT t.id, t.title, t.description, t.date_assign, t.due_date, t.status,
           c.category_name
    FROM task_assignment t
    LEFT JOIN task_category_master c ON t.task_category_id = c.id
    WHERE t.assign_to = %s
""", (empid,))
rows = cur.fetchall()

if rows:
    for r in rows:
        print(f"""
          <tr>
            <td>{r['id']}</td>
            <td>{r['title']}</td>
            <td>{r['description']}</td>
            <td>{r['category_name'] or ''}</td>
            <td>{r['date_assign'] or ''}</td>
            <td>{r['due_date'] or ''}</td>
            <td>{r['status']}</td>
            <td>
              <a href="workreport.py?task_id={r['id']}&empid={empid}" class="btn btn-success btn-sm">Report</a>
            </td>
          </tr>
        """)
else:
    print("""
          <tr>
            <td colspan="8" class="text-center text-muted">No tasks assigned to you.</td>
          </tr>
    """)

print("""
      </tbody>
    </table>
    </div>
  </div>
 </div>
</div>
""")

import footer
