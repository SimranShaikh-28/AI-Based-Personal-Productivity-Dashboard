#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector, json
from datetime import date, datetime, timedelta
cgitb.enable()

form = cgi.FieldStorage()

# DB connect
mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor()

# --- JSON endpoint used by the form to fetch leave dates (for JS blocking) ---
if form.getvalue("get_leaves"):
    emp_id = form.getvalue("emp_id")

    # Fetch approved leave ranges
    cur.execute("""
        SELECT from_date, to_date
        FROM leave_master
        WHERE emp_id=%s AND status='Approved'
    """, (emp_id,))
    ranges = cur.fetchall()

    leave_dates = []
    for r in ranges:
        start = r[0]
        end   = r[1] if r[1] else r[0]
        current = start
        while current <= end:
            leave_dates.append(str(current))
            current += timedelta(days=1)

    print("Content-Type: application/json\n")
    print(json.dumps({"leave_dates": leave_dates}))
    raise SystemExit

# --- Normal form processing with server-side leave validation ---
print("Content-Type: text/html\n")

title         = form.getvalue("title")
description   = form.getvalue("description")
task_category = form.getvalue("task_category_id")
assign_to     = form.getvalue("assign_to")
date_assign   = form.getvalue("date_assign")  # expected 'YYYY-MM-DD'
due_date      = form.getvalue("due_date")
status        = form.getvalue("status") or "Pending"
priority      = form.getvalue("priority") or "Medium"   # <-- New priority field

# Guard: required fields
if not (title and description and task_category and assign_to and date_assign and due_date):
    print("""
    <script>
      alert("Please fill all required fields.");
      window.location="taskassignment.py";
    </script>
    """)
    raise SystemExit

# Convert assign_date and today to date objects
try:
    assign_date_obj = datetime.strptime(date_assign, "%Y-%m-%d").date()
    today_obj = date.today()
except ValueError:
    print("""
    <script>
      alert("Invalid date format.");
      window.location="taskassignment.py";
    </script>
    """)
    raise SystemExit

# Check if selected employee is on Approved leave on assign date or today
cur.execute("""
    SELECT from_date, to_date
    FROM leave_master
    WHERE emp_id=%s AND status='Approved'
""", (assign_to,))
conflicts = []
for r in cur.fetchall():
    start, end = r
    if not end:
        end = start
    if start <= assign_date_obj <= end:
        conflicts.append(str(assign_date_obj))
    if start <= today_obj <= end:
        conflicts.append(str(today_obj))

if conflicts:
    detail = " and ".join(conflicts)
    print(f"""
    <script>
      alert("Cannot assign task: selected employee is on leave on {detail}.");
      window.location="taskassignment.py";
    </script>
    """)
    raise SystemExit

# No conflicts -> proceed to insert
insert_sql = """
    INSERT INTO task_assignment
    (title, description, task_category_id, assign_to, date_assign, due_date, status, priority)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
"""
cur.execute(insert_sql, (title, description, task_category, assign_to, date_assign, due_date, status, priority))
mydb.commit()

print("""
<script>
  alert("Task Assigned successfully!");
  window.location="taskassignmentlist.py";
</script>
""")
