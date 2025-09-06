#!C:\Python310\python.exe
import cgi
import cgitb
import mysql.connector

cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
company_id = form.getvalue("id")

if company_id:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password='',
        database="drw"
    )
    cur = mydb.cursor()
    cur.execute("DELETE FROM company_master WHERE id=%s", (company_id,))
    mydb.commit()

print('''
<script>
    alert("Company deleted successfully!");
    window.location.href="companylist.py";
</script>
''')
