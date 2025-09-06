#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()

id          = form.getvalue("id")
emp_id      = form.getvalue("emp_id")
task_id     = form.getvalue("task_id")
client_id   = form.getvalue("client_id")
category_id = form.getvalue("category_id")
description = form.getvalue("description")
work_date   = form.getvalue("date")
status      = form.getvalue("status") or "Pending"

# --- DB connection ---
mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor()

update_sql = """
    UPDATE work_report
    SET emp_id=%s,
        task_id=%s,
        client_id=%s,
        category_id=%s,
        description=%s,
        date=%s,
        status=%s
    WHERE id=%s
"""
cur.execute(update_sql, (emp_id, task_id, client_id, category_id, description, work_date, status, id))
mydb.commit()

print("""
<script>
  alert("Work Report updated successfully!");
  window.location="workreportlist.py";
</script>
""")
