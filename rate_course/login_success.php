<!--session_start() must go before the html tag; otherwise it won't work-->
<?php
session_start();
//if the session variable 'MyUserName' is not set, redirect the user to login page
if(!isset($_SESSION['MyUserName'])){
	header("location: login.html");
	}

?>
<html>
<head>

</head>

<body>
<?php
include 'menu.php';

$username = $_SESSION['MyUserName'];
echo "Hello, $username!";
?>



</body>
</html>
