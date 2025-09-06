#!C:\Python310\python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")

myhtml ='''
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Product Form</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body>

<div class="container mt-3">
  <h2>product form</h2>
  <form action="productprocess.py" method="post">
    <div class="mb-3 mt-3">
      <label for="product">Product Name:</label>
      <input type="product" class="form-control" id="" placeholder="" name="product_name">
    </div>
    <div class="mb-3 mt-3">
      <label for="price">Price:</label>
      <input type="price" class="form-control" id="" placeholder="" name="product_price">
    </div>
    <div class="mb-3 mt-3">
      <label for="Description">Description:</label>
      <input type="Description" class="form-control" id="" placeholder="" name="product_description">
    </div>
    <div class="mb-3 mt-3">
      <label for="Cateogery">Cateogery:</label>
      <input type="Cateogery" class="form-control" id="" placeholder="" name="product_cateogery">
    </div>
    <div class="mb-3 mt-3">
      <label for="Quantity">Quantity:</label>
      <input type="Quantity" class="form-control" id="" placeholder="" name="Product_quantity">
    </div>
    <div class="form-check mb-3">
      <label class="form-check-label">
        <input class="form-check-input" type="checkbox" name="remember"> Remember me
      </label>
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
</div>

</body>
</html>
'''
print(myhtml)