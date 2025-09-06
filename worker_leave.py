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
    <h4>My Leave Applications</h4>
    <div class="table-responsive">
    <table class="table table-bordered">
      <thead>
        <tr>
          <th>ID</th>
          <th>Leave Type</th>
          <th>From Date</th>
          <th>To Date</th>
          <th>Reason</th>
          <th>Status</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
""")

# Fetch only this worker’s leave applications
cur.execute("""
    SELECT l.id, l.from_date, l.to_date, l.reason, l.status, lt.leave_type
    FROM leave_master l
    JOIN leave_type_master lt ON l.leave_type_id = lt.id
    WHERE l.emp_id = %s
    ORDER BY l.id DESC
""", (empid,))
rows = cur.fetchall()

if rows:
    for r in rows:
        print(f"""
          <tr>
            <td>{r['id']}</td>
            <td>{r['leave_type']}</td>
            <td>{r['from_date']}</td>
            <td>{r['to_date']}</td>
            <td>{r['reason']}</td>
            <td>{r['status']}</td>
            <td>
              <a href="worker_leave_edit.py?id={r['id']}" class="btn btn-sm btn-warning">Edit</a>
              <a href="worker_leave_delete.py?id={r['id']}" class="btn btn-sm btn-danger" onclick="return confirm('Delete this leave application?');">Delete</a>
            </td>
          </tr>
        """)
else:
    print("""
          <tr>
            <td colspan="7" class="text-center text-muted">No leave applications found.</td>
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
