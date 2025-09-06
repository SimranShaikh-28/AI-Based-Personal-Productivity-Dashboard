#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
import header_exec
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
leave_id = form.getvalue("id")

if not leave_id:
    print("<script>alert('Invalid leave ID.');window.location='worker_leave.py';</script>")
    raise SystemExit

db = mysql.connector.connect(host="localhost", user="root", password="", database="drw")
cur = db.cursor(dictionary=True)

# Fetch leave application
cur.execute("""
    SELECT l.id, l.leave_type_id, l.from_date, l.to_date, l.reason, l.status
    FROM leave_master l
    WHERE l.id = %s
""", (leave_id,))
leave = cur.fetchone()

if not leave:
    print("<script>alert('Leave application not found.');window.location='worker_leave.py';</script>")
    raise SystemExit

# Fetch leave types for dropdown
cur.execute("SELECT id, leave_type FROM leave_type_master")
leave_types = cur.fetchall()

print(f'''
<div class="main-content">
 <div class="page-content">
  <div class="container-fluid">

    <div class="row">
      <div class="col-12">
        <div class="page-title-box d-flex align-items-center justify-content-between">
          <h4 class="mb-0">Edit Leave Application</h4>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-lg-12">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Update Leave</h4>

            <form method="post" action="worker_leave_update.py">
              <input type="hidden" name="id" value="{leave['id']}">

              <div class="row align-items-start">
                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Leave Type</label>
                    <select name="leave_type_id" class="form-control form-control-sm" style="border:1px solid black !important;">
''')

for lt in leave_types:
    selected = "selected" if lt["id"] == leave["leave_type_id"] else ""
    print(f"<option value='{lt['id']}' {selected}>{lt['leave_type']}</option>")

print(f'''
                    </select>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">From Date</label>
                    <input type="date" name="from_date" value="{leave['from_date']}" 
                           class="form-control form-control-sm" style="border:1px solid black !important;" required>
                  </div>
                </div>
              </div>

              <div class="row align-items-start">
                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">To Date</label>
                    <input type="date" name="to_date" value="{leave['to_date']}" 
                           class="form-control form-control-sm" style="border:1px solid black !important;" required>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Reason</label>
                    <textarea name="reason" class="form-control form-control-sm" 
                              style="border:1px solid black !important;">{leave['reason']}</textarea>
                  </div>
                </div>
              </div>

              <button type="submit" class="btn btn-primary">Update</button>
              <a href="worker_leave.py" class="btn btn-secondary">Cancel</a>
            </form>

          </div>
        </div>
      </div>
    </div>

  </div>
 </div>
</div>
''')

import footer
