@echo off

cls

TITLE Arcane Web-App Tester

cls

START /B php -t www -S localhost:8888

cls

START /W chrome --chrome-frame --window-size=640,512 --window-position=250,60 --app=http://localhost:8888

cls

TASKKILL /FI "WINDOWTITLE eq Arcane Web-App Tester*"
