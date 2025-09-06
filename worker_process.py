#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector, http.cookies
cgitb.enable()

form = cgi.FieldStorage()
username = form.getvalue("username") or ""
# we keep password field to preserve your layout, but we don't validate it (not in schema)
# password = form.getvalue("userpassword")

db = mysql.connector.connect(host="localhost", user="root", password="", database="drw")
cur = db.cursor(dictionary=True)

cur.execute("SELECT id, name FROM employee_master WHERE name=%s AND status='Active'", (username,))
user = cur.fetchone()

if user:
    # set cookie so pages work even without ?empid= in the URL
    cookie = http.cookies.SimpleCookie()
    cookie["empid"] = str(user["id"])
    cookie["empid"]["path"] = "/"
    # optional: cookie["empid"]["max-age"] = 86400  # 1 day

    print(cookie.output())
    print("Content-Type: text/html\n")
    # redirect to tasks without showing ID in URL
    print("<script>alert('Welcome {}');location.href='tasks.py';</script>".format(user["name"]))
else:
    print("Content-Type: text/html\n")
    print("<script>alert('Worker not found');location.href='worker_login.py';</script>")
