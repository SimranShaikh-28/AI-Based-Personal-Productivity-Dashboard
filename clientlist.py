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
          <h4 class="mb-0">Client Table</h4>
        </div>
      </div>
    </div>
    <!-- end page title -->

    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Client List</h4>

            <table id="datatable" class="table table-bordered dt-responsive nowrap"
                   style="border-collapse: collapse; border-spacing: 0; width: 100%;">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Client Name</th>
                  <th>Email</th>
                  <th>Phone</th>
                  <th>Address</th>
                  <th>Company Name</th>
                  <th>Company Phone</th>
                  <th>Company Email</th>
                  <th>Status</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
''')

# DB connection
mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor(dictionary=True)
cur.execute("SELECT * FROM client_master")
rows = cur.fetchall()

for r in rows:
    print(f'''
      <tr>
        <td>{r['id']}</td>
        <td>{r['client_name']}</td>
        <td>{r['email']}</td>
        <td>{r['phone_no']}</td>
        <td>{r['address']}</td>
        <td>{r['company_name']}</td>
        <td>{r['company_phone']}</td>
        <td>{r['company_email']}</td>
        <td>{r['status']}</td>
        <td class="text-nowrap">
  <a href="clientedit.py?id={r['id']}" class="btn btn-primary btn-sm me-2">Edit</a>
  <a href="clientdelete.py?id={r['id']}" class="btn btn-danger btn-sm" onclick="return confirm('Are you sure?');">Delete</a>
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
