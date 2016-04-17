<?php
include "menu.php";
?>
<html>
<head>
<title> Register a new account at RateCourse</title>
</head>
<body>
<h1> Register an account at RateCourse</h1>

<form action = "registration.php" method = "post">
<p>Email: <input name = "email" type="email"> </p>
<p>Username: <input name = "username" type = "text"></p>
<p>Password: <input name= "password" type= "password"> </p>
<p>School: <input name = "school" type = "text"> </p> <!--prompt a new window to search, or enable automatic search from dropdown -->
<p> Graduation date: <input name = "graduate_date" type = "date"  max="2020-12-31"></p>
<p><input type = "submit" name = "submit reg" value = "register now"></p>
</form>

</body>

</html>
