#!C:\Python310\python.exe
import cgi
import cgitb
cgitb.enable()
#print("Content-Type: text/html\n") 
import header
print('''
<div class="main-content">

                <div class="page-content">
                    <div class="container-fluid">

                        <!-- start page title -->
                        <div class="row">
                            <div class="col-12">
                                <div class="page-title-box d-flex align-items-center justify-content-between">
                                    <h4 class="mb-0">Add New Product<h4>

                                </div>
                            </div>
                        </div>
                        <!-- end page title -->

                        <!-- Start Form Sizing -->
                        <div class="row">
                            <div class="col-lg-12">
                                <div class="card">
                                    <div class="card-body">
                                        <h4 class="card-title">Product Form</h4>
                                        
                                        <form>
                                            <div class="row align-items-start">
                                                <div class="col-lg-6">
                                                    <div class="mb-3">
                                                        <label class="form-label" for="form-sm-input">Product name</label>
                                                        <input class="form-control form-control-sm" type="text" id="form-sm-input" style="border:1px solid black !important;">
                                                    </div>
                                                </div>
                                                
                                                <div class="col-lg-6">
                                                    <div class="">
                                                        <label class="form-label" for="form-lg-input">Product Price</label>
                                                        <input class="form-control form-control-sm" type="text" id="form-lg-input" style="border:1px solid black !important;">
                                                    </div>
                                                </div>
                                                <div class="col-lg-6">
                                                    <div class="">
                                                        <label class="form-label" for="form-lg-input">Product Description</label>
                                                        <input class="form-control form-control-sm" type="text" id="form-lg-input" style="border:1px solid black !important;">
                                                    </div>
                                                </div>
                                                <div class="col-lg-6">
                                                    <div class="">
                                                        <label class="form-label" for="form-lg-input">Product Quantity</label>
                                                        <input class="form-control form-control-sm" type="text" id="form-lg-input" style="border:1px solid black !important;">
                                                    </div>
                                                </div>
                                               
                                            </div>
                                        </form>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- End Form Sizing -->
                        
                    </div> <!-- container-fluid -->
                </div>
                <!-- End Page-content -->
''')
import footer

        