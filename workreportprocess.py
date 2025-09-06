#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector, json
from datetime import date
cgitb.enable()

form = cgi.FieldStorage()

# --- DB connect ---
mydb = mysql.connector.connect(host="localhost", user="root", password="", database="drw")
cur = mydb.cursor(dictionary=True)

# --- JSON endpoint: fetch tasks for a given employee ---
if form.getvalue("get_tasks"):
    emp_id = form.getvalue("emp_id")
    cur.execute("""
        SELECT id, title 
        FROM task_assignment
        WHERE assign_to = %s
        ORDER BY title ASC
    """, (emp_id,))
    tasks = [{"id": r["id"], "title": r["title"]} for r in cur.fetchall()]
    print("Content-Type: application/json\n")
    print(json.dumps({"tasks": tasks}))
    raise SystemExit

# --- Normal form processing ---
print("Content-Type: text/html\n")

emp_id      = form.getvalue("emp_id")
task_id     = form.getvalue("task_id")
client_id   = form.getvalue("client_id")
category_id = form.getvalue("category_id")
description = form.getvalue("description")
work_date   = form.getvalue("date")
status      = form.getvalue("status") or "Pending"

# Guard: required fields
if not (emp_id and task_id and client_id and category_id and description and work_date):
    print("""
    <script>
      alert("Please fill all required fields.");
      window.location="workreport.py";
    </script>
    """)
    raise SystemExit

# Insert into work_report
insert_sql = """
    INSERT INTO work_report
    (emp_id, task_id, client_id, category_id, description, date, status)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
"""
cur.execute(insert_sql, (emp_id, task_id, client_id, category_id, description, work_date, status))
mydb.commit()

print("""
<script>
  alert("Work Report submitted successfully!");
  window.location="workreportlist.py";
</script>
""")
