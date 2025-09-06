#!C:\Python310\python.exe
import cgitb, mysql.connector, cgi
cgitb.enable()
print("Content-Type: text/html\n")

import header

form = cgi.FieldStorage()
filter_date = form.getvalue("date")
filter_emp  = form.getvalue("employee_id")
filter_status = form.getvalue("status")

# DB Connection
mydb = mysql.connector.connect(host="localhost", user="root", password='', database="drw")
cur = mydb.cursor(dictionary=True)

# Total Employees
cur.execute("SELECT COUNT(*) as total FROM employee_master")
total_employees = cur.fetchone()['total']

# Tasks Assigned Today
cur.execute("SELECT COUNT(*) as total FROM task_assignment WHERE DATE(date_assign)=CURDATE()")
tasks_today = cur.fetchone()['total']

# Completed Today
cur.execute("SELECT COUNT(*) as total FROM task_assignment WHERE status='Completed' AND DATE(date_assign)=CURDATE()")
completed_today = cur.fetchone()['total']

# Completed This Week
cur.execute("SELECT COUNT(*) as total FROM task_assignment WHERE status='Completed' AND YEARWEEK(date_assign,1)=YEARWEEK(CURDATE(),1)")
completed_week = cur.fetchone()['total']

# Completed This Month
cur.execute("SELECT COUNT(*) as total FROM task_assignment WHERE status='Completed' AND MONTH(date_assign)=MONTH(CURDATE()) AND YEAR(date_assign)=YEAR(CURDATE())")
completed_month = cur.fetchone()['total']

# Pending Tasks
cur.execute("SELECT COUNT(*) as total FROM task_assignment WHERE status='Pending'")
pending_tasks = cur.fetchone()['total']

print(f"""
<div class='main-content'>
 <div class='page-content'>
  <div class='container-fluid'>
    <div class='row'>

      <div class='col-md-3'>
        <div class='card'><div class='card-body'><h4>Total Employees</h4><h3>{total_employees}</h3></div></div>
      </div>
      <div class='col-md-3'>
        <div class='card'><div class='card-body'><h4>Tasks Assigned Today</h4><h3>{tasks_today}</h3></div></div>
      </div>
      <div class='col-md-3'>
        <div class='card'><div class='card-body'><h4>Completed Today</h4><h3>{completed_today}</h3></div></div>
      </div>
      <div class='col-md-3'>
        <div class='card'><div class='card-body'><h4>Pending Tasks</h4><h3>{pending_tasks}</h3></div></div>
      </div>

    </div>

    <div class='row'>
      <div class='col-md-4'><div class='card'><div class='card-body'><h5>Completed This Week</h5><h3>{completed_week}</h3></div></div></div>
      <div class='col-md-4'><div class='card'><div class='card-body'><h5>Completed This Month</h5><h3>{completed_month}</h3></div></div></div>
    </div>
""")

# Employee Task Completion %
cur.execute("""
SELECT e.name,
       SUM(CASE WHEN t.status='Completed' THEN 1 ELSE 0 END) as completed,
       COUNT(t.id) as total
FROM employee_master e
LEFT JOIN task_assignment t ON e.id=t.assign_to
GROUP BY e.id
""")
rows = cur.fetchall()

print("""
<div class='row'>
 <div class='col-lg-12'>
  <div class='card'><div class='card-body'>
   <h4>Task Completion % by Employee</h4>
   <table class='table table-bordered'>
     <thead><tr><th>Employee</th><th>Completed</th><th>Total</th><th>%</th></tr></thead>
     <tbody>
""")

for r in rows:
    percent = round((r['completed']/r['total']*100),2) if r['total']>0 else 0
    print(f"<tr><td>{r['name']}</td><td>{r['completed']}</td><td>{r['total']}</td><td>{percent}%</td></tr>")

print("""
     </tbody>
   </table>
  </div></div>
 </div>
</div>
""")

# Map (using dummy lat/lng fields in task_assignment, add to your schema)
cur.execute("SELECT e.name, t.latitude, t.longitude FROM task_assignment t JOIN employee_master e ON t.assign_to=e.id WHERE t.latitude IS NOT NULL AND t.longitude IS NOT NULL")
locations = cur.fetchall()

print("""
<div class='row'>
 <div class='col-lg-12'>
  <div class='card'><div class='card-body'>
   <h4>Live Task Locations</h4>
   <div id="map" style="height:400px;"></div>
  </div></div>
 </div>
</div>

<script>
function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), { zoom: 6, center: {lat: 20.5937, lng: 78.9629} });
""")

for loc in locations:
    print(f"new google.maps.Marker({{ position: {{lat:{loc['latitude']}, lng:{loc['longitude']}}}, map: map, title:'{loc['name']}' }});")

print("""
}
</script>
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap" async defer></script>
""")

print("</div></div></div>")
import footer
