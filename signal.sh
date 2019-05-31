#!/bin/bash

displayMessage() {
  echo "OUCH That HURT don't press Ctrl-C"
}

trap displayMessage 2

n=1
while [ $n -le 10 ]
do
  echo n is $n
  n=$(expr $n + 1)
  sleep 1
done

