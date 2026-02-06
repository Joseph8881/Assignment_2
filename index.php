<?php
// index.php

// Define the command to run the Python script. 
// 'python3' is commonly used on Linux/macOS. 
// You might need to use 'python' or the full path to your python executable depending on your system configuration.
$command = escapeshellcmd('python3 script.py "This is an argument from PHP"');

// Execute the command and capture the output
$output = shell_exec($command);

echo "<h1>PHP Output:</h1>";
echo "<pre>$output</pre>";

// Basic error handling (if $output is null, something likely went wrong)
if ($output === null) {
    echo "<p style='color: red;'>Error: The command failed to execute or returned no output.</p>";
    echo "<p>Please ensure 'python3' is in your system's PATH and the script file exists.</p>";
}
?>
