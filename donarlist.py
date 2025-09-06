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
                                    <h4 class="mb-0">Brand Table</h4>

                                    <div class="page-title-right">
                                         
                                    </div>

                                </div>
                            </div>
                        </div>
                        <!-- end page title -->
                        
                        <div class="row">
                            <div class="col-12">
                                <div class="card">
                                    <div class="card-body">
        
                                        <h4 class="card-title">Brand List</h4>
                                         
        
                                        <table id="datatable" class="table table-bordered dt-responsive nowrap" style="border-collapse: collapse; border-spacing: 0; width: 100%;">
                                            <thead>
                                            <tr>
                                                <th>Sr.No</th>
                                                <th> Name</th>
                                                <th>Descriptions</th>
                                                <th>MRP</th>
                                                <th>Sale Price</th>
                                            </tr>
                                            </thead>
        
        
                                            <tbody>
                                            <tr>
                                                <td>1</td>
                                                <td>Notebook</td>
                                                <td>All Notebooks are available</td>
                                                <td>50</td>
                                                <td>50</td>
                                            </tr>
                                            <tr>
                                                <td>2</td>
                                                <td>Book</td>
                                                <td>All Books are available</td>
                                                <td>50</td>
                                                <td>50</td>
                                            </tr>
                                            
                                             
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