<!--menu.php creates a menu that can be inserted in every page in the website -->
<?php
session_start();
//if the session variable 'MyUserName' is not set, redirect the user to login page
if(isset($_SESSION['MyUserName'])){?>
	<a href = "default.php">Home</a>
	<a href = "form_submit_rating.php">Add a Review</a>
	<a href = "reviews.php">Search Reviews</a>
	<a href = "mission.php"> Mission</a>
	<a href = "contacts.php">Contact Us</a>
	<a href = "edit_profile.php"> Edit Your Profile</a>
	<a href = "logout.php">Log out</a>
	
	<?php
	}
else{?>
	<a href = "default.php">Home</a>
	<a href = "reviews.php">Search Reviews</a>
	<a href = "mission.php"> Mission</a>
	<a href = "contacts.php">Contact Us</a>
	<a href = "login.php">Login</a>
	<a href = "form_registration.php">Register</a>
	<p> Please register an account to share your reviews! </p>
	
	<?php
	}
?>
