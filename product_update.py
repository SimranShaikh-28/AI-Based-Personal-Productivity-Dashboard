#!C:\Python310\python.exe
import cgi
import mysql.connector
import cgitb
cgitb.enable()

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
product_id = form.getvalue("id")
product_name = form.getvalue("product_name")
price = form.getvalue("price")
category = form.getvalue("category")
quantity = form.getvalue("quantity")
description = form.getvalue("description")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password='',
    database="task"
)
mycursor = mydb.cursor(dictionary=True)

# If form is submitted, update product
if product_id and product_name and price and category and quantity and description:
    query = """UPDATE products 
               SET product_name=%s, price=%s, category=%s, quantity=%s, description=%s 
               WHERE id=%s"""
    mycursor.execute(query, (product_name, price, category, quantity, description, product_id))
    mydb.commit()
    print('<meta http-equiv="refresh" content="0; URL=productlist.py">')

else:
    # Fetch product details to edit
    query = "SELECT * FROM products WHERE id=%s"
    mycursor.execute(query, (product_id,))
    product = mycursor.fetchone()

    # Pre-fill the form with existing data
    print(f'''
    <!-- Start Form Sizing -->
    <div class="row">
        <div class="col-lg-12">
            <div class="card">
                <div class="card-body">
                    <h4 class="card-title">Edit Product</h4>
                    
                    <form action="productedit.py" method="post">
                        <input type="hidden" name="id" value="{product['id']}">
                        
                        <div class="row align-items-start">
                            <div class="col-lg-6">
                                <div class="mb-3">
                                    <label class="form-label" for="product_name">Product Name</label>
                                    <input class="form-control form-control-sm" 
                                           type="text" 
                                           id="product_name" 
                                           name="product_name" 
                                           value="{product['product_name']}" 
                                           placeholder="Enter product name" 
                                           style="border:1px solid black !important;" 
                                           required>
                                </div>
                            </div>

                            <div class="col-lg-6">
                                <div class="mb-3">
                                    <label class="form-label" for="price">Price</label>
                                    <input class="form-control form-control-sm" 
                                           type="number" 
                                           id="price" 
                                           name="price" 
                                           value="{product['price']}" 
                                           placeholder="Enter price" 
                                           style="border:1px solid black !important;" 
                                           required>
                                </div>
                            </div>
                        </div>

                        <div class="row align-items-start">
                            <div class="col-lg-6">
                                <div class="mb-3">
                                    <label class="form-label" for="category">Category</label>
                                    <input class="form-control form-control-sm" 
                                           type="text" 
                                           id="category" 
                                           name="category" 
                                           value="{product['category']}" 
                                           placeholder="Enter category" 
                                           style="border:1px solid black !important;" 
                                           required>
                                </div>
                            </div>

                            <div class="col-lg-6">
                                <div class="mb-3">
                                    <label class="form-label" for="quantity">Quantity</label>
                                    <input class="form-control form-control-sm" 
                                           type="number" 
                                           id="quantity" 
                                           name="quantity" 
                                           value="{product['quantity']}" 
                                           placeholder="Enter quantity" 
                                           style="border:1px solid black !important;" 
                                           required>
                                </div>
                            </div>
                        </div>

                        <div class="row align-items-start">
                            <div class="col-lg-12">
                                <div class="mb-3">
                                    <label class="form-label" for="description">Description</label>
                                    <textarea class="form-control form-control-sm" 
                                              id="description" 
                                              name="description" 
                                              rows="3" 
                                              placeholder="Write product details..." 
                                              style="border:1px solid black !important;">{product['description']}</textarea>
                                </div>
                            </div>
                        </div>

                        <div class="row mt-3">
                            <div class="col-lg-12">
                                <button type="submit" class="btn btn-primary">Update Product</button>
                            </div>
                        </div>
                    </form>

                </div>
            </div>
        </div>
    </div>
    <!-- End Form Sizing -->
    ''')
