#!/bin/bash

Greeting() {
  echo "Greeting function says hello!!"
}

function GreetUser {
  echo "GreetUser says HELLO $*"
}

AddNos() {
  sum=0
  for number in "$@"
  do
    sum=$(expr $sum + $number)
  done
  #return $sum
  echo "The sum is $sum"
}

Greeting
GreetUser Super 			Star
result=$(AddNos 22 33 44 55 66 77)
echo result is $result

