#!/bin/bash

if [ $# -lt 1 ]; then 
	echo  "$0 [win/linux] "
fi

if [ $1 = "win" ]; then
	echo "windows will use bash git"
	cp _config.win _config.yml
elif [ $1 = 'linux' ]; then
	echo "linux, will use http"
	cp _config.linux _config.yml
else	
	echo "input err"
fi
