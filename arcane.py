import os
import sys
import time
import platform
import binascii
import getpass
from os import path

OSname = str(platform.system())

# Windows OS Functions..

if OSname == "Windows":

	def clear():

		import os
		os.system('cls')

	def create(xvar):

		import os
		import getpass
		USERNAME = str(getpass.getuser())
		homepath = str('C:/Users/'+USERNAME+'/Desktop/'+xvar)
		xwebpath = str('C:/Users/'+USERNAME+'/Desktop/'+xvar+'/www')
		cascpath = str('C:/Users/'+USERNAME+'/Desktop/'+xvar+'/www/css')
		javspath = str('C:/Users/'+USERNAME+'/Desktop/'+xvar+'/www/js')
		fontpath = str('C:/Users/'+USERNAME+'/Desktop/'+xvar+'/www/fonts')
		imagpath = str('C:/Users/'+USERNAME+'/Desktop/'+xvar+'/www/img')
		htmlpath = str('C:/Users/'+USERNAME+'/Desktop/'+xvar+'/www/index.php')
		jscrpath = str('C:/Users/'+USERNAME+'/Desktop/'+xvar+'/www/js/index.js')
		cshepath = str('C:/Users/'+USERNAME+'/Desktop/'+xvar+'/www/css/main.css')
		batpath = str('C:/Users/'+USERNAME+'/Desktop/'+xvar+'/app.bat')
		os.mkdir(homepath)
		os.mkdir(xwebpath)
		os.mkdir(cascpath)
		os.mkdir(javspath)
		os.mkdir(fontpath)
		os.mkdir(imagpath)
		xdata = '''<?php
	$xtitle = "'''+xvar+''' v1.0";
?>
<html>
<head>
<title>
<?php echo $xtitle; ?>
</title>
<link type="image/ico" rel="icon" href="https://raw.githubusercontent.com/alectramell/arcane/master/img/favicon.ico">
<link type="text/css" rel="stylesheet" href="css/main.css">
<script type="text/javascript" src="js/index.js"></script>
</head>
<body>

<div id="player"><font class="labelText">64x64</font></div>

</body>
</html>
		'''
		xhtml = open(htmlpath, 'w')
		xhtml.write(xdata)
		xhtml.close()

		jdata = '''function reLoad(xvar) {

	setTimeout(function(){location.reload();}, xvar);
}

function movePlayer(e) {

	var xPos = e.clientX;
	var yPos = e.clientY;

	document.getElementById('player').style.animation = "fadeOut 600ms 1";
	document.getElementById('player').style.top = yPos - 32 + "px";
	document.getElementById('player').style.left = xPos - 32 + "px";
	document.getElementById('player').style.animation = "fadeIn 600ms 1";
	setTimeout(reset_player_animation, 300);
}

function reset_player_animation() {

	var el = document.getElementById('player');
	el.style.animation = 'none';
	el.offsetHeight; /* trigger reflow */
	el.style.animation = null; 
}

document.addEventListener('click', movePlayer);
		'''
		xjscr = open(jscrpath, 'w')
		xjscr.write(jdata)
		xjscr.close()

		cdata = '''body, html {

	background:#000000;
	background-size:cover;
	width:100%;
	height:100%;
	overflow:hidden;
	cursor:pointer;
}

#player {

	position:absolute;
	top:15px;
	left:15px;
	width:64px;
	height:64px;
	border:5px solid #4d9900;
	border-radius:10px;
	background:#333333;
}

.labelText {

	position:fixed;
	color:#ffffff;
	font-family:trebuc;
	font-size:20px;
	font-weight:regular;
	padding:20px 5px;
	opacity:1.0;
}

@font-face {

	font-family:trebuc;
	src:url(https://github.com/alectramell/arcane/raw/master/fonts/trebuc.ttf);
}

@keyframes fadeOut {

	0% {
		opacity:1.0;
	}

	100% {
		opacity:0.0;
	}
}

@keyframes fadeIn {

	0% {
		opacity:0.0;
	}

	100% {
		opacity:1.0;
	}
}
		'''

		xcssh = open(cshepath, 'w')
		xcssh.write(cdata)
		xcssh.close()

		batdata = '''@echo off

cls

TITLE Arcane Web-App Tester

cls

START /B php -t www -S localhost:8888

cls

START /W chrome --chrome-frame --window-size=640,512 --window-position=250,60 --app=http://localhost:8888

cls

echo http://localhost:8888 is active..
echo Press [ANY-KEY] to EXIT..
pause > nul

cls

TASKKILL /FI "WINDOWTITLE eq Arcane Web-App Tester*"
		'''

		batfile = open(batpath, 'w')
		batfile.write(batdata)
		batfile.close()

# Mac OS Functions..

elif OSname == "Darwin":

	def clear():

		import os
		os.system('clear')

# Linux OS Functions..

elif OSname == "Linux":

	def clear():

		import os
		os.system('clear')
