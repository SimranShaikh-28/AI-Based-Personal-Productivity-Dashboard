#!C:\Python310\python.exe
import cgitb, mysql.connector
cgitb.enable()
import header
print("Content-Type: text/html\n")

print('''
<div class="main-content">
 <div class="page-content">
  <div class="container-fluid">

    <!-- start page title -->
    <div class="row">
      <div class="col-12">
        <div class="page-title-box d-flex align-items-center justify-content-between">
          <h4 class="mb-0">Designation Table</h4>
        </div>
      </div>
    </div>
    <!-- end page title -->

    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Designation List</h4>

            <table id="datatable" class="table table-bordered dt-responsive nowrap"
                   style="border-collapse: collapse; border-spacing: 0; width: 100%;">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Designation Name</th>
                  <th>Description</th>
                  <th>Action</th>
              </thead>
              <tbody>
''')

# DB connection
mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor(dictionary=True)
cur.execute("SELECT * FROM designation_master")
rows = cur.fetchall()

for r in rows:
    print(f'''
      <tr>
        <td>{r['id']}</td>
        <td>{r['designation_name']}</td>
        <td>{r['description']}</td>
        <td class="text-nowrap">
  <a href="designationedit.py?id={r['id']}" class="btn btn-primary btn-sm me-2">Edit</a>
  <a href="designationdelete.py?id={r['id']}" class="btn btn-danger btn-sm" onclick="return confirm('Are you sure?');">Delete</a>
</td>
      </tr>
    ''')

print('''
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

  </div>
 </div>
</div>
''')

import footer
