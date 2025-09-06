#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
import header

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
dept_id = form.getvalue("id")

mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor(dictionary=True)

cur.execute("SELECT * FROM department_master WHERE id=%s", (dept_id,))
department = cur.fetchone()

if not department:
    print("<h3>Department not found</h3>")
else:
    print(f'''
<div class="main-content">
 <div class="page-content">
  <div class="container-fluid">
    <div class="row">
      <div class="col-12">
        <div class="page-title-box d-flex align-items-center justify-content-between">
          <h4 class="mb-0">Edit Department</h4>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-lg-12">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Department Form</h4>

            <form method="post" action="departmentupdate.py">
              <input type="hidden" name="id" value="{department['id']}">
              <div class="row align-items-start">

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Department Name</label>
                    <input type="text" name="department_name" value="{department['department_name']}" 
                           class="form-control form-control-sm" required>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Description</label>
                    <input type="text" name="description" value="{department['description']}" 
                           class="form-control form-control-sm" required>
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
