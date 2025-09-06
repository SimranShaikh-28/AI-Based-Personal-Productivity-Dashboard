#!C:\Python310\python.exe
import cgitb, mysql.connector
cgitb.enable()
import header

print("Content-Type: text/html\n")

print('''
<div class="main-content">
  <div class="page-content">
    <div class="container-fluid">
      <h4 class="mb-0">Leave Applications</h4>

      <table class="table table-bordered">
        <thead>
          <tr>
            <th>ID</th>
            <th>Employee</th>
            <th>Leave Type</th>
            <th>From Date</th>
            <th>To Date</th>
            <th>Reason</th>
            <th>Status</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
''')

db = mysql.connector.connect(host="localhost", user="root", password="", database="drw")
cur = db.cursor(dictionary=True)

cur.execute("""
    SELECT l.id, e.name AS emp_name, lt.leave_type,
           l.from_date, l.to_date, l.reason, l.status
    FROM leave_master l
    JOIN employee_master e ON l.emp_id = e.id
    JOIN leave_type_master lt ON l.leave_type_id = lt.id
    ORDER BY l.id DESC
""")
for row in cur.fetchall():
    print(f"""
      <tr>
        <td>{row['id']}</td>
        <td>{row['emp_name']}</td>
        <td>{row['leave_type']}</td>
        <td>{row['from_date']}</td>
        <td>{row['to_date']}</td>
        <td>{row['reason']}</td>
        <td>{row['status']}</td>
        <td>
          <a href='leave_approve.py?id={row['id']}&status=Approved' class='btn btn-sm btn-success'>Approve</a>
          <a href='leave_approve.py?id={row['id']}&status=Rejected' class='btn btn-sm btn-danger'>Reject</a>
        </td>
      </tr>
    """)

print('''
        </tbody>
      </table>
    </div>
  </div>
</div>
''')

import footer
