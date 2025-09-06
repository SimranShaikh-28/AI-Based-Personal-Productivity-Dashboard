#!C:\Python310\python.exe
import cgi
import cgitb
import mysql.connector

cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
company_id    = form.getvalue("id")
person_name   = form.getvalue("person_name")
email         = form.getvalue("email")
phone_no      = form.getvalue("phone_no")
address       = form.getvalue("address")
company_name  = form.getvalue("company_name")
company_phone = form.getvalue("company_phone")
company_email = form.getvalue("company_email")
status        = form.getvalue("status")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password='',
    database="drw"
)
cur = mydb.cursor()
cur.execute("""
    UPDATE company_master
    SET person_name=%s, email=%s, phone_no=%s, address=%s, 
        company_name=%s, company_phone=%s, company_email=%s, status=%s
    WHERE id=%s
""", (person_name, email, phone_no, address, company_name, company_phone, company_email, status, company_id))
mydb.commit()

print('''
<script>
    alert("Company updated successfully!");
    window.location.href="companylist.py";
</script>
''')
