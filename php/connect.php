<?php
$username = filter_input(INPUT_POST, 'username');
$comment = filter_input(INPUT_POST, 'comment');
$date = filter_input(INPUT_POST, 'date');
if (!empty($username)){
if (!empty($comment)){
if (!empty($date)){
$host = "localhost";
$dbusername = "root";
$dbpassword = "";
$dbname = "blog";
// Create connection
$conn = new mysqli ($host, $dbusername, $dbpassword, $dbname);


if (mysqli_connect_error()){
die('Connect Error ('. mysqli_connect_errno() .') '
. mysqli_connect_error());
}
else{
$sql = "INSERT INTO blogging (username, comment, date)
values ('$username','$comment','$date')";
if ($conn->query($sql)){
    echo "New record is inserted sucessfully";
    header("Location:blogging.php");
    }
    else{
    echo "Error: ". $sql ."
    ". $conn->error;
    }
$conn->close();
}
}
else{
echo "Username should not be empty.;";
die();
}
}
else{
echo "Comment should not be empty";
die();
}
}
?>