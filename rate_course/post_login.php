<!--Receive login information from login.html-->
<html>
<head>
	<title> Check and respond to login information</title>
</head>

<body>
<?php

//connect to the database 'RateCourse'
include "db.php";

//get the username and password from login.html
$username = $_POST['username'];
$password = $_POST['password'];


//protect against SQL injection
$username = stripslashes($username);
$password = stripslashes($password);
$username = $con->real_escape_string($username);
$password = $con->real_escape_string($password);

$query = "SELECT * FROM USERS WHERE USERNAME ='$username' AND PASSWORD = '$password'";

if ($result = $con->query($query)){
	$count = $result->num_rows;
	}

//Register session variables and redirect users to login_success.php page
if ($count==1){
	session_start();
	$_SESSION['MyUserName'] = $username;
	while ($result_ar = mysqli_fetch_assoc($result)){
		$_SESSION['Role'] = $result_ar['ROLE'];
		}
	header("location: login_success.php");
	}
else {
	echo "Wrong username or password";
	?>
	<a href = "login.html">Return to login</a>
	
	<?php
	}

?>

</body>

</html>
