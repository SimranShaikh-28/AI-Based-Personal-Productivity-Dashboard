#!C:\Python310\python.exe
import cgitb, mysql.connector
cgitb.enable()
import header
print("Content-Type: text/html\n")

# Get dropdown values
mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor(dictionary=True)

cur.execute("SELECT id, department_name FROM department_master")
departments = cur.fetchall()

cur.execute("SELECT id, designation_name FROM designation_master")
designations = cur.fetchall()

print('''
<div class="main-content">
 <div class="page-content">
  <div class="container-fluid">

    <div class="row">
      <div class="col-12">
        <div class="page-title-box d-flex align-items-center justify-content-between">
          <h4 class="mb-0">Add Employee</h4>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-lg-12">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Employee Form</h4>

            <form method="post" action="employeeprocess.py">
              <div class="row align-items-start">

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Name</label>
                    <input type="text" name="name" 
                      class="form-control form-control-sm" 
                      style="border:1px solid black !important;" 
                      required pattern="[A-Za-z ]{2,50}" 
                      title="Only letters allowed, min 2 characters">
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Email</label>
                    <input type="email" name="email" 
                      class="form-control form-control-sm" 
                      style="border:1px solid black !important;" required>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Password</label>
                    <input type="password" name="password" 
                      class="form-control form-control-sm" 
                      style="border:1px solid black !important;" 
                      required minlength="6" 
                      title="Minimum 6 characters">
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Street</label>
                    <input type="text" name="street" 
                      class="form-control form-control-sm" 
                      style="border:1px solid black !important;" 
                      minlength="3" required>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">City</label>
                    <input type="text" name="city" 
                      class="form-control form-control-sm" 
                      style="border:1px solid black !important;" 
                      required pattern="[A-Za-z ]{2,50}" 
                      title="Only letters allowed">
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Pincode</label>
                    <input type="text" name="pincode" 
                      class="form-control form-control-sm" 
                      style="border:1px solid black !important;" 
                      required pattern="^[0-9]{6}$" 
                      title="Enter valid 6 digit pincode">
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">State</label>
                    <input type="text" name="state" 
                      class="form-control form-control-sm" 
                      style="border:1px solid black !important;" 
                      required pattern="[A-Za-z ]{2,50}" 
                      title="Only letters allowed">
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Designation</label>
                    <select name="designation_id" class="form-control form-control-sm" style="border:1px solid black !important;" required>
''')

for d in designations:
    print(f"<option value='{d['id']}'>{d['designation_name']}</option>")

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
    print(f"<option value='{dep['id']}'>{dep['department_name']}</option>")

print('''
                    </select>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Role</label>
                    <select name="role" class="form-control form-control-sm" style="border:1px solid black !important;" required>
                      <option value="Manager">Manager</option>
                      <option value="Executive">Executive</option>
                    </select>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Status</label>
                    <select name="status" class="form-control form-control-sm" style="border:1px solid black !important;" required>
                      <option value="Active">Active</option>
                      <option value="Inactive">Inactive</option>
                    </select>
                  </div>
                </div>

              </div>
              <button type="submit" class="btn btn-primary">Save</button>
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
