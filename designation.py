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
          <h4 class="mb-0">Add Designation</h4>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-lg-12">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Designation Form</h4>

            <form method="post" action="designationprocess.py">
              <div class="row align-items-start">

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Designation Name</label>
                    <input type="text" name="designation_name" 
                      class="form-control form-control-sm" 
                      style="border:1px solid black !important;" 
                      required pattern="[A-Za-z ]{2,50}" 
                      title="Only letters allowed, min 2 characters">
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Description</label>
                    <input type="text" name="description" 
                      class="form-control form-control-sm" 
                      style="border:1px solid black !important;" 
                      minlength="5" maxlength="200" 
                      title="Enter at least 5 characters" required>
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
