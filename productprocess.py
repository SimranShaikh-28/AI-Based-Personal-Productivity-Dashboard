#!C:\Python310\python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")
formdata=cgi.FieldStorage()
print(formdata)

product_name=formdata.getvalue("product_name")
print(product_name)

product_price=formdata.getvalue("product_price")
print(product_price)

product_description=formdata.getvalue("product_description")
print(product_description)

product_cateogery=formdata.getvalue("product_cateogery")
print(product_cateogery)

product_quantity=formdata.getvalue("product_quantity")
print(product_quantity)

mydb=mysql.connector.connect(host="localhost",user="root",password='',database="ecom")

mycursor=mydb.cursor()

query=f"""INSERT INTO product(product_name, product_price,product_description,product_cateogery,product_quantity) VALUES ('{product_name}','{product_price}','{product_description}','{product_cateogery}','{product_quantity}')"""
print(query)
mycursor.execute(query)


mydb.commit()
print('''
<script>
      alert("product saved successfully");
      location.href="product.py";
      </script>''')

