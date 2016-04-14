<!--Display today's working hours-->
<html>
	<body>
		<h1> Welcome to Claire's Bistro</h1>
		<h2> Operating Hours</h2> 
		<?php
			$current_time =  date("r");
			echo "<br>". "Current time is $current_time"."<br>";
			date_default_timezone_set("EST");
			/*date("l"): A full textual representation of the day of the week*/
			if (date("l") == "Saturday" || date("l") == "Sunday"){
				echo "Today the store is open from 9 AM - 9 PM";
				}
			if (date("l") == "Monday"){
				echo "Today we're close.";
				}
			else{
				/*date("F"): A full textual representation of the month*/
				if (date("F")=="July"|| date("F")=="August"){
					echo "Today the store is open from 10 AM - 7 PM";
					}
				else{
					echo "Today the store is open from 10 AM - 6 PM";
					}
				}
			
		?>
	</body>
	
</html>
