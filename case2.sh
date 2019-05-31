#!/bin/bash

read -p "Enter a day number(1-7): " daynum
case $daynum in
1|7) echo "HOORAY!! Weekend"
   ;;
[2-6]) echo "OH NOOOOO its a work day!!"
   ;;
*) echo "Invalid day number $daynum!!"
esac
