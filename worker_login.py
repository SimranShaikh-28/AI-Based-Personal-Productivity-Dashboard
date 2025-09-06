#!C:\Python310\python.exe
import cgitb
cgitb.enable()

print("Content-Type: text/html\n")
print('''
<!doctype html>
<html lang="en">
 <head>
    <meta charset="utf-8" />
    <title>Worker Login </title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="assets/images/favicon.ico">
    <link href="assets/css/bootstrap.min.css" id="bootstrap-style" rel="stylesheet" type="text/css" />
    <link href="assets/css/icons.min.css" rel="stylesheet" type="text/css" />
    <link href="assets/css/app.min.css" id="app-style" rel="stylesheet" type="text/css" />

    <style>
      body.authentication-bg {
          background: url("assets/images/admin-bg.png") no-repeat center center fixed;
          
      }
      .card {
          background: rgba(255, 255, 255, 0.92); /* semi-transparent so text is readable */
          border-radius: 15px;
          box-shadow: 0 8px 20px rgba(0,0,0,0.3);
      }
    </style>
 </head>

 <body class="authentication-bg">
    <div class="account-pages my-5 pt-sm-5">
        <div class="container">
            <div class="row align-items-center justify-content-center">
                <div class="col-md-8 col-lg-6 col-xl-5">
                    <div class="card">
                        <div class="text-center"><div></div></div>
                        <div class="card-body p-4">
                            <div class="text-center mt-2">
                                <h5 class="text-primary">Worker Login</h5>
                                <p class="text-muted">Sign in to continue.</p>
                            </div>
                            <div class="p-2 mt-4">
                                <form action="worker_process.py" method="post">
                                    <div class="mb-3">
                                        <label class="form-label" for="username">Worker Username</label>
                                        <input type="text" class="form-control" id="username" name="username" placeholder="Enter username" required>
                                    </div>
                                    <div class="mb-3">
                                        <label class="form-label" for="userpassword">Password</label>
                                        <input type="password" class="form-control" id="userpassword" name="userpassword" placeholder="Enter password" required>
                                    </div>
                                    <div class="mt-3 text-end">
                                        <button class="btn btn-success w-sm waves-effect waves-light" type="submit">Login</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="assets/libs/jquery/jquery.min.js"></script>
    <script src="assets/libs/bootstrap/js/bootstrap.bundle.min.js"></script>
    <script src="assets/libs/metismenu/metisMenu.min.js"></script>
    <script src="assets/libs/simplebar/simplebar.min.js"></script>
    <script src="assets/libs/node-waves/waves.min.js"></script>
    <script src="assets/libs/waypoints/lib/jquery.waypoints.min.js"></script>
    <script src="assets/libs/jquery.counterup/jquery.counterup.min.js"></script>
 </body>
</html>
''')
