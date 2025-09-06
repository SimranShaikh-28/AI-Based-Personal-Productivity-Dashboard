#!C:\Python310\python.exe
import cgitb, mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")

import header

# Connect DB
mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor(dictionary=True)

# Total Employees
cur.execute("SELECT COUNT(*) as total_employees FROM employee_master")
total_employees = cur.fetchone()['total_employees']

# Total Tasks Assigned Today
cur.execute("SELECT COUNT(*) as total_today FROM task_assignment WHERE DATE(date_assign) = CURDATE()")
total_today = cur.fetchone()['total_today']

# Completed Tasks (Today)
cur.execute("SELECT COUNT(*) as completed_today FROM task_assignment WHERE status='Completed' AND DATE(date_assign)=CURDATE()")
completed_today = cur.fetchone()['completed_today']

# Pending Tasks
cur.execute("SELECT COUNT(*) as pending_tasks FROM task_assignment WHERE status='Pending'")
pending_tasks = cur.fetchone()['pending_tasks']

print(f'''
<div class="main-content">
 <div class="page-content">
  <div class="container-fluid">

    <!-- Dashboard Counters -->
    <div class="row">
        <div class="col-md-6 col-xl-3">
            <div class="card"><div class="card-body">
                <h4>Total Employees</h4>
                <p><span data-plugin="counterup">{total_employees}</span></p>
            </div></div>
        </div>

        <div class="col-md-6 col-xl-3">
            <div class="card"><div class="card-body">
                <h4>Total Tasks Assigned Today</h4>
                <p><span data-plugin="counterup">{total_today}</span></p>
            </div></div>
        </div>

        <div class="col-md-6 col-xl-3">
            <div class="card"><div class="card-body">
                <h4>Completed Tasks (Today)</h4>
                <p><span data-plugin="counterup">{completed_today}</span></p>
            </div></div>
        </div>

        <div class="col-md-6 col-xl-3">
            <div class="card"><div class="card-body">
                <h4>Pending Tasks</h4>
                <p><span data-plugin="counterup">{pending_tasks}</span></p>
            </div></div>
        </div>
    </div>
''')

# Employee Task Completion %
cur.execute("""
SELECT e.name,
       SUM(CASE WHEN t.status='Completed' THEN 1 ELSE 0 END) as completed,
       COUNT(t.id) as total
FROM employee_master e
LEFT JOIN task_assignment t ON e.id=t.assign_to
GROUP BY e.id
""")
rows = cur.fetchall()

print('''
    <!-- Employee Task Completion % -->
    <div class="row">
      <div class="col-lg-12">
        <div class="card"><div class="card-body">
          <h4 class="card-title">Task Completion % by Employee</h4>
          <table class="table table-bordered">
            <thead><tr><th>Employee</th><th>Completed</th><th>Total</th><th>%</th></tr></thead>
            <tbody>
''')

for r in rows:
    percent = round((r['completed']/r['total']*100),2) if r['total']>0 else 0
    print(f"<tr><td>{r['name']}</td><td>{r['completed']}</td><td>{r['total']}</td><td>{percent}%</td></tr>")

print('''
            </tbody>
          </table>
        </div></div>
      </div>
    </div>
  </div>
 </div>
</div>
''')

import footer
