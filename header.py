#!C:\Python310\python.exe
import cgi, cgitb, mysql.connector, os, http.cookies
cgitb.enable()
print("Content-Type: text/html\n")

# --- get manager id from cookie or URL ---
form = cgi.FieldStorage()
adminid = form.getvalue("adminid")

if not adminid:
    cookies = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE", ""))
    adminid = cookies["adminid"].value if "adminid" in cookies else None

manager_name = "Manager"
if adminid:
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="", database="drw")
        cur = db.cursor(dictionary=True)
        cur.execute("SELECT name FROM employee_master WHERE id=%s AND role='Manager'", (adminid,))
        row = cur.fetchone()
        if row:
            manager_name = row["name"]
        cur.close()
        db.close()
    except Exception as e:
        manager_name = "Manager"

        import os, http.cookies

def get_admin_display_name():
    cookies = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE", ""))
    if "adminname" in cookies and cookies["adminname"].value.strip():
        return cookies["adminname"].value.strip()
    return "Marcus"  # fallback if no cookie

print(f'''
<!doctype html>
<html lang="en">

 <head>
        
        <meta charset="utf-8" />
        <title>Basic Elements | Minible - Admin & Dashboard Template</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta content="Premium Multipurpose Admin & Dashboard Template" name="description" />
        <meta content="Themesbrand" name="author" />
        <!-- App favicon -->
        <link rel="shortcut icon" href="assets/images/favicon.ico">

        <!-- Bootstrap Css -->
        <link href="assets/css/bootstrap.min.css" id="bootstrap-style" rel="stylesheet" type="text/css" />
        <!-- Icons Css -->
        <link href="assets/css/icons.min.css" rel="stylesheet" type="text/css" />
        <!-- App Css-->
        <link href="assets/css/app.min.css" id="app-style" rel="stylesheet" type="text/css" />
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css" integrity="sha512-5A8nwdMOWrSz20fDsjczgUidUBR8liPYU+WymTZP1lmY9G6Oc7HlZv156XqnsgNUzTyMefFTcsFH/tnJE/+xBg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    </head>

    
    <body>

    <!-- <body data-layout="horizontal" data-topbar="colored"> -->

        <!-- Begin page -->
        <div id="layout-wrapper">

            
            <header id="page-topbar">
                <div class="navbar-header" style="background-color: #6597c2;">

                    <div class="d-flex">
                        <!-- LOGO -->
                        <div class="navbar-brand-box">
                     

                          
                        </div>

                        <button type="button" class="btn btn-sm px-3 font-size-16 header-item waves-effect vertical-menu-btn">
                            <i class="fa fa-fw fa-bars"></i>
                        </button>

                       
                    </div>

                    <div class="d-flex">

                        <div class="dropdown d-inline-block d-lg-none ms-2">
                            <button type="button" class="btn header-item noti-icon waves-effect" id="page-header-search-dropdown"
                                data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <i class="uil-search"></i>
                            </button>
                            <div class="dropdown-menu dropdown-menu-lg dropdown-menu-end p-0"
                                aria-labelledby="page-header-search-dropdown">
                    
                                <form class="p-3">
                                    <div class="m-0">
                                        <div class="input-group">
                                            <input type="text" class="form-control" placeholder="Search ..." aria-label="Recipient's username">
                                            <div class="input-group-append">
                                                <button class="btn btn-primary" type="submit"><i class="mdi mdi-magnify"></i></button>
                                            </div>
                                        </div>
                                    </div>
                                </form>
                            </div>
                        </div>
 
 

                        

                        <div class="dropdown d-inline-block">
       <button type="button" class="btn header-item waves-effect" id="page-header-user-dropdown"
           data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
               
           <span class="d-none d-xl-inline-block ms-1 fw-medium font-size-15">{manager_name}</span>
           <i class="uil-angle-down d-none d-xl-inline-block font-size-15"></i>
       </button>
       <div class="dropdown-menu dropdown-menu-end">
           <a class="dropdown-item" href="#"><i class="uil uil-sign-out-alt font-size-18 align-middle me-1 text-muted"></i> 
           <span class="align-middle">Sign out</span></a>
       </div>
   </div>

                        <div class="dropdown d-inline-block">
                            <button type="button" class="btn header-item noti-icon right-bar-toggle waves-effect">
                                <i class="uil-cog"></i>
                            </button>
                        </div>
            
                    </div>
                </div>
            </header>
            <!-- ========== Left Sidebar Start ========== -->
            <div class="vertical-menu">
            <div class="navbar-brand-box">
                    <a href="dashboard.py" class="logo logo-dark">
                         <span class="logo-sm">
                            <img src="assets\images\image.png"  style="width:45px;">
                        </span>
                        <span class="logo-lg">
                            <img src="assets\images\image.png" style="width:55%;" >
                        </span>
                    </a>

                    <a href="dashboard.py" class="logo logo-light">
                        <span class="logo-sm">
                            <img src="assets\images\image.png" style="width:55%;" >
                        </span>
                        <span class="logo-lg">
                            <img src="assets\images\image.png" style="width:55%;" >
                        </span>
                    </a>
                </div>


                <button type="button" class="btn btn-sm px-3 font-size-16 header-item waves-effect vertical-menu-btn">
                    <i class="fa fa-fw fa-bars"></i>
                </button>

                <div data-simplebar class="sidebar-menu-scroll" style="background-color:#6597c2;">

                    <!--- Sidemenu -->
                    <div id="sidebar-menu" style="margin-top:30px;">
                        <!-- Left Menu Start -->
                        <ul class="metismenu list-unstyled" id="side-menu">
                            <li class="menu-title">Welcome To Admin Dashboard</li>

                            <li>
                                <a href="admin_dashboard.py">
                                    <i class="fa fa-cog" aria-hidden="true"></i><span>Dashboard</span>
                                </a>
                            </li>

                            <li>
    <a href="javascript: void(0);" class="has-arrow waves-effect">
        <i class="fa fa-building" aria-hidden="true"></i>
        <span>Company Master</span>
    </a>
    <ul class="sub-menu" aria-expanded="true">
        <li><a href="company.py"><i class="fa fa-plus"></i> Add Company</a></li>
        <li><a href="companylist.py"><i class="fa fa-list"></i> Company List</a></li>
    </ul>
</li>

<li>
    <a href="javascript: void(0);" class="has-arrow waves-effect">
        <i class="fa fa-sitemap" aria-hidden="true"></i>
        <span>Department Master</span>
    </a>
    <ul class="sub-menu" aria-expanded="true">
        <li><a href="department.py"><i class="fa fa-plus"></i> Add Department</a></li>
        <li><a href="departmentlist.py"><i class="fa fa-list"></i> Department List</a></li>
    </ul>
</li>

<li>
    <a href="javascript: void(0);" class="has-arrow waves-effect">
        <i class="fa fa-id-badge" aria-hidden="true"></i>
        <span>Designation Master</span>
    </a>
    <ul class="sub-menu" aria-expanded="true">
        <li><a href="designation.py"><i class="fa fa-plus"></i> Add Designation</a></li>
        <li><a href="designationlist.py"><i class="fa fa-list"></i> Designation List</a></li>
    </ul>
</li>

<li>
    <a href="javascript: void(0);" class="has-arrow waves-effect">
        <i class="fa fa-users" aria-hidden="true"></i>
        <span>Employee Master</span>
    </a>
    <ul class="sub-menu" aria-expanded="true">
        <li><a href="employee.py"><i class="fa fa-plus"></i> Add Employee</a></li>
        <li><a href="employeelist.py"><i class="fa fa-list"></i> Employee List</a></li>
    </ul>
</li>

<li>
    <a href="javascript: void(0);" class="has-arrow waves-effect">
        <i class="fa fa-calendar" aria-hidden="true"></i>
        <span>Leave Type Master</span>
    </a>
    <ul class="sub-menu" aria-expanded="true">
        <li><a href="leavetype.py"><i class="fa fa-plus"></i> Add Leave Type</a></li>
        <li><a href="leavetypelist.py"><i class="fa fa-list"></i> Leave Type List</a></li>
    </ul>
</li>

<li>
    <a href="javascript: void(0);" class="has-arrow waves-effect">
        <i class="fa fa-tasks" aria-hidden="true"></i>
        <span>Task Category Master</span>
    </a>
    <ul class="sub-menu" aria-expanded="true">
        <li><a href="taskcategory.py"><i class="fa fa-plus"></i> Add Task Category</a></li>
        <li><a href="taskcategorylist.py"><i class="fa fa-list"></i> Task Category List</a></li>
    </ul>
</li>

<li>
    <a href="javascript: void(0);" class="has-arrow waves-effect">
        <i class="fa fa-handshake-o" aria-hidden="true"></i>
        <span>Client Master</span>
    </a>
    <ul class="sub-menu" aria-expanded="true">
        <li><a href="client.py"><i class="fa fa-plus"></i> Add Client</a></li>
        <li><a href="clientlist.py"><i class="fa fa-list"></i> Client List</a></li>
    </ul>
</li>

<li>
    <a href="javascript: void(0);" class="has-arrow waves-effect">
        <i class="fa fa-tasks" aria-hidden="true"></i>
        <span>Task Assignment</span>
    </a>
    <ul class="sub-menu" aria-expanded="true">
        <li><a href="taskassignment.py"><i class="fa fa-plus"></i> Assign Task</a></li>
        <li><a href="taskassignmentlist.py"><i class="fa fa-list"></i> Task Assignment List</a></li>
    </ul>
</li>
      
      <li>
                            <a href="managerleave.py" class="waves-effect">
                                <i class="fa fa-calendar"></i>
                                <span>Leave Application</span>
                            </a>
                        </li>
                        </ul>
                    </div>
                    <!-- Sidebar -->
                </div>
            </div>
            <!-- Left Sidebar End -->

            

            <!-- ============================================================== -->
            <!-- Start right Content here -->
          
''')
