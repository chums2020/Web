<!--Where to include menu.php?-->
<?php
	include "menu.php";
?>
<html>
<head>
	<title> User's login page</title>
</head>
<body>

	<h1>RateCourse Login Page</h1>
	<form action = "post_login.php" method = "post">
		<p>Username: <input name = "username" type = "text"></p>
		<p>Password: <input name = "password" type = "password"></p>
		<p><input name = "login" type = "submit", value = "Login"></p>
	</form>
</body>
</html>
