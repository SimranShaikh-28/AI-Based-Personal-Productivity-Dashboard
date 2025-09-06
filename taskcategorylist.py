#!C:\Python310\python.exe
import cgitb, mysql.connector
cgitb.enable()
import header
print("Content-Type: text/html\n")

print('''
<div class="main-content">
 <div class="page-content">
  <div class="container-fluid">
    <h4>Task Category List</h4>
    <table class="table table-bordered">
      <thead>
        <tr>
          <th>ID</th>
          <th>Category Name</th>
          <th>Description</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
''')

mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor(dictionary=True)
cur.execute("SELECT * FROM task_category_master")
rows = cur.fetchall()

for r in rows:
    print(f'''
      <tr>
        <td>{r['id']}</td>
        <td>{r['category_name']}</td>
        <td>{r['description']}</td>
        <td class="text-nowrap">
  <a href="taskcategoryedit.py?id={r['id']}" class="btn btn-primary btn-sm me-2">Edit</a>
  <a href="taskcategorydelete.py?id={r['id']}" class="btn btn-danger btn-sm" onclick="return confirm('Are you sure?');">Delete</a>
</td>
      </tr>
    ''')

print('''
      </tbody>
    </table>
  </div>
 </div>
</div>
''')

import footer

# <td>
#           <a href="taskcategoryedit.py?id={r['id']}" class="btn btn-sm btn-primary">Edit</a>
#           <a href="taskcategorydelete.py?id={r['id']}" class="btn btn-sm btn-danger" onclick="return confirm('Are you sure?');">Delete</a>
#         </td>
