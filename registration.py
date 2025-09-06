#!C:\Python310\python.exe
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")

print('''
<!doctype html>
<html lang="en">
 <head>
    <meta charset="utf-8" />
    <title>Register | Minible - Admin & Dashboard Template</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="assets/css/bootstrap.min.css" id="bootstrap-style" rel="stylesheet" type="text/css" />
    <link href="assets/css/icons.min.css" rel="stylesheet" type="text/css" />
    <link href="assets/css/app.min.css" id="app-style" rel="stylesheet" type="text/css" />
</head>

<body class="authentication-bg">
    <div class="account-pages my-5 pt-sm-5">
        <div class="container">
            <div class="row align-items-center justify-content-center">
                <div class="col-md-8 col-lg-6 col-xl-5">
                    <div class="card">
                        <div class="card-body p-4"> 
                            <div class="text-center mt-2">
                                <h5 class="text-primary">Register Account</h5>
                            </div>
                            <div class="p-2 mt-4">
                                <!-- IMPORTANT: Post to registration_process.py -->
                                <form action="registration_process.py" method="post">
                                    
                                    <div class="mb-3">
                                        <label class="form-label" for="username">Username</label>
                                        <input type="text" class="form-control" id="username" name="username" placeholder="Enter username" required>        
                                    </div>

                                    <div class="mb-3">
                                        <label class="form-label" for="userpassword">Password</label>
                                        <input type="password" class="form-control" id="userpassword" name="userpassword" placeholder="Enter password" required>        
                                    </div>

                                    <div class="mb-3">
                                        <label class="form-label" for="role">Role</label>
                                        <select class="form-control w-100" id="role" name="role" required>
                                            <option value="Manager">Manager (Admin)</option>
                                            <option value="Executive">Executive (Worker)</option>
                                        </select>
                                    </div>

                                    <div class="mb-3">
                                        <label class="form-label" for="status">Status</label>
                                        <select class="form-control w-100" id="status" name="status" required>
                                            <option value="Active">Active</option>
                                            <option value="Inactive">Inactive</option>
                                        </select>
                                    </div>
                                    
                                    <div class="mt-3 text-end">
                                        <button class="btn btn-primary w-sm waves-effect waves-light" type="submit">Register</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
''')
