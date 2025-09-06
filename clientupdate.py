#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
id            = form.getvalue("id")
client_name   = form.getvalue("client_name")
email         = form.getvalue("email")
phone_no      = form.getvalue("phone_no")
address       = form.getvalue("address")
company_name  = form.getvalue("company_name")
company_phone = form.getvalue("company_phone")
company_email = form.getvalue("company_email")
status        = form.getvalue("status")

mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor()

query = """UPDATE client_master 
           SET client_name=%s, email=%s, phone_no=%s, address=%s, 
               company_name=%s, company_phone=%s, company_email=%s, status=%s
           WHERE id=%s"""
values = (client_name, email, phone_no, address, company_name, company_phone, company_email, status, id)

cur.execute(query, values)
mydb.commit()

print('''
<script>
    alert("Client updated successfully!");
    location.href="clientlist.py";
</script>
''')
