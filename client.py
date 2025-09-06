#!C:\Python310\python.exe
import cgitb
cgitb.enable()
import header
print("Content-Type: text/html\n")

print('''
<div class="main-content">
 <div class="page-content">
  <div class="container-fluid">

    <div class="row">
      <div class="col-12">
        <div class="page-title-box d-flex align-items-center justify-content-between">
          <h4 class="mb-0">Add Client</h4>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-lg-12">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Client Form</h4>

            <form method="post" action="clientprocess.py">
              <div class="row align-items-start">

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Client Name</label>
                    <input type="text" name="client_name" class="form-control form-control-sm" 
                      style="border:1px solid black !important;" required pattern="[A-Za-z ]{2,50}" 
                      title="Only letters, minimum 2 characters">
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Email</label>
                    <input type="email" name="email" class="form-control form-control-sm" 
                      style="border:1px solid black !important;" required>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Phone No</label>
                    <input type="text" name="phone_no" class="form-control form-control-sm" 
                      style="border:1px solid black !important;" required pattern="^[0-9]{10}$" 
                      title="Enter 10 digit number">
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Address</label>
                    <input type="text" name="address" class="form-control form-control-sm" 
                      style="border:1px solid black !important;" required minlength="5">
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Company Name</label>
                    <input type="text" name="company_name" class="form-control form-control-sm" 
                      style="border:1px solid black !important;" pattern="[A-Za-z0-9& ]{2,100}" 
                      title="Only letters, numbers and & allowed">
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Company Phone</label>
                    <input type="text" name="company_phone" class="form-control form-control-sm" 
                      style="border:1px solid black !important;" pattern="^[0-9]{10}$" 
                      title="Enter 10 digit number">
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Company Email</label>
                    <input type="email" name="company_email" class="form-control form-control-sm" 
                      style="border:1px solid black !important;">
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Status</label>
                    <select name="status" class="form-control form-control-sm" 
                      style="border:1px solid black !important;">
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
