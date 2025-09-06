#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()

# If you have an employee header, use it (keeps side menu etc.)
try:
    import header_exec as header_mod   # employee layout (if available)
except Exception:
    import header as header_mod        # fallback

print("Content-Type: text/html\n")

# DB
db = mysql.connector.connect(host="localhost", user="root", password="", database="drw")
cur = db.cursor(dictionary=True)

# Fetch dropdown data
cur.execute("SELECT id, name FROM employee_master WHERE status='Active' ORDER BY name")
employees = cur.fetchall()

cur.execute("SELECT id, leave_type FROM leave_type_master ORDER BY leave_type")
leave_types = cur.fetchall()

print('''
<div class="main-content">
  <div class="page-content">
    <div class="container-fluid">

      <div class="row">
        <div class="col-12">
          <div class="page-title-box d-flex align-items-center justify-content-between">
            <h4 class="mb-0">Apply for Leave</h4>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <h4 class="card-title">Leave Application</h4>

              <form method="post" action="leave_process.py" onsubmit="return validateDates();">
                <div class="row align-items-start">
''')

# Employee (if you use session, replace this with a hidden field)
print('''
                  <div class="col-lg-6">
                    <div class="mb-3">
                      <label class="form-label">Employee</label>
                      <select name="emp_id" class="form-control form-control-sm" required>
                        <option value="">-- Select Employee --</option>
''')
for e in employees:
    print(f'                        <option value="{e["id"]}">{e["name"]}</option>')
print('''
                      </select>
                    </div>
                  </div>
''')

# Leave Type
print('''
                  <div class="col-lg-6">
                    <div class="mb-3">
                      <label class="form-label">Leave Type</label>
                      <select name="leave_type_id" class="form-control form-control-sm" required>
                        <option value="">-- Select Leave Type --</option>
''')
for lt in leave_types:
    print(f'                        <option value="{lt["id"]}">{lt["leave_type"]}</option>')
print('''
                      </select>
                    </div>
                  </div>
''')

# From / To dates + Reason
print('''
                  <div class="col-lg-6">
                    <div class="mb-3">
                      <label class="form-label">From Date</label>
                      <input type="date" name="from_date" class="form-control form-control-sm" required>
                    </div>
                  </div>

                  <div class="col-lg-6">
                    <div class="mb-3">
                      <label class="form-label">To Date</label>
                      <input type="date" name="to_date" class="form-control form-control-sm" required>
                    </div>
                  </div>

                  <div class="col-lg-12">
                    <div class="mb-3">
                      <label class="form-label">Reason</label>
                      <textarea name="reason" class="form-control form-control-sm" rows="3" placeholder="Reason for leave" required></textarea>
                    </div>
                  </div>

                </div>

                <button type="submit" class="btn btn-primary">Submit</button>
                <a href="leave_list.py" class="btn btn-secondary ms-2">View My Requests</a>
              </form>

            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</div>

<script>
function validateDates() {
  var f = document.querySelector('[name="from_date"]').value;
  var t = document.querySelector('[name="to_date"]').value;
  if (!f || !t) return true;
  if (f > t) {
    alert("From Date cannot be after To Date.");
    return false;
  }
  return true;
}
</script>
''')

import footer  # keep your existing footer
