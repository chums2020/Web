<!--Select a database to work with-->
<?php
$con = new mysqli('localhost','root','xxxxxxxx');//password is omitted for now
if (!$con){
		echo "Connection failed: ".$con->error;
		exit();
	}
	
$con->select_db("RateCourse"); 
echo "Selected the RateCourse database";
?>
