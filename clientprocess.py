#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
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
query = f"""INSERT INTO client_master(client_name,email,phone_no,address,company_name,company_phone,company_email,status)
VALUES ('{client_name}','{email}','{phone_no}','{address}','{company_name}','{company_phone}','{company_email}','{status}')"""
print(query)

cur.execute(query)
mydb.commit()

print('''
<script>
    alert("Client saved successfully!");
    location.href="clientlist.py";
</script>
''')
