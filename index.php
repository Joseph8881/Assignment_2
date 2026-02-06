<?php
$a = $_GET['a'] ?? 2;
$b = $_GET['b'] ?? 3;
$c = $_GET['c'] ?? 4;

$url = "http://localhost/calculate.py?a=$a&b=$b&c=$c";
echo file_get_contents($url);
?>
