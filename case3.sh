#!/bin/bash

read -p "Enter a character: " ch
case $ch in
[0-9]) echo "Its a digit" ;;
[A-Z]) echo "Its a uppercase alphabet" ;;
[a-z]) echo "Its a lowercase alphabet" ;;
*) echo "Some other character"
esac

