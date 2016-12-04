<!DOCTYPE html>
<html lang="en">
	<head>
		<title> RecruitMe </title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
  		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
	</head>
	<body>
		<div class="container">

			<!-- Filter -->
			<div class="row">
				<div class="panel panel-default col-lg-4">
					<div class="panel-heading">
						<h4>
						FILTER
						</h4>
					</div>
					<div class="panel-body" style="min-height: 500px; max-height: 500px;">
						<ul class="list-unstyled">
							<!-- Collapsable Major checkboxes -->
							<li>
								<a data-toggle="collapse" href="#majorCollapse"><span class="glyphicon glyphicon glyphicon-circle-arrow-down"></span> Major</a>
								<div id="majorCollapse" class="panel-collapse collapse">
							      <form>
							      	<div class="checkbox">
									  <label><input type="checkbox" checked="true" value="">Accounting</label>
									</div>
									<div class="checkbox">
									  <label><input type="checkbox" value="" checked="true">Computer Science</label>
									</div>
							      </form>
							    </div>
						    </li>

						    <!-- Collapsable GPA checkboxes -->
							<li>
							    <a data-toggle="collapse" href="#gpaCollapse"><span class="glyphicon glyphicon glyphicon-circle-arrow-down"></span> GPA</a>
								<div id="gpaCollapse" class="panel-collapse collapse">
							      <form>
							      	<div class="checkbox">
									  <label><input type="checkbox" value="" checked="true">2.00 - 2.99</label>
									</div>
									<div class="checkbox">
									  <label><input type="checkbox" value="" checked="true">3.00 - 3.99</label>
									</div>
									<div class="checkbox">
									  <label><input type="checkbox" value="" checked="true">4.00+</label>
									</div>
							      </form>
							    </div>
						    </li>

						    <!-- Collapsable college checkboxes -->
						    <li>
							    <a data-toggle="collapse" href="#collegeCollapse"><span class="glyphicon glyphicon glyphicon-circle-arrow-down"></span> College</a>
								<div id="collegeCollapse" class="panel-collapse collapse">
							      <form>
							      	<div class="checkbox">
									  <label><input type="checkbox" value="" checked="true">Kansas State University</label>
									</div>
									<div class="checkbox">
									  <label><input type="checkbox" value="" checked="true">Oklahoma State University</label>
									</div>
							      </form>
							    </div>
						    </li>
					    </ul>
					    <button type="button" class="btn btn-success"><span class="glyphicon glyphicon-repeat"></span> FILTER</button>
					</div>
					<div class="panel-footer">
						<button type="button" class="btn btn-danger" onclick="deleteAccount()">DELETE ACCOUNT</button>
					</div>
				</div>

				<!-- Main header -->
				<div class="panel panel-default col-lg-8">
					<div class="panel-heading"><h4>FIND A CANDIDATE</h4></div>
					<div class="panel-body" style="min-height: 500px; max-height: 500px;">
						<!-- Student Info Table -->
						<table class = "table table-hover">
							<thead>
								<th> First Name </th>
								<th> Last Name </th>
								<th> Email </th>
								<th> Major </th>
								<th> College </th>
								<th> GPA </th>
							</thead>
							<tbody>
								<tr>
							        <td>
							        	<?php
											$servername = "mysql.cis.ksu.edu";
											$username = "mhixon";
											$password = "cis560";
											$dbname = "mhixon";

											// Create connection
											$conn = new mysqli($servername, $username, $password, $dbname);
											// Check connection
											if ($conn->connect_error) {
											    die("Connection failed: " . $conn->connect_error);
											} 

											$sql = "SELECT student_ID FROM Student";
											$result = $conn->query($sql);

											if ($result->num_rows > 0) {
											    // output data of each row
											    while($row = $result->fetch_assoc()) {
											        echo "id: " . $row["student_ID"].;
											    }
											} else {
											    echo "0 results";
											}
											$conn->close();
										?>
							        </td>
								</tr>
							</tbody>
						</table>
					</div>
				</div>
			</div>
		</div>
		<script>
			function deleteAccount() {
			    window.alert("Account deleted.");
			}
		</script>
	</body>
</html>