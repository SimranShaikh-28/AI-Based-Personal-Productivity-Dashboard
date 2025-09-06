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
                                    <h4 class="mb-0">Add New Brand<h4>

                                     

                                </div>
                            </div>
                        </div>
                        <!-- end page title -->

                         

                     

                        <!-- Start Form Sizing -->
                        <div class="row">
                            <div class="col-lg-12">
                                <div class="card">
                                    <div class="card-body">
                                        <h4 class="card-title">Brand Form</h4>
                                        
                                        <form action=post >
                                            <div class="row align-items-start">
                                                <div class="col-lg-6">
                                                    <div class="mb-3">
                                                        <label class="form-label" for="form-sm-input" name='brand name'>Brand name</label>
                                                        <input class="form-control form-control-sm" type="text" id="form-sm-input" style="border:1px solid black !important;">
                                                    </div>
                                                </div>
      
      <div class="row align-items-start">
                                                <div class="col-lg-6">
                                                    <div class="mb-3">
                                                        <label class="form-label" for="form-sm-input" name='brand description'>Brand description</label>
                                                        <input class="form-control form-control-sm" type="text" id="form-sm-input" style="border:1px solid black !important;">
                                                    </div>
                                                </div>
                                                
                        </div>
                        <!-- End Form Sizing -->

                        <button type="button" class="btn btn-primary" style=width:10%;height:40px;>Submit</button>
           
 
                          

                       
                        
                    </div> <!-- container-fluid -->
                </div>
                <!-- End Page-content -->
''')
import footer

        