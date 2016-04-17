<html>
<body>
	<?php
	#Create an object of mysqli
	$con = new mysqli('localhost','root','xxxxxxxx'); //password is omitted
	if (!$con){
		die('Couldn not connect '.$con->error);
	}
	echo 'Connected successfully to mySQL.<br>';
	
	$con->query("CREATE DATABASE IF NOT EXISTS RateCourse");
	echo "Create DB RateCourse, if not already exists";
	$con->select_db("RateCourse");
	echo "Selected the database RateCourse";
	
	//create a USERS table
	$query = "CREATE TABLE USERS 
			  (id int(5) NOT NULL AUTO_INCREMENT,
				username varchar(30) NOT NULL,
				password varchar(30) NOT NULL,
				email varchar(60) NOT NULL,
				role varchar(30) NOT NULL,
				school varchar(30),
				graduate_date date,
				join_date date NOT NULL,
				PRIMARY KEY (id))";
	if ($con->query($query)===TRUE){
		echo "<p>Database table 'USERS' created </p>";
	}		  
	else {echo "<p>Error:</p> ".$con->error;}
	?>
</body>
</html>
