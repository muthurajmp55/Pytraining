#!/bin/bash

read -p "Enter a day number(1-7): " daynum
case $daynum in
1) echo "Sunday"
   ;;
2) echo "Monday"
   ;;
3) echo "Tuesday"
   ;;
4) echo "Wednesday"
   ;;
5) echo "Thursday"
   ;;
6) echo "Friday"
   ;;
7) echo "Saturday"
   ;;
*) echo "Invalid day number $daynum!!"
esac
