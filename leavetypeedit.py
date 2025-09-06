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

# Fetch existing record
cur.execute("SELECT * FROM leave_type_master WHERE id=%s", (id,))
row = cur.fetchone()

print(f'''
<div class="main-content">
 <div class="page-content">
  <div class="container-fluid">

    <div class="row">
      <div class="col-12">
        <div class="page-title-box d-flex align-items-center justify-content-between">
          <h4 class="mb-0">Edit Leave Type</h4>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-lg-12">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Update Leave Type</h4>

            <form method="post" action="leavetypeupdate.py">
              <input type="hidden" name="id" value="{row['id']}">

              <div class="row align-items-start">

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Leave Type</label>
                    <input type="text" name="leave_type" value="{row['leave_type']}"
                           class="form-control form-control-sm"
                           style="border:1px solid black !important;"
                           pattern="^[A-Za-z ]{{3,30}}$"
                           title="Only letters and spaces, 3-30 characters" required>
                  </div>
                </div>

                <div class="col-lg-6">
                  <div class="mb-3">
                    <label class="form-label">Description</label>
                    <input type="text" name="description" value="{row['description']}"
                           class="form-control form-control-sm"
                           style="border:1px solid black !important;"
                           pattern="^[A-Za-z0-9 ,.()-]{{5,100}}$"
                           title="Letters, numbers, and basic punctuation allowed (5-100 chars)" required>
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
