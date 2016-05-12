<?php
$servername = "localhost";
$username = "demo";
$password = "demo";
$dbname = "masscan_api";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
//echo "Connected successfully\n";
if ($_GET["get"] == "host") {
$sql = "SELECT Host, Port, Wait, Shard FROM api WHERE Wait=0 AND Complete=0 LIMIT 1;";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
//        echo "Host: " . $row["Host"]. " - Port: " . $row["Port"]. " " . $row["Wait"]. "<br>";
          $host = $row["Host"];
          $port = $row["Port"];
          $wait = $row["Wait"];
          $shard = $row["Shard"];
    }
} else {
    echo "No jobs available at this time";
    $conn->close();
}
echo "{" . "\"host\"" ." : " . "\"" . $host . "\"" . ", \"port\"" . " : " . "\"" . $port . "\"" . ", \"shard\"" . " : " . "\"" . $shard . "\"" . "}";
$sql = "UPDATE api SET Wait='1' WHERE Host='$host' AND Port='$port' AND Shard='$shard'";
$result = $conn->query($sql);
}
if ($_GET["complete"] == "yes") {
//Set parms
$current_host = $_GET["host"];
$current_port = $_GET["port"];
$current_shard = $_GET["shard"];
echo $current_host . " " . $current_port . " " . $current_shard;
$sql = "UPDATE api SET Wait='0', Complete='1' WHERE Host='$current_host' AND Port='$current_port' AND Shard='$current_shard'";
$result = $conn->query($sql);
}
$conn->close();
?>
