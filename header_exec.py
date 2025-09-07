#!C:\Python310\python.exe
import cgi
import cgitb
import os
import http.cookies
import mysql.connector

cgitb.enable()
print("Content-Type: text/html\n") 

form = cgi.FieldStorage()
workerid = form.getvalue("workerid")

if not workerid:
    cookies = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE", ""))
    workerid = cookies["workerid"].value if "workerid" in cookies else None

worker_name = "Executive"
if workerid:
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="", database="drw")
        cur = db.cursor(dictionary=True)
        cur.execute("SELECT name FROM employee_master WHERE id=%s AND role='Executive'", (workerid,))
        row = cur.fetchone()
        if row:
            worker_name = row["name"]
        cur.close()
        db.close()
    except Exception as e:
        worker_name = "Executive"

def get_admin_display_name():
    cookies = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE", ""))
    if "workername" in cookies and cookies["workername"].value.strip():
        return cookies["workername"].value.strip()
    return "Marcus"  # fallback if no cookie

emp_id = workerid
emp_name = worker_name


print(f'''
<!doctype html>
<html lang="en">

 <head>
        
        <meta charset="utf-8" />
        <title>AI-Based Personal Productivity Dashboard</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta content="Premium Multipurpose Admin & Dashboard Template" name="description" />
        <meta content="Themesbrand" name="author" />
        <!-- App favicon -->
        <link rel="shortcut icon" href="assets/images/image.png">

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
                                
           <span class="d-none d-xl-inline-block ms-1 fw-medium font-size-15">{worker_name}</span>
                                <i class="uil-angle-down d-none d-xl-inline-block font-size-15"></i>
                            </button>
                            <div class="dropdown-menu dropdown-menu-end">
                                <a class="dropdown-item" href="#"><i class="uil uil-sign-out-alt font-size-18 align-middle me-1 text-muted"></i> <span class="align-middle">Sign out</span></a>
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
                            <li class="menu-title">Welcome To View Task</li>

                            <li>
                                <a href="worker_dashboard.py">
                                    <i class="fa fa-cog" aria-hidden="true"></i><span>Dashboard</span>
                                </a>
                            </li>

                            
                        <li>
                            <a href="tasks.py" class="waves-effect">
                                <i class="fa fa-tasks"></i>
                                <span>Task</span>
                            </a>
                        </li>

                        <li>
                            <a href="leave.py" class="waves-effect">
                                <i class="fa fa-calendar"></i>
                                <span>Apply Leave</span>
                            </a>
                        </li>

                        <li>
                            <a href="worker_leave.py" class="waves-effect">
                                <i class="fa fa-calendar"></i>
                                <span>View Leave</span>
                            </a>
                        </li>

                        <li>
                            <a href="workreportlist.py" class="waves-effect">
                                <i class="fa fa-calendar"></i>
                                <span>My Work Report List</span>
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>

                    <!-- Sidebar -->
                </div>
            </div>
            <!-- Left Sidebar End -->

            


            <!-- ============================================================== -->
            <!-- Start right Content here -->
          
''')

