#!C:\Python310\python.exe
import cgi
import cgitb
import os
import mysql.connector

# Enable detailed error messages for debugging
cgitb.enable()

# Print HTTP header (mandatory for CGI output)
print("Content-Type: text/html\n")
myhtml='''
<!DOCTYPE html>
<html>
<head>
    <title>Upload Student Photo</title>
</head>
<body>
    <h2>Upload Student Photo</h2>
    <form action="folderimageupload.py" method="post" enctype="multipart/form-data">
        
        <label>Student Name:</label>
        <input type="text" name="student_name" required><br><br>

        <label>Upload Photo:</label>
        <input type="file" name="student_photo" accept="image/*" required><br><br>

        <input type="submit" value="Upload">
    </form>
</body>
</html>
'''
print(myhtml)