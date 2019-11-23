<html>
<head>
    <title>SQL SELECT Statement</title>
</head>
<body>
<table align="center" border="1">
<?php
    $cnx = new mysqli('localhost', 'root', 'password', 'demo');

    if ($cnx->connect_error)
        die('Connection failed: ' . $cnx->connect_error);

    $query = 'SELECT * FROM demo.Nasdaq ORDER BY price';
    $cursor = $cnx->query($query);

    echo "<tr><td>" . "<b>EXCHANGE</b>" . "</td><td>" . '<b><a href="symbol.php">SYMBOL</a></b>' . "</td><td>" . '<b><a href="company.php">COMPANY</a></b>' . "</td><td>" . "<b><a href=volume.php>VOLUME</a></b>" . "</td><td>" . "<b><a href=price.php>PRICE($)</a></b>" . "</td><td>" . "<b><a href=change.php>CHANGE</a></b>" . "</td>";
    while ($row = $cursor->fetch_assoc()) {
        echo '<tr>';
        echo '<td>' . $row['exchangee'] . '</td><td>' . $row['symbol'] . '</td><td>' . $row['company'] . '</td><td>' . $row['volume'] . '</td><td>' . $row['price'] . '</td><td align="right">' . $row['changee'] .'</td>';
        echo '</tr>';
    }

    $cnx->close();
?>
</table>
</body>
</html>