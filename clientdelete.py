#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
client_id = form.getvalue("id")

if client_id:
    mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
    cur = mydb.cursor()
    cur.execute("DELETE FROM client_master WHERE id=%s", (client_id,))
    mydb.commit()

    print('''
    <script>
        alert("Client deleted successfully!");
        location.href="clientlist.py";
    </script>
    ''')
else:
    print("<h3>Invalid Request</h3>")
