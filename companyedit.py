#!C:\Python310\python.exe
import cgi
import cgitb
import mysql.connector
import header

cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
company_id = form.getvalue("id")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password='',
    database="drw"
)
cur = mydb.cursor(dictionary=True)
cur.execute("SELECT * FROM company_master WHERE id=%s", (company_id,))
company = cur.fetchone()

print(f'''
<div class="main-content">
 <div class="page-content">
  <div class="container-fluid">

    <div class="row">
      <div class="col-12">
        <div class="page-title-box d-flex align-items-center justify-content-between">
          <h4 class="mb-0">Edit Company</h4>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-lg-12">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Company Form</h4>

            <form method="post" action="companyupdate.py">
              <input type="hidden" name="id" value="{company['id']}">
              <div class="row align-items-start">

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Contact Person Name</label>
                    <input type="text" name="person_name" class="form-control form-control-sm"
                      value="{company['person_name']}" required>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Email</label>
                    <input type="email" name="email" class="form-control form-control-sm"
                      value="{company['email']}" required>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Phone No</label>
                    <input type="text" name="phone_no" class="form-control form-control-sm"
                      value="{company['phone_no']}" required>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Address</label>
                    <input type="text" name="address" class="form-control form-control-sm"
                      value="{company['address']}" required>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Company Name</label>
                    <input type="text" name="company_name" class="form-control form-control-sm"
                      value="{company['company_name']}" required>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Company Phone No</label>
                    <input type="text" name="company_phone" class="form-control form-control-sm"
                      value="{company['company_phone']}">
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Company Email</label>
                    <input type="email" name="company_email" class="form-control form-control-sm"
                      value="{company['company_email']}">
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Status</label>
                    <select name="status" class="form-control form-control-sm">
                      <option value="Active" {"selected" if company['status']=="Active" else ""}>Active</option>
                      <option value="Inactive" {"selected" if company['status']=="Inactive" else ""}>Inactive</option>
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
