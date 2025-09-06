#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
import header
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
id = form.getvalue("id")

# DB connection
mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor(dictionary=True)

# Fetch employee record
cur.execute("SELECT * FROM employee_master WHERE id=%s", (id,))
emp = cur.fetchone()

# Fetch dropdown values
cur.execute("SELECT id, department_name FROM department_master")
departments = cur.fetchall()

cur.execute("SELECT id, designation_name FROM designation_master")
designations = cur.fetchall()

print(f'''
<div class="main-content">
 <div class="page-content">
  <div class="container-fluid">

    <div class="row">
      <div class="col-12">
        <div class="page-title-box d-flex align-items-center justify-content-between">
          <h4 class="mb-0">Edit Employee</h4>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-lg-12">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Update Employee</h4>

            <form method="post" action="employeeupdate.py">
              <input type="hidden" name="id" value="{emp['id']}">

              <div class="row align-items-start">

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Name</label>
                    <input type="text" name="name" value="{emp['name']}"
                      class="form-control form-control-sm" 
                      style="border:1px solid black !important;" 
                      required pattern="[A-Za-z ]{{2,50}}">
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Email</label>
                    <input type="email" name="email" value="{emp['email']}"
                      class="form-control form-control-sm" 
                      style="border:1px solid black !important;" required>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Password</label>
                    <input type="password" name="password" value="{emp['password']}"
                      class="form-control form-control-sm" 
                      style="border:1px solid black !important;" required>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Street</label>
                    <input type="text" name="street" value="{emp['street']}"
                      class="form-control form-control-sm" 
                      style="border:1px solid black !important;" required>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">City</label>
                    <input type="text" name="city" value="{emp['city']}"
                      class="form-control form-control-sm" 
                      style="border:1px solid black !important;" required>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Pincode</label>
                    <input type="text" name="pincode" value="{emp['pincode']}"
                      class="form-control form-control-sm" 
                      style="border:1px solid black !important;" required>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">State</label>
                    <input type="text" name="state" value="{emp['state']}"
                      class="form-control form-control-sm" 
                      style="border:1px solid black !important;" required>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Designation</label>
                    <select name="designation_id" class="form-control form-control-sm" style="border:1px solid black !important;" required>
''')

for d in designations:
    selected = "selected" if d['id'] == emp['designation_id'] else ""
    print(f"<option value='{d['id']}' {selected}>{d['designation_name']}</option>")

print('''
                    </select>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Department</label>
                    <select name="department_id" class="form-control form-control-sm" style="border:1px solid black !important;" required>
''')

for dep in departments:
    selected = "selected" if dep['id'] == emp['department_id'] else ""
    print(f"<option value='{dep['id']}' {selected}>{dep['department_name']}</option>")

print(f'''
                    </select>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Role</label>
                    <select name="role" class="form-control form-control-sm" style="border:1px solid black !important;" required>
                      <option value="Manager" {"selected" if emp['role']=="Manager" else ""}>Manager</option>
                      <option value="Executive" {"selected" if emp['role']=="Executive" else ""}>Executive</option>
                    </select>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Status</label>
                    <select name="status" class="form-control form-control-sm" style="border:1px solid black !important;" required>
                      <option value="Active" {"selected" if emp['status']=="Active" else ""}>Active</option>
                      <option value="Inactive" {"selected" if emp['status']=="Inactive" else ""}>Inactive</option>
                    </select>
                  </div>
                </div>

              </div>
              <button type="submit" class="btn btn-primary">Update</button>
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
