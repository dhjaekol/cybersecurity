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