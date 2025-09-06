#!C:\Python310\python.exe
import cgitb, mysql.connector
cgitb.enable()
import header_exec
print("Content-Type: text/html\n")

# ---------------------------
# Simulate logged-in executive (later replace with session-based emp_id)
# ---------------------------
emp_id = 1   # Example: Simran Shaikh (id=1 in employee_master)

# ---------------------------
# Database Connection
# ---------------------------
db = mysql.connector.connect(host="localhost", user="root", password="", database="drw")
cursor = db.cursor(dictionary=True)

# ---------------------------
# Dashboard Summary
# ---------------------------
cursor.execute("SELECT COUNT(*) AS total FROM task_assignment WHERE assign_to=%s", (emp_id,))
tasks_total = cursor.fetchone()['total']

cursor.execute("""SELECT COUNT(*) AS completed 
                  FROM work_report 
                  WHERE emp_id=%s AND status='Completed'""", (emp_id,))
completed = cursor.fetchone()['completed']

cursor.execute("""SELECT COUNT(*) AS pending 
                  FROM work_report 
                  WHERE emp_id=%s AND status='Pending'""", (emp_id,))
pending = cursor.fetchone()['pending']

cursor.execute("""SELECT COUNT(*) AS partial 
                  FROM work_report 
                  WHERE emp_id=%s AND status='Partial'""", (emp_id,))
partial = cursor.fetchone()['partial']

# ---------------------------
# HTML Output
# ---------------------------
# print(f'''
# <div class="main-content">
#   <div class="page-content">
#     <div class="container-fluid">

#       <!-- start page title -->
#       <div class="row">
#         <div class="col-12">
#           <div class="page-title-box d-flex align-items-center justify-content-between">
#             <h4 class="mb-0">Executive Dashboard</h4>
#           </div>
#         </div>
#       </div>

#       <!-- Dashboard Cards -->
#       <div class="row">
#         <div class="col-md-3">
#           <div class="card text-center"><div class="card-body"><h5 class="card-title">Total Tasks</h5><h3>{tasks_total}</h3></div></div>
#         </div>
#         <div class="col-md-3">
#           <div class="card text-center"><div class="card-body"><h5 class="card-title">Completed</h5><h3>{completed}</h3></div></div>
#         </div>
#         <div class="col-md-3">
#           <div class="card text-center"><div class="card-body"><h5 class="card-title">Pending</h5><h3>{pending}</h3></div></div>
#         </div>
#         <div class="col-md-3">
#           <div class="card text-center"><div class="card-body"><h5 class="card-title">Partial</h5><h3>{partial}</h3></div></div>
#         </div>
#       </div>

#       <!-- Quick Actions -->
#       <div class="row mt-4">
#         <div class="col-md-6"><a href="workreport.py" class="btn btn-primary w-100"> Upload Work Report</a></div>
#         <div class="col-md-6"><a href="leave.py" class="btn btn-warning w-100"> Apply Leave</a></div>
#       </div>

#       <!-- My Tasks -->
#       <div class="row mt-5">
#         <div class="col-12">
#           <div class="card">
#             <div class="card-body">
#               <h4 class="card-title">My Assigned Tasks</h4>
#               <table class="table table-bordered dt-responsive nowrap" style="width:100%">
#                 <thead>
#                   <tr>
#                     <th>ID</th>
#                     <th>Title</th>
#                     <th>Description</th>
#                     <th>Category</th>
#                     <th>Date Assign</th>
#                     <th>Due Date</th>
#                     <th>Status</th>
#                   </tr>
#                 </thead>
#                 <tbody>
# ''')

# ---------------------------
# Task List for this executive
# ---------------------------
# query = """SELECT t.id,t.title,t.description,t.date_assign,t.due_date,t.status,
#                   c.category_name
#            FROM task_assignment t
#            LEFT JOIN task_category_master c ON t.task_category_id=c.id
#            WHERE t.assign_to=%s
#            ORDER BY t.id DESC"""
# cursor.execute(query, (emp_id,))
# rows = cursor.fetchall()

# for r in rows:
#     print(f"""
#       <tr>
#         <td>{r['id']}</td>
#         <td>{r['title']}</td>
#         <td>{r['description']}</td>
#         <td>{r['category_name']}</td>
#         <td>{r['date_assign']}</td>
#         <td>{r['due_date']}</td>
#         <td>{r['status']}</td>
#       </tr>
#     """)

# print('''
#                 </tbody>
#               </table>
#             </div>
#           </div>
#         </div>
#       </div>

#     </div>
#   </div>
# </div>
# ''')

import footer
