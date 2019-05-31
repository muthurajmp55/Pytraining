#!/bin/bash

if [ $# -lt 2 ]; then
  echo "Please give at least 2 nos as arguments!!"
  echo "Usage is " $(basename $0) " list of numbers"
  exit 1
fi

sum=0
for number in "$@"
do
  sum=$(expr $sum + $number)
done
echo "The total of $* is: $sum"

