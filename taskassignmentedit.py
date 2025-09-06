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

# Fetch task record
cur.execute("SELECT * FROM task_assignment WHERE id=%s", (id,))
task = cur.fetchone()

# Fetch dropdowns
cur.execute("SELECT id, category_name FROM task_category_master")
categories = cur.fetchall()

cur.execute("SELECT id, name FROM employee_master WHERE status='Active'")
employees = cur.fetchall()

print(f"""
<div class="main-content">
 <div class="page-content">
  <div class="container-fluid">
    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Edit Task Assignment</h4>
            <form method="post" action="taskassignmentupdate.py">
              <input type="hidden" name="id" value="{task['id']}">

              <div class="row">
                <div class="col-lg-6 mb-3">
                  <label>Task Title</label>
                  <input type="text" name="title" value="{task['title']}" class="form-control" required>
                </div>

                <div class="col-lg-6 mb-3">
                  <label>Description</label>
                  <textarea name="description" class="form-control" required>{task['description']}</textarea>
                </div>

                <div class="col-lg-6 mb-3">
                  <label>Category</label>
                  <select name="task_category_id" class="form-control" required>
""")

for c in categories:
    selected = "selected" if c["id"] == task["task_category_id"] else ""
    print(f"<option value='{c['id']}' {selected}>{c['category_name']}</option>")

print("""</select></div>""")

print("""<div class="col-lg-6 mb-3"><label>Assign To</label>
<select name="assign_to" class="form-control" required>""")
for e in employees:
    selected = "selected" if e["id"] == task["assign_to"] else ""
    print(f"<option value='{e['id']}' {selected}>{e['name']}</option>")
print("</select></div>")

print(f"""
<div class="col-lg-6 mb-3">
 <label>Date Assign</label>
 <input type="date" name="date_assign" value="{task['date_assign']}" class="form-control" required>
</div>

<div class="col-lg-6 mb-3">
 <label>Due Date</label>
 <input type="date" name="due_date" value="{task['due_date']}" class="form-control" required>
</div>

<div class="col-lg-6 mb-3">
 <label>Status</label>
 <select name="status" class="form-control">
   <option value="Pending" {"selected" if task['status']=="Pending" else ""}>Pending</option>
   <option value="In Progress" {"selected" if task['status']=="In Progress" else ""}>In Progress</option>
   <option value="Completed" {"selected" if task['status']=="Completed" else ""}>Completed</option>
 </select>
</div>

<div class="col-lg-6 mb-3">
 <label>Priority</label>
 <select name="priority" class="form-control">
   <option value="Low" {"selected" if task['priority']=="Low" else ""}>Low</option>
   <option value="Medium" {"selected" if task['priority']=="Medium" else ""}>Medium</option>
   <option value="High" {"selected" if task['priority']=="High" else ""}>High</option>
 </select>
</div>

<div class="col-12">
 <button type="submit" class="btn btn-primary">Update</button>
</div>
</div>
</form>
</div></div></div></div></div></div>
""")

import footer
