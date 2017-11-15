// page1.php
<pre>
	<?php
	$page[ 'body' ] .= "
		<div class=\"body_padded\">
			<h1>Vulnerability: File Inclusion</h1>
			<div class=\"vulnerable_code_area\">
				<h3>File 1</h3>
				<hr />
				Hello <em>" . dvwaCurrentUser() . "</em><br />
				Your IP address is: <em>{$_SERVER[ 'REMOTE_ADDR' ]}</em><br /><br />
				[<em><a href=\"?page=include.php\">back</a></em>]
			</div>
			<h2>More info</h2>
				<ul>
					<li>" . dvwaExternalLinkUrlGet( 'https://en.wikipedia.org/wiki/Remote_File_Inclusion' ) . "</li>
					<li>" . dvwaExternalLinkUrlGet( 'https://www.owasp.org/index.php/Top_10_2007-A3' ) . "</li>
				</ul>
		</div>\n";
	?>
</pre>


<?php
// The page we wish to display
$file = $_GET[ 'page' ];
?> 


Hello " . dvwaCurrentUser() . "

		Your IP address is: {$_SERVER[ 'REMOTE_ADDR' ]}

The PHP function allow_url_include is not enabled.

"; } 
if( !ini_get( 'allow_url_fopen' ) ) 
{ 
	$WarningHtml .= "The PHP function allow_url_fopen is not enabled."; 
} 
$page[ 'body' ] .= "
\n"; ?>


1;cd ../../../../www/blob/vulnerabilities/fi/;ls -a -l;

total 40
drwxr-xr-x  4 www-data www-data 4096 Oct  5 15:16 .
drwxr-xr-x 14 www-data www-data 4096 Nov  8 08:45 ..
-rwxr-xr-x  1 www-data www-data  604 Oct  4 10:45 file1.php
-rwxr-xr-x  1 www-data www-data  608 Oct  4 10:45 file2.php
-rwxr-xr-x  1 www-data www-data 1113 Oct  4 10:45 file3.php
-rwxr-xr-x  1 www-data www-data  445 Oct  5 15:16 file4.php
drwxr-xr-x  2 www-data www-data 4096 Oct  4 10:45 help
-rwxr-xr-x  1 www-data www-data  971 Oct  4 10:45 include.php
-rwxr-xr-x  1 www-data www-data 1005 Oct  4 10:45 index.php
drwxr-xr-x  2 www-data www-data 4096 Oct  4 10:45 source


cd ../../../../www/blob/vulnerabilities/fi/file4.php;


Notes from class
- Upload a PHP file as an image file.
- Use the link for the PHP file to use.
- Download the first .gz file
- Once image is there, rename to .php
	- Use Task 2 command injection to rename the file (need root privleges)
	- Use MV command
- You can execute the image file as-is, don't need to rename it.
- Calls back your machine from an open socket.
- Run the netcat command on Windows.
- Don't put -p
- Use ncat for Windows - see link.