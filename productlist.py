#!C:\Python310\python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()

import header

print('''
<div class="main-content">
    <div class="page-content">
        <div class="container-fluid">

            <!-- start page title -->
            <div class="row">
                <div class="col-12">
                    <div class="page-title-box d-flex align-items-center justify-content-between">
                        <h4 class="mb-0">Product Table</h4>
                        <div class="page-title-right"></div>
                    </div>
                </div>
            </div>
            <!-- end page title -->
            
            <div class="row">
                <div class="col-12">
                    <div class="card">
                        <div class="card-body">
                            <h4 class="card-title">Product List</h4>

                            <table id="datatable" class="table table-bordered dt-responsive nowrap" 
                                   style="border-collapse: collapse; border-spacing: 0; width: 100%;">
                                <thead>
                                    <tr>
                                        
                                        <th>ID</th>
                                        <th>Product Name</th>
                                        <th>Price</th>
                                        <th>Category</th>
                                        <th>Quantity</th>
                                        <th>Description</th>
                                        <th>Action</th>
      
                                    </tr>
                                </thead>
                                <tbody>
''')

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password='',
    database="task"
)
mycursor = mydb.cursor(dictionary=True)
mycursor.execute("SELECT * FROM products")
myresult = mycursor.fetchall()

# Loop through results
for x in myresult:
    print(f'''
        <tr>
            
            <td>{x['id']}</td>
            <td>{x['product_name']}</td>
            <td>{x['price']}</td>
            <td>{x['category']}</td>
            <td>{x['quantity']}</td>
            <td>{x['description']}</td>

            <td>
                <a href="product_update.py?id={x['id']}" class="btn btn-sm btn-primary">Edit</a>
                <a href="product_delete.py?id={x['id']}" class="btn btn-sm btn-danger" onclick="return confirm('Are you sure?');">Delete</a>
            </td>
        </tr>
    ''')

print('''
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div> <!-- end col -->
            </div> <!-- end row -->

        </div> <!-- container-fluid -->
    </div>
    <!-- End Page-content -->
''')

import footer
