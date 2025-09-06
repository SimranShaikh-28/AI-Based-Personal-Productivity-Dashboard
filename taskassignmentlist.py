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
          <h4 class="mb-0">Task Assignment Table</h4>
        </div>
      </div>
    </div>
    <!-- end page title -->

    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Task Assignment List</h4>

            <table id="datatable" class="table table-bordered dt-responsive nowrap"
                   style="border-collapse: collapse; border-spacing: 0; width: 100%;">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Title</th>
                  <th>Description</th>
                  <th>Category</th>
                  <th>Assigned To</th>
                  <th>Date Assign</th>
                  <th>Due Date</th>
                  <th>Status</th>
                  <th>Priority</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
''')

# DB connection
mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor(dictionary=True)

query = """
    SELECT t.id, t.title, t.description, t.date_assign, t.due_date, t.status, t.priority,
           c.category_name, e.name AS employee_name
    FROM task_assignment t
    LEFT JOIN task_category_master c ON t.task_category_id = c.id
    LEFT JOIN employee_master e ON t.assign_to = e.id
"""
cur.execute(query)
rows = cur.fetchall()

for r in rows:
    print(f'''
      <tr>
        <td>{r['id']}</td>
        <td>{r['title']}</td>
        <td>{r['description']}</td>
        <td>{r['category_name'] or ''}</td>
        <td>{r['employee_name'] or ''}</td>
        <td>{r['date_assign'] or ''}</td>
        <td>{r['due_date'] or ''}</td>
        <td>{r['status']}</td>
        <td>{r['priority'] or 'Medium'}</td>
        <td class="text-nowrap">
  <a href="taskassignmentedit.py?id={r['id']}" class="btn btn-primary btn-sm me-2">Edit</a>
  <a href="taskassignmentdelete.py?id={r['id']}" class="btn btn-danger btn-sm" onclick="return confirm('Are you sure?');">Delete</a>
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
