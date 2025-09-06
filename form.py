#!C:\Python310\python.exe
import cgi
import cgitb
import os
import mysql.connector

# Enable detailed error messages for debugging
cgitb.enable()

# Print HTTP header (mandatory for CGI output)
print("Content-Type: text/html\n")

# Get form data
form = cgi.FieldStorage()
student_name = form.getvalue("student_name")   # Student name
photo_file=form["student_photo"]            # Uploaded photo file

# Extract file extension (e.g. .jpg, .png)
file_name, file_ext = os.path.splitext(photo_file.filename)
upload_file_name = "wolfox" + file_ext         # Rename uploaded file

# ✅ Connect to MySQL Database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="pythonbasic"
)
mycursor = mydb.cursor()

# ✅ Insert student record (name + photo filename)
insert_query = """INSERT INTO student_photo (pname, photo) VALUES (%s, %s)"""
mycursor.execute(insert_query, (student_name, upload_file_name))
mydb.commit()

# ✅ Get auto-generated student ID
student_id = mycursor.lastrowid

# ✅ Create directory for this student (based on ID)
upload_dir = f"student/{student_id}"
os.makedirs(upload_dir, exist_ok=True)

# ✅ Save uploaded file into that directory
file_path = os.path.join(upload_dir, upload_file_name)
with open(file_path, 'wb') as f:
    f.write(photo_file.file.read())

# ✅ Show success message and redirect back
print(f"""
    <script>
        alert("Student Photo Added Successfully!");
        location.href="upload_form.html";
    </script>
""")