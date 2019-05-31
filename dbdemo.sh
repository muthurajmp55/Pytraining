#!/bin/bash

read -p "Enter DB username: " dbuser
echo -n "Enter DB password: " 
stty -echo
read dbpass
stty echo
echo
read -p "Database to use: " dbname
read -p "Table to display: " tblname
read -p "File to store data: " fil
mysql -u$dbuser -p$dbpass > $fil <<EOF
use $dbname
select * from $tblname;
EOF
cat $fil
