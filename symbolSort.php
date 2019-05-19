<?php
    $cnx = new mysqli('localhost', 'ananya', 'password', 'test');
    if ($cnx->connect_error)
        die('Connection failed: ' . $cnx->connect_error);

    $query = 'SELECT * FROM test.Stocks1 ORDER BY symbol';
    $cursor = $cnx->query($query);
    

    echo "<table border='1'>";
    echo "<tr><td>" . "<b>EXCHANGE</b>" . "</td><td>" . "<b>SYMBOL</b>" . "</td><td>" . '<b><a href="main.php">COMPANY</a></b>' . "</td><td>" . "<b>VOLUME</b>" . "</td><td>" . "<b>PRICE($)</b>" . "</td><td>" . "<b>CHANGE</b>" . "</td>";
    while ($row = $cursor->fetch_assoc()) {
        echo "<tr><td>" . $row['exchange'] . "</td><td>" . $row['symbol'] . "</td><td>" . $row['company'] . "</td><td>". $row['volume'] . "</td><td>" .  $row['price'] . "</td><td>" . $row['chang'] . "</td><tr>";
    }

    echo "</table>";

    $cnx->close();
?>
