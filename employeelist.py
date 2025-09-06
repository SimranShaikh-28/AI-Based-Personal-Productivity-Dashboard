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
          <h4 class="mb-0">Employee Table</h4>
        </div>
      </div>
    </div>
    <!-- end page title -->

    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Employee List</h4>

            <table id="datatable" class="table table-bordered dt-responsive nowrap"
                   style="border-collapse: collapse; border-spacing: 0; width: 100%;">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Name</th>
                  <th>Email</th>
                  <th>City</th>
                  <th>State</th>
                  <th>Role</th>
                  <th>Status</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
''')

# DB connection
mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor(dictionary=True)

query = """SELECT e.id, e.name, e.email, e.city, e.state, e.role, e.status,
                  d.department_name, g.designation_name
           FROM employee_master e
           LEFT JOIN department_master d ON e.department_id = d.id
           LEFT JOIN designation_master g ON e.designation_id = g.id"""
cur.execute(query)
rows = cur.fetchall()

for r in rows:
    print(f'''
      <tr>
        <td>{r['id']}</td>
        <td>{r['name']}</td>
        <td>{r['email']}</td>
        <td>{r['city']}</td>
        <td>{r['state']}</td>
        <td>{r['role']}</td>
        <td>{r['status']}</td>
        <td class="text-nowrap">
  <a href="employeeedit.py?id={r['id']}" class="btn btn-primary btn-sm me-2">Edit</a>
  <a href="employeedelete.py?id={r['id']}" class="btn btn-danger btn-sm" onclick="return confirm('Are you sure?');">Delete</a>
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
