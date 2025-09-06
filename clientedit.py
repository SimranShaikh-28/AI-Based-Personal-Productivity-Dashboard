#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
import header

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
client_id = form.getvalue("id")

mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor(dictionary=True)

# Fetch client details
cur.execute("SELECT * FROM client_master WHERE id=%s", (client_id,))
client = cur.fetchone()

if not client:
    print("<h3>Client not found</h3>")
else:
    print(f'''
<div class="main-content">
 <div class="page-content">
  <div class="container-fluid">
    <div class="row">
      <div class="col-12">
        <div class="page-title-box d-flex align-items-center justify-content-between">
          <h4 class="mb-0">Edit Client</h4>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-lg-12">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Client Form</h4>

            <form method="post" action="clientupdate.py">
              <input type="hidden" name="id" value="{client['id']}">
              <div class="row align-items-start">

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Client Name</label>
                    <input type="text" name="client_name" value="{client['client_name']}" class="form-control form-control-sm" required>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Email</label>
                    <input type="email" name="email" value="{client['email']}" class="form-control form-control-sm" required>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Phone No</label>
                    <input type="text" name="phone_no" value="{client['phone_no']}" class="form-control form-control-sm" required>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Address</label>
                    <input type="text" name="address" value="{client['address']}" class="form-control form-control-sm" required>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Company Name</label>
                    <input type="text" name="company_name" value="{client['company_name']}" class="form-control form-control-sm">
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Company Phone</label>
                    <input type="text" name="company_phone" value="{client['company_phone']}" class="form-control form-control-sm">
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Company Email</label>
                    <input type="email" name="company_email" value="{client['company_email']}" class="form-control form-control-sm">
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Status</label>
                    <select name="status" class="form-control form-control-sm">
                      <option value="Active" {"selected" if client['status']=="Active" else ""}>Active</option>
                      <option value="Inactive" {"selected" if client['status']=="Inactive" else ""}>Inactive</option>
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
