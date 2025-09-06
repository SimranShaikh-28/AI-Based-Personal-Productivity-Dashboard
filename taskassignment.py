#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")

import header

print("""
<div class="main-content">
 <div class="page-content">
  <div class="container-fluid">
    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Assign Task</h4>
            <form method="post" action="taskassignmentprocess.py">
              <div class="row">
""")

# DB connect
mydb = mysql.connector.connect(host="localhost", user="root", password="", database="drw")
cur = mydb.cursor(dictionary=True)

# Task title
print("""
<div class="col-lg-6 mb-3">
 <label>Task Title</label>
 <input type="text" name="title" class="form-control" required>
</div>
""")

# Task description
print("""
<div class="col-lg-6 mb-3">
 <label>Description</label>
 <textarea name="description" class="form-control" required></textarea>
</div>
""")

# Category dropdown
print("""<div class="col-lg-6 mb-3"><label>Category</label>
<select name="task_category_id" class="form-control" required>""")
cur.execute("SELECT id, category_name FROM task_category_master")
for row in cur.fetchall():
    print(f"<option value='{row['id']}'>{row['category_name']}</option>")
print("</select></div>")

# Employee dropdown
print("""<div class="col-lg-6 mb-3"><label>Assign To</label>
<select name="assign_to" id="assign_to" class="form-control" required>""")
cur.execute("SELECT id, name FROM employee_master WHERE status='Active'")
for row in cur.fetchall():
    print(f"<option value='{row['id']}'>{row['name']}</option>")
print("</select></div>")

# Date Assign
print("""
<div class="col-lg-6 mb-3">
 <label>Date Assign</label>
 <input type="date" id="date_assign" name="date_assign" class="form-control" required>
 <small id="assign_help" class="text-danger"></small>
</div>
""")

# Due Date
print("""
<div class="col-lg-6 mb-3">
 <label>Due Date</label>
 <input type="date" id="due_date" name="due_date" class="form-control" required>
 <small id="due_help" class="text-danger"></small>
</div>
""")

# Status
print("""
<div class="col-lg-6 mb-3">
 <label>Status</label>
 <select name="status" class="form-control">
   <option value="Pending">Pending</option>
   <option value="In Progress">In Progress</option>
   <option value="Completed">Completed</option>
 </select>
</div>
""")

# Priority
print("""
<div class="col-lg-6 mb-3">
 <label>Priority</label>
 <select name="priority" class="form-control">
   <option value="Low">Low</option>
   <option value="Medium" selected>Medium</option>
   <option value="High">High</option>
 </select>
</div>
""")

print("""
<div class="col-12">
 <button type="submit" class="btn btn-primary">Submit</button>
</div>
</div>
</form>
</div></div></div></div></div></div>
""")

# JavaScript for disabling leave dates
print("""
<script>
document.getElementById('assign_to').addEventListener('change', function() {
    let empId = this.value;
    if (!empId) return;

    fetch('taskassignmentprocess.py?get_leaves=1&emp_id=' + empId)
      .then(response => response.json())
      .then(data => {
          let assignInput = document.getElementById('date_assign');
          let dueInput = document.getElementById('due_date');
          let assignHelp = document.getElementById('assign_help');
          let dueHelp = document.getElementById('due_help');

          let disabledDates = data.leave_dates; // ["2025-08-24","2025-08-25"]

          // Show blocked dates info
          if (disabledDates.length > 0) {
              assignHelp.textContent = "Blocked dates: " + disabledDates.join(", ");
              dueHelp.textContent = "Blocked dates: " + disabledDates.join(", ");
          } else {
              assignHelp.textContent = "";
              dueHelp.textContent = "";
          }

          function blockLeaveDates(input) {
              input.addEventListener('input', function() {
                  if (disabledDates.includes(this.value)) {
                      alert("This date is on leave for selected employee!");
                      this.value = '';
                  }
              });
          }

          blockLeaveDates(assignInput);
          blockLeaveDates(dueInput);
      });
});
</script>
""")

import footer
