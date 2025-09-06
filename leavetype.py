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
          <h4 class="mb-0">Add Leave Type</h4>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-lg-12">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Leave Type Form</h4>

            <form method="post" action="leavetypeprocess.py">
              <div class="row align-items-start">

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Leave Type</label>
                    <input type="text" name="leave_type" 
                           class="form-control form-control-sm" 
                           style="border:1px solid black !important;"
                           placeholder="e.g., Sick Leave"
                           pattern="^[A-Za-z ]{3,30}$" 
                           title="Only letters and spaces, 3-30 characters" required>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Description</label>
                    <input type="text" name="description" 
                           class="form-control form-control-sm" 
                           style="border:1px solid black !important;"
                           placeholder="Brief description"
                           pattern="^[A-Za-z0-9 ,.()-]{5,100}$"
                           title="Letters, numbers, and basic punctuation allowed (5-100 chars)" required>
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
