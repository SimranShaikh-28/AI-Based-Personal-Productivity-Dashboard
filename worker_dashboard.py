#!C:\Python310\python.exe
import cgi, cgitb
import mysql.connector
import header_exec   # import header template
cgitb.enable()

print("Content-Type: text/html\n")

# ---- Simulated login (replace with session handling later) ----
logged_in_user_id = 1  # hardcode for now

# ---- Database Connection ----
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="drw"
)
cur = db.cursor(dictionary=True)

# ---- Tasks for Today ----
cur.execute("SELECT COUNT(*) AS cnt FROM task_assignment WHERE assign_to=%s AND date_assign=CURDATE()", (logged_in_user_id,))
tasks_today = cur.fetchone()

# ---- Completed Tasks Summary ----
cur.execute("SELECT COUNT(*) AS cnt FROM task_assignment WHERE assign_to=%s AND status='Completed'", (logged_in_user_id,))
completed_summary = cur.fetchone()

# ---- Task Status Tracker ----
cur.execute("""
    SELECT status, COUNT(*) AS cnt 
    FROM task_assignment 
    WHERE assign_to=%s
    GROUP BY status
""", (logged_in_user_id,))
status_data = cur.fetchall()
status_dict = {"Pending": 0, "In Progress": 0, "Completed": 0}
for row in status_data:
    status_dict[row['status']] = row['cnt']

# ---- Latest Google Maps Location ----
cur.execute("""
    SELECT latitude, longitude, t.title, w.status
    FROM work_report w
    JOIN task_assignment t ON w.task_id = t.id
    WHERE w.emp_id=%s AND w.latitude IS NOT NULL AND w.longitude IS NOT NULL
    ORDER BY w.created_at DESC LIMIT 1
""", (logged_in_user_id,))
latest_location = cur.fetchone()

# ---- Scripts ----
print("""
<script src="https://www.gstatic.com/charts/loader.js"></script>
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_GOOGLE_MAPS_API_KEY"></script>
<script>
google.charts.load('current', {'packages':['corechart','bar']}); 
google.charts.setOnLoadCallback(drawCharts);

function drawCharts() {
    var status_data = google.visualization.arrayToDataTable([
        ['Status', 'Tasks'],
        ['Pending', """+str(status_dict['Pending'])+"""],
        ['In Progress', """+str(status_dict['In Progress'])+"""],
        ['Completed', """+str(status_dict['Completed'])+"""]
    ]);
    var chart = new google.visualization.ColumnChart(document.getElementById('status_chart'));
    chart.draw(status_data, {title: 'Task Status Tracker', bars: 'vertical'});
}

function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 6,
        center: {lat: 19.7515, lng: 75.7139}
    });
""")

if latest_location:
    print(f"""
    new google.maps.Marker({{
        position: {{lat: {latest_location['latitude']}, lng: {latest_location['longitude']}}},
        map: map,
        title: "{latest_location['title']} ({latest_location['status']})"
    }});
    map.setCenter({{lat: {latest_location['latitude']}, lng: {latest_location['longitude']}}});
    """)
else:
    print("""console.log("No location data for this user");""")

print("""
}
</script>
""")

# ---- Dashboard ----
print(f"""
<div class="main-content">
<div class="page-content">
<div class="container-fluid">

  <h2 class="mb-4 text-center">Worker Dashboard</h2>

  <!-- Tasks for Today -->
  <div class="row mb-4">
    <div class="col-md-6">
      <div class="card text-bg-primary text-center">
        <div class="card-body">
          <h5>Tasks for Today</h5>
          <h2>{tasks_today['cnt']}</h2>
        </div>
      </div>
    </div>

    <!-- Completed Tasks Summary -->
    <div class="col-md-6">
      <div class="card text-bg-success text-center">
        <div class="card-body">
          <h5>Completed Tasks</h5>
          <h2>{completed_summary['cnt']}</h2>
        </div>
      </div>
    </div>
  </div>

  <!-- Task Status Tracker -->
  <div class="row mb-4">
    <div class="col-12">
      <div id="status_chart" style="width:100%; height:400px;"></div>
    </div>
  </div>

  <!-- Google Maps Location -->
  <div class="row mb-4">
    <div class="col-12">
      <div id="map" style="width:100%; height:500px;"></div>
    </div>
  </div>

</div>
</div>
</div>

</div> <!-- layout-wrapper end -->
</body>
</html>
""")

import footer
