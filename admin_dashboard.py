#!C:\Python310\python.exe
import cgi, cgitb
import mysql.connector
import header   # import header template
cgitb.enable()

print("Content-Type: text/html\n")

# ---- Database Connection ----
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="drw"
)
cur = db.cursor(dictionary=True)

# ---- Summary Counts ----
def fetch_one(query):
    cur.execute(query)
    return cur.fetchone()

total_employees = fetch_one("SELECT COUNT(*) AS total_employees FROM employee_master")
today_tasks     = fetch_one("SELECT COUNT(*) AS today_tasks FROM task_assignment WHERE date_assign = CURDATE()")
completed_today = fetch_one("SELECT COUNT(*) AS completed_today FROM task_assignment WHERE status='Completed' AND date_assign = CURDATE()")
completed_week  = fetch_one("SELECT COUNT(*) AS completed_week FROM task_assignment WHERE status='Completed' AND date_assign >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)")
completed_month = fetch_one("SELECT COUNT(*) AS completed_month FROM task_assignment WHERE status='Completed' AND date_assign >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)")
pending_tasks   = fetch_one("SELECT COUNT(*) AS pending_tasks FROM task_assignment WHERE status='Pending'")

# ---- Task Status Pie ----
cur.execute("SELECT status, COUNT(*) AS cnt FROM task_assignment GROUP BY status")
status_data = cur.fetchall()
status_dict = {"Pending": 0, "In Progress": 0, "Completed": 0}
for row in status_data:
    status_dict[row['status']] = row['cnt']

# ---- Task Categories Pie ----
cur.execute("""
    SELECT c.category_name, COUNT(t.id) AS cnt
    FROM task_assignment t
    JOIN task_category c ON t.task_category_id = c.id
    GROUP BY c.category_name
""")
category_data = cur.fetchall()

# ---- Task Completion by Employee (Bar) ----
cur.execute("""
    SELECT e.name,
        SUM(CASE WHEN t.status='Completed' THEN 1 ELSE 0 END) AS completed,
        SUM(CASE WHEN t.status='Pending' OR t.status='In Progress' THEN 1 ELSE 0 END) AS pending
    FROM task_assignment t
    JOIN employee_master e ON t.assign_to = e.id
    GROUP BY e.name
""")
employee_data = cur.fetchall()

# ---- Task Locations for Map ----
cur.execute("""
    SELECT e.name, t.title, w.latitude, w.longitude, w.status, c.category_name
    FROM work_report w
    JOIN employee_master e ON w.emp_id = e.id
    JOIN task_assignment t ON w.task_id = t.id
    JOIN task_category c ON t.task_category_id = c.id
    WHERE w.latitude IS NOT NULL AND w.longitude IS NOT NULL
""")
map_data = cur.fetchall()

# ---- Charts & Map Scripts ----
print("""
<script src="https://www.gstatic.com/charts/loader.js"></script>
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_GOOGLE_MAPS_API_KEY"></script>
<script>
google.charts.load('current', {'packages':['corechart','bar']}); 
google.charts.setOnLoadCallback(drawCharts);

function drawCharts() {
    // ---- Task Status Pie ----
    var status_data = google.visualization.arrayToDataTable([
        ['Status', 'Tasks'],
        ['Pending', """+str(status_dict['Pending'])+""" ],
        ['In Progress', """+str(status_dict['In Progress'])+""" ],
        ['Completed', """+str(status_dict['Completed'])+""" ]
    ]);
    var status_chart = new google.visualization.PieChart(document.getElementById('status_pie'));
    status_chart.draw(status_data, {title: 'Task Status Distribution'});

    // ---- Task Categories Pie ----
    var category_data = google.visualization.arrayToDataTable([
        ['Category', 'Tasks'],
""")
if category_data:
    for row in category_data:
        print(f"['{row['category_name']}', {row['cnt']}],")
else:
    print("['No Data', 1],")
print("""
    ]);
    var category_chart = new google.visualization.PieChart(document.getElementById('category_pie'));
    category_chart.draw(category_data, {title: 'Task Categories'});

    // ---- Task Completion by Employee (Bar) ----
    var employee_data = google.visualization.arrayToDataTable([
        ['Employee', 'Completed', 'Pending'],
""")
if employee_data:
    for row in employee_data:
        print(f"['{row['name']}', {row['completed']}, {row['pending']}],")
else:
    print("['No Data', 0, 0],")
print("""
    ]);
    var employee_chart = new google.visualization.ColumnChart(document.getElementById('employee_chart'));
    employee_chart.draw(employee_data, {title: 'Task Completion by Employee', bars: 'vertical'});
}

function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 6,
        center: {lat: 19.7515, lng: 75.7139}
    });
""")

if map_data:
    for row in map_data:
        lat = row['latitude'] if row['latitude'] else "19.7515"
        lng = row['longitude'] if row['longitude'] else "75.7139"
        title = f"{row['name']} - {row['title']} ({row['category_name']} - {row['status']})"
        print(f"""
    new google.maps.Marker({{
        position: {{lat: {lat}, lng: {lng}}},
        map: map,
        title: "{title}"
    }});
    """)
else:
    print("""console.log("No map data available");""")

print("""
}
</script>
""")

# ---- Dashboard Body ----
print(f"""
<div class="main-content">
<div class="page-content">
<div class="container-fluid">

  <h2 class="mb-4 text-center">Manager Dashboard</h2>

  <!-- Summary Cards -->
  <div class="row mb-4">
    <div class="col-md-3"><div class="card text-bg-primary"><div class="card-body text-center"><h6>Total Employees</h6><h3>{total_employees['total_employees']}</h3></div></div></div>
    <div class="col-md-3"><div class="card text-bg-success"><div class="card-body text-center"><h6>Tasks Today</h6><h3>{today_tasks['today_tasks']}</h3></div></div></div>
    <div class="col-md-3"><div class="card text-bg-warning"><div class="card-body text-center"><h6>Completed Today</h6><h3>{completed_today['completed_today']}</h3></div></div></div>
    <div class="col-md-3"><div class="card text-bg-danger"><div class="card-body text-center"><h6>Pending Tasks</h6><h3>{pending_tasks['pending_tasks']}</h3></div></div></div>
  </div>

  <!-- Week/Month Stats -->
  <div class="row mb-4">
    <div class="col-md-4"><div class="card"><div class="card-body text-center"><h6>Completed This Week</h6><h3>{completed_week['completed_week']}</h3></div></div></div>
    <div class="col-md-4"><div class="card"><div class="card-body text-center"><h6>Completed This Month</h6><h3>{completed_month['completed_month']}</h3></div></div></div>
    <div class="col-md-4"><div class="card"><div class="card-body text-center"><h6>Total Tasks</h6><h3>{today_tasks['today_tasks']+completed_week['completed_week']+pending_tasks['pending_tasks']}</h3></div></div></div>
  </div>

  <!-- Charts -->
  <div class="row">
    <div class="col-md-6"><div id="status_pie" style="width:100%; height:400px;"></div></div>
    <div class="col-md-6"><div id="category_pie" style="width:100%; height:400px;"></div></div>
  </div>
  <div class="row mt-4">
    <div class="col-12"><div id="employee_chart" style="width:100%; height:400px;"></div></div>
  </div>

  <!-- Map -->
  <div class="row mt-4">
    <div class="col-12"><div id="map" style="width:100%; height:500px;"></div></div>
  </div>

</div>
</div>
</div>

</div> <!-- layout-wrapper end -->
</body>
</html>
""")

import footer
