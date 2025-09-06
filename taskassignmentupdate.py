#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
id           = form.getvalue("id")
title        = form.getvalue("title")
description  = form.getvalue("description")
task_category= form.getvalue("task_category_id")
assign_to    = form.getvalue("assign_to")
date_assign  = form.getvalue("date_assign")
due_date     = form.getvalue("due_date")
status       = form.getvalue("status") or "Pending"
priority     = form.getvalue("priority") or "Medium"

mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor()

update_sql = """
    UPDATE task_assignment
    SET title=%s, description=%s, task_category_id=%s, assign_to=%s,
        date_assign=%s, due_date=%s, status=%s, priority=%s
    WHERE id=%s
"""
cur.execute(update_sql, (title, description, task_category, assign_to, date_assign, due_date, status, priority, id))
mydb.commit()

print("""
<script>
  alert("Task updated successfully!");
  window.location="taskassignmentlist.py";
</script>
""")
