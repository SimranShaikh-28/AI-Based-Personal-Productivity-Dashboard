#!C:\Python310\python.exe
import cgi
import cgitb
import mysql.connector

cgitb.enable()
print("Content-Type: text/html\n")

formdata = cgi.FieldStorage()

# Collect form values
person_name   = formdata.getvalue("person_name")
email         = formdata.getvalue("email")
phone_no      = formdata.getvalue("phone_no")
address       = formdata.getvalue("address")
company_name  = formdata.getvalue("company_name")
company_phone = formdata.getvalue("company_phone")
company_email = formdata.getvalue("company_email")
status        = formdata.getvalue("status")

# Connect to database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password='',
    database="drw"   # ⚠️ Use the same DB you use for product
)
mycursor = mydb.cursor()

# Insert query
query = f"""INSERT INTO company_master
(person_name, email, phone_no, address, company_name, company_phone, company_email, status)
VALUES ('{person_name}','{email}','{phone_no}','{address}','{company_name}','{company_phone}','{company_email}','{status}')"""

print(query)   # (for debugging, you can remove later)

mycursor.execute(query)
mydb.commit()

# Success message
print('''
<script>
    alert("Company saved successfully!");
    location.href="companylist.py";
</script>
''')
