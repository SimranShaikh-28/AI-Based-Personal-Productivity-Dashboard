#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector, os
cgitb.enable()

print("Content-Type: text/html\n")

form = cgi.FieldStorage()

emp_id      = form.getvalue("emp_id")
task_id     = form.getvalue("task_id")
client_id   = form.getvalue("client_id")
description = form.getvalue("description")
report_date = form.getvalue("report_date")
latitude    = form.getvalue("latitude")
longitude   = form.getvalue("longitude")
status      = form.getvalue("status")

filename = None
if "work_photo" in form:
    fileitem = form["work_photo"]
    if fileitem is not None and fileitem.filename:
        upload_dir = "uploads"
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        filename = os.path.basename(fileitem.filename)
        with open(os.path.join(upload_dir, filename), "wb") as f:
            f.write(fileitem.file.read())

try:
    db = mysql.connector.connect(host="localhost", user="root", password="", database="drw")
    cur = db.cursor()

    # derive category from task
    cur.execute("SELECT task_category_id FROM task_assignment WHERE id=%s", (task_id,))
    row = cur.fetchone()
    category_id = row[0] if row else None
    if not category_id:
        raise Exception("Task has no category")

    cur.execute("""
        INSERT INTO work_report
        (emp_id, task_id, client_id, category_id, description, work_photo, report_date, latitude, longitude, status)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (emp_id, task_id, client_id, category_id, description, filename, report_date, latitude, longitude, status))
    db.commit()

    print('''
    <script>
      alert("Work Report saved successfully");
      location.href="workreport_list.py";
    </script>
    ''')

except Exception as e:
    print(f"<h3 style='color:red'>Error: {e}</h3>")
