#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector, os, http.cookies
cgitb.enable()
import header_exec
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
empid = form.getvalue("empid")

# --- fallback: cookie ---
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

# --- DB connection ---
mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor(dictionary=True)

# --- Validate worker ---
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
    <h4>My Work Reports</h4>
    <div class="table-responsive">
    <table class="table table-bordered">
      <thead>
        <tr>
          <th>ID</th>
          <th>Task</th>
          <th>Client</th>
          <th>Category</th>
          <th>Description</th>
          <th>Date</th>
          <th>Status</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
""")

# --- Fetch only this worker’s work reports ---
query = """
    SELECT w.id, w.description, w.date, w.status,
           t.title AS task_title,
           c.client_name,
           cat.category_name
    FROM work_report w
    LEFT JOIN task_assignment t ON w.task_id = t.id
    LEFT JOIN client_master c ON w.client_id = c.id
    LEFT JOIN task_category cat ON w.category_id = cat.id
    WHERE w.emp_id = %s
    ORDER BY w.id DESC
"""
cur.execute(query, (empid,))
rows = cur.fetchall()

if rows:
    for r in rows:
        print(f"""
          <tr>
            <td>{r['id']}</td>
            <td>{r['task_title'] or ''}</td>
            <td>{r['client_name'] or ''}</td>
            <td>{r['category_name'] or ''}</td>
            <td>{r['description'] or ''}</td>
            <td>{r['date'] or ''}</td>
            <td>{r['status']}</td>
            <td>
              <a href="workreportedit.py?id={r['id']}" class="btn btn-primary btn-sm me-2">Edit</a>
              <a href="workreportdelete.py?id={r['id']}" class="btn btn-danger btn-sm" onclick="return confirm('Are you sure?');">Delete</a>
            </td>
          </tr>
        """)
else:
    print("""
          <tr>
            <td colspan="8" class="text-center text-muted">No work reports submitted yet.</td>
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
