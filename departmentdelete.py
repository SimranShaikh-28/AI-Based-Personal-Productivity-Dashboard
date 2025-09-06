#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
dept_id = form.getvalue("id")

if dept_id:
    mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
    cur = mydb.cursor()
    cur.execute("DELETE FROM department_master WHERE id=%s", (dept_id,))
    mydb.commit()

    print('''
    <script>
        alert("Department deleted successfully!");
        location.href="departmentlist.py";
    </script>
    ''')
else:
    print("<h3>Invalid Request</h3>")
